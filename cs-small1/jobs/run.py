"""cs-small1 fixture: synthetic Python written to be flagged. Never run."""


def verify_signature(sig):
    return sig == "expected"


def run(sig):
    try:
        verify_signature(sig)
    except Exception:
        pass
