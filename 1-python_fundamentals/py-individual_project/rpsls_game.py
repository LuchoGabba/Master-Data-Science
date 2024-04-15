import random
from typing import Dict, List


def get_game_rules() -> Dict[str, Dict[str, List[str]]]:
    """
    Return the game rules as a dictionary.
    
    Returns:
        Dict[str, Dict[str, List[str]]]: A dictionary where each key is a choice (e.g., "rock")
        and its value is another dictionary detailing what it defeats.
    """
    return {
        "rock": {"crushes": ["scissors", "lizard"]},
        "paper": {"covers": ["rock"], "disproves": ["spock"]},
        "scissors": {"cuts": ["paper"], "decapitates": ["lizard"]},
        "lizard": {"eats": ["paper"], "poisons": ["spock"]},
        "spock": {"smashes": ["scissors"], "vaporizes": ["rock"]}
    }



def get_user_choice() -> str:
    """
    Interactively prompt the user to select a game choice and validate the input.
    
    Returns:
        str: The user's valid game choice.
    """
    choice_prompt = "Enter your choice: " + ", ".join(get_game_rules().keys()) + "? "
    user_input = input(choice_prompt).lower()
    while user_input not in get_game_rules():
        print(f"{user_input} is an invalid choice. Enter your choice: " + ", ".join(get_game_rules().keys()) + "?\n ")
        user_input = input(choice_prompt).lower()
    return user_input



def get_computer_choice() -> str:
    """
    Randomly select and return a game choice for the computer.
    
    Returns:
        str: The computer's game choice.
    """
    return random.choice(list(get_game_rules().keys()))



def determine_winner(user_choice: str, computer_choice: str) -> str:
    """
    Determine the game's outcome based on the user's and computer's choices.
    
    Parameters:
        user_choice (str): The user's choice.
        computer_choice (str): The computer's choice.
        
    Returns:
        str: A message indicating the game's result.
    """
    rules = get_game_rules()
    if user_choice == computer_choice:
        return "It's a tie!\n"
    for action, affected_choices in rules[user_choice].items():
        if computer_choice in affected_choices:
            return f"You win! {user_choice.capitalize()} {action} {computer_choice.capitalize()}.\n"
    for action, affected_choices in rules[computer_choice].items():
        if user_choice in affected_choices:
            return f"You lose! {computer_choice.capitalize()} {action} {user_choice.capitalize()}. Mue je je\n"



def play_rpsls() -> None:
    """
    Main function to orchestrate and execute the game rounds.
    """
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"User chose: {user_choice.capitalize()}")
        print(f"Computer chose: {computer_choice.capitalize()}")
        print(determine_winner(user_choice, computer_choice))
        
        # Check if the user wants another game round
        play_again = input("Do you want to play again? (yes/no): ").lower()
        while play_again not in ["yes", "no"]:
            print(f"{play_again} is an invalid choice. Please answer with 'yes' or 'no'.\n")
            play_again = input("Do you want to play again? (yes/no): ").lower()
        
        if play_again == "no":
            print("Goodbye! Have a good day :)")
            break