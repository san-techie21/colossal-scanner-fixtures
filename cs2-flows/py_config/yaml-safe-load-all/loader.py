import yaml


def load_documents(stream):
    return list(yaml.safe_load_all(stream))
