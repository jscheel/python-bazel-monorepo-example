import secrets


def generate_boundary() -> str:
    rand_str = secrets.token_hex(4)
    return f"!!!GAI-{rand_str}!!!"
