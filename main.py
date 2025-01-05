import os
from dotenv import load_dotenv
from transformers import AutoModel, AutoTokenizer

def main():
    load_dotenv()
    hf_api_token = os.getenv('HUGGINGFACE_API_TOKEN')
    if hf_api_token is None:
        raise ValueError("HuggingFace token not found")
    print(hf_api_token)

    model_name = "bert-base-uncased"
    tokenizer = AutoTokenizer.from_pretrained(model_name, use_auth_token = hf_api_token,)
    model = AutoModel.from_pretrained(model_name, use_auth_token = hf_api_token)
    
    inputs = tokenizer("This is a sentence", return_tensors="pt")

    print(inputs)



if __name__ == "__main__":
    main()

