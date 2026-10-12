from transformers import AutoModelForCausalLM


def load():
    return AutoModelForCausalLM.from_pretrained(
        "mistralai/Mistral-7B-v0.3", revision="caa1feb0e54d415e2df31207e5f4e273e33509b1",
        trust_remote_code=False)
