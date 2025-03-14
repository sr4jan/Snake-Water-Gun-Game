import random

def get_computer_choice():
    return random.choice(['snake', 'water', 'gun'])

def get_winner(player, computer):
    if player == computer:
        return "It's a tie!"
    elif (player == 'snake' and computer == 'water') or \
         (player == 'water' and computer == 'gun') or \
         (player == 'gun' and computer == 'snake'):
        return "You win!"
    else:
        return "Computer wins!"

def main():
    print("Welcome to Snake-Water-Gun Game!")
    choices = ['snake', 'water', 'gun']
    player_choice = input("Enter your choice (snake/water/gun): ").lower()
    
    if player_choice not in choices:
        print("Invalid choice. Please choose snake, water, or gun.")
        return
    
    computer_choice = get_computer_choice()
    print(f"Computer chose: {computer_choice}")
    
    result = get_winner(player_choice, computer_choice)
    print(result)

if __name__ == "__main__":
    main()
