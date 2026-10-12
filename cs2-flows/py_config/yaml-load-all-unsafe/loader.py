import yaml


def load_documents(stream):
    return list(yaml.load_all(stream, Loader=yaml.UnsafeLoader))
