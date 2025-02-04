import huggingface_hub
from huggingface_hub import InferenceClient

client = InferenceClient(model="mistralai/Mistral-7B-Instruct-v0.1")

prompt = "Explain how transformers work in deep learning."
response = client.text_generation(prompt, max_new_tokens=200)

print(response)