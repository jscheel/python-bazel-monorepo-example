import os
import redis


class TokenWallet:
    DAILY_TOKENS = 4096 * 100  # max gpt-3.5 context window * 100
    WALLET_LIFETIME = 24 * 60 * 60  # 24 hours

    def __init__(self, owner_gid: str, infinite: bool = False):
        self.owner_gid = owner_gid
        self.infinite = infinite
        self.redis = redis.from_url(os.getenv("REDIS_DSN"))

    def withdraw(self, amount: int) -> bool:
        if amount < 0:
            raise ValueError("Amount cannot be negative")
        if self.infinite:
            return True
        if amount > self.balance(keep_lock=True):
            self.redis.unwatch()
            return False
        self.redis.decrby(self.redis_key(), amount)
        self.redis.unwatch()
        return True

    def deposit(self, amount: int) -> bool:
        if amount < 0:
            raise ValueError("Amount cannot be negative")
        if self.infinite or amount == 0:
            return True
        self.redis.incrby(self.redis_key(), amount)
        return True

    def balance(self, keep_lock: bool = False) -> int:
        if self.infinite:
            return float("inf")
        self.redis.watch(self.redis_key())
        stored_balance = self.redis.get(self.redis_key())
        if stored_balance is None:
            stored_balance = self.daily_tokens()
            self.redis.set(
                self.redis_key(), stored_balance, ex=self.WALLET_LIFETIME, nx=True
            )
        if not keep_lock:
            self.redis.unwatch()
        return int(stored_balance)

    def redis_key(self) -> str:
        return f"tokenwallet:{self.owner_gid}"

    def daily_tokens(self) -> int:
        # TODO (jscheel): Figure out a better way to handle this.
        return self.DAILY_TOKENS
