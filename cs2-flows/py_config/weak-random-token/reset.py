import random
import string


def reset_token() -> str:
    token = "".join(random.choice(string.ascii_letters + string.digits) for _ in range(32))
    return token
