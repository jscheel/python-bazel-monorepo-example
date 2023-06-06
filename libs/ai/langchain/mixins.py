# TODO (jscheel): Fix completion token calculation, estimate should include max tokens
# or the rest of the context window so that we always deposit back instead of needing
# to take more out later.

# TODO (jscheel): Abstract code in _generate and _agenerate so that it can written once

from typing import List, Optional
from langchain.schema import (
    BaseMessage,
)
from pydantic import BaseModel, validator
from libs.ai.tokens.token_wallet import TokenWallet


class MeteredLLMMixin(BaseModel):
    requester_gid: str
    wallet: Optional[TokenWallet]

    class Config:
        arbitrary_types_allowed = True

    @validator("wallet", pre=True, always=True)
    def default_wallet(cls, v, values, **kwargs):
        requester_gid = values.get("requester_gid")
        if v is TokenWallet:
            return v
        if v is None and values["requester_gid"]:
            return TokenWallet(owner_gid=requester_gid)
        raise "No wallet could be instantiated"

    def _generate(self, messages: List[BaseMessage], stop: Optional[List[str]] = None):
        budget = self.get_num_tokens_from_messages(messages=messages)
        self.wallet.withdraw(budget)
        spend = None
        try:
            result = super()._generate(messages=messages, stop=stop)
            spend = result.llm_output.get("token_usage", {}).get(
                "completion_tokens", None
            )
        finally:
            spend = spend or 0
        self._reconcile_budget(budget, spend)
        return result

    async def _agenerate(
        self, messages: List[BaseMessage], stop: Optional[List[str]] = None
    ):
        budget = self.get_num_tokens_from_messages(messages=messages)
        self.wallet.withdraw(budget)
        spend = None
        try:
            result = await super()._agenerate(messages=messages, stop=stop)
            spend = result.llm_output.get("token_usage", {}).get(
                "completion_tokens", None
            )
        finally:
            spend = spend or 0
        self._reconcile_budget(budget, spend)
        return result

    def _reconcile_budget(self, budget: int, spend: int) -> None:
        difference = budget - spend
        if difference > 0:
            self.wallet.deposit(difference)
        elif difference < 0:
            # TODO (jscheel): Something went wrong and we spent more than expected.
            # If this number is way off we should probably log in bugsnag.
            pass
