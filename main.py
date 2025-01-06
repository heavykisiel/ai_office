import os
from dotenv import load_dotenv
from transformers import AutoModel, AutoTokenizer
from utils.config_loader import load_config
from rich.console import Console
from rich.traceback import install
from InquirerPy import inquirer
from InquirerPy.base.control import Choice
from agents.brainstorm_room import Room
from agents.Agent import Agent
from transformers import pipeline
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
    if selected_menu_option == "Brainstorming":
        current_room = Room("Brainstorm", hf_api_token)
        current_room.start()
    elif selected_menu_option == "Review":
        print("review  TODO")
    elif selected_menu_option == "Project":
        print("project TODO")
    elif selected_menu_option == "Developers":
        print("Developers TODO")
    elif selected_menu_option == "Manage":
        print("Manage TODO")
    elif selected_menu_option == "Settings":
        print("Setting TODO")
    elif selected_menu_option == "Exit":
        quit()
    else:
        raise ValueError('Selected option doesnt match any of the possible options')

    
def main_menu():
    options = [
        Choice("Brainstorming", name="Start Brainstorming"),
        Choice("Review", name="Review Ideas"),
        Choice("Poject", name="Start to make a project"),
        Choice("Developers", name="Visist Developers team"),
        Choice("Manage", name="Manage Agents"),
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

