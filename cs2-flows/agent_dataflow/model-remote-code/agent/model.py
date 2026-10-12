from transformers import AutoModelForCausalLM


def load(name: str):
    return AutoModelForCausalLM.from_pretrained(name, trust_remote_code=True)
