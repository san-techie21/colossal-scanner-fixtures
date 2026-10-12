import secrets


def reset_token() -> str:
    token = secrets.token_urlsafe(32)
    return token
