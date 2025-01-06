import os
from dotenv import load_dotenv
from transformers import AutoModel, AutoTokenizer
from utils.config_loader import load_config
from rich.console import Console
from rich.traceback import install
from InquirerPy import inquirer
from InquirerPy.base.control import Choice
install()


def main():
    test = True
    load_dotenv()
    config = load_config()
    hf_api_token = os.getenv('HUGGINGFACE_API_TOKEN')
    if hf_api_token is None:
        raise ValueError("HuggingFace token not found")
    if test:
       # print(hf_api_token)
       # print("Config loaded")
       # print(config)
        print()
    
    selected_menu_option = main_menu()
    #model_name = "bert-base-uncased"
    #tokenizer = AutoTokenizer.from_pretrained(model_name, use_auth_token = hf_api_token,)
    #model = AutoModel.from_pretrained(model_name, use_auth_token = hf_api_token)
    
    #inputs = tokenizer("This is a sentence", return_tensors="pt")

    #print(inputs)


def main_menu():
    options = [
        Choice("Start Brainstorming", name="Start Brainstorming"),
        Choice("Review Ideas", name="Review Ideas"),
        Choice("Start to make a project", name="Start to make a project"),
        Choice("Visist Developers team", name="Visist Developers team"),
        Choice("Manage Agents", name="Manage Agents"),
        Choice("Settings", name="Settings"),
        Choice("Exit", name="Exit")
    ]
    choice = inquirer.select(
        message="AI Office Main Menu:",
        choices=options,
        pointer="=>",
    ).execute()
    return choice

if __name__ == "__main__":
    main()

