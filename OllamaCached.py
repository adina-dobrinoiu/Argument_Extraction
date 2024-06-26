import os
from tqdm import tqdm
import ollama

# Set environment variable to save models to the models folder in the repository.
os.environ["OLLAMA_MODELS"] = "./models"
os.environ["OLLAMA_KEEP_ALIVE"] = "1m"


def check_and_download_model(model_name: str) -> None:
    """
    Checks if the specified LLM exists locally and downloads it if necessary.

    Args:
        model_name (str): Tag of the LLM.
    """
    model_exists: bool = False

    existing_models = ollama.list()["models"]
    print(existing_models)
    for model in existing_models:
        if model["name"] == model_name:
            model_exists = True

    if not model_exists:
        print("Model Uncached - Downloading...")
        current_digest, bars = '', {}
        for progress in ollama.pull(model_name, stream=True):
            digest = progress.get('digest', '')
            if digest != current_digest and current_digest in bars:
                bars[current_digest].close()

            if not digest:
                print(progress.get('status'))
                continue

            if digest not in bars and (total := progress.get('total')):
                bars[digest] = tqdm(total=total, desc=f'pulling {digest[7:19]}', unit='B', unit_scale=True)

            if completed := progress.get('completed'):
                bars[digest].update(completed - bars[digest].n)

            current_digest = digest
        print("Download Complete.")
    else:
        print("Model Cached - Using Cached Version...")


def llm_chat(model_name: str, message: str) -> str:
    """
    Chat with the llm

    Args:
        model_name (str): Tag of the LLM.
        message (str): The prompt to provide to the LLM.
    Returns:
        response (str): The response from the assistant.
    """
    check_and_download_model(model_name)

    response = ollama.chat(model=model_name, messages=message, format="json", stream=False)
    return response["message"]["content"]

