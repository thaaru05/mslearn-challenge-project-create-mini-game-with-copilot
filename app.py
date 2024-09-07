import random

def get_computer_choice():
    """Randomly select the computer's choice."""
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(player_choice, computer_choice):
    """Determine the winner based on game rules."""
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (player_choice == 'rock' and computer_choice == 'scissors') or \
         (player_choice == 'scissors' and computer_choice == 'paper') or \
         (player_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "You lose!"

def print_score(wins, total_games):
    """Print the player's score."""
    print(f"\nFinal Score: {wins} win(s) out of {total_games} game(s)")

def main():
    """Main function to run the game loop."""
    wins = 0
    total_games = 0
    valid_choices = ['rock', 'paper', 'scissors']
    
    while True:
        player_choice = input("Enter rock, paper, or scissors (or 'quit' to exit): ").strip().lower()
        
        if player_choice == 'quit':
            print_score(wins, total_games)
            break
        
        if player_choice not in valid_choices:
            print("Invalid option. Please choose rock, paper, or scissors.")
            continue
        
        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")
        
        result = determine_winner(player_choice, computer_choice)
        print(result)
        
        if result == "You win!":
            wins += 1
        total_games += 1

if __name__ == "__main__":
    main()
