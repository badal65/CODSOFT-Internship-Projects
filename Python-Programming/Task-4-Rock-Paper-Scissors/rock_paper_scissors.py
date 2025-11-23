import random

def get_computer_choice():
    """Generate random choice for computer"""
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    """Determine the winner based on game logic"""
    if user_choice == computer_choice:
        return 'tie'
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return 'user'
    else:
        return 'computer'

def display_result(user_choice, computer_choice, result):
    """Display the result of the game"""
    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    
    if result == 'tie':
        print("It's a tie!")
    elif result == 'user':
        print("Congratulations! You win!")
    else:
        print("Computer wins! Better luck next time.")

def play_game():
    """Main game function"""
    user_score = 0
    computer_score = 0
    
    print("=" * 40)
    print("Welcome to Rock-Paper-Scissors Game!")
    print("=" * 40)
    
    while True:
        print("\nChoose your move:")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")
        print("4. Quit")
        
        choice = input("\nEnter your choice (1-4): ")
        
        if choice == '4':
            print("\n" + "=" * 40)
            print("Final Score:")
            print(f"You: {user_score} | Computer: {computer_score}")
            print("Thanks for playing!")
            print("=" * 40)
            break
        
        if choice not in ['1', '2', '3']:
            print("Invalid choice! Please try again.")
            continue
        
        # Convert choice to move
        moves = {'1': 'rock', '2': 'paper', '3': 'scissors'}
        user_choice = moves[choice]
        computer_choice = get_computer_choice()
        
        # Determine winner
        result = determine_winner(user_choice, computer_choice)
        display_result(user_choice, computer_choice, result)
        
        # Update scores
        if result == 'user':
            user_score += 1
        elif result == 'computer':
            computer_score += 1
        
        print(f"\nCurrent Score - You: {user_score} | Computer: {computer_score}")

if __name__ == "__main__":
    play_game()
