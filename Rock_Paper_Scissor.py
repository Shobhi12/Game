import random

class RockPaperScissors:
    def __init__(self):
        self.user_score = 0
        self.computer_score = 0

    def get_computer_choice(self):
        choices = ["rock", "paper", "scissors"]
        return random.choice(choices)

    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "tie"
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "scissors" and computer_choice == "paper") or \
             (user_choice == "paper" and computer_choice == "rock"):
            return "user"
        else:
            return "computer"

    def play_round(self):
        user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
        while user_choice not in ["rock", "paper", "scissors"]:
            user_choice = input("Invalid input. Please enter rock, paper, or scissors: ").lower()
        computer_choice = self.get_computer_choice()
        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}\n")
        winner = self.determine_winner(user_choice, computer_choice)
        if winner == "tie":
            print("It's a tie!")
        elif winner == "user":
            print("You win this round!")
            self.user_score += 1
        else:
            print("Computer wins this round!")
            self.computer_score += 1
        print(f"Score - You: {self.user_score}, Computer: {self.computer_score}\n")

    def play_game(self):
        while True:
            self.play_round()
            play_again = input("Do you want to play another round? (yes/no): ").lower()
            while play_again not in ["yes", "no"]:
                play_again = input("Invalid input. Please enter yes or no: ").lower()
            if play_again == "no":
                print("Thanks for playing!")
                break

def main():
    game = RockPaperScissors()
    print("Welcome to Rock-Paper-Scissors!")
    print("-------------------------------")
    print("Instructions:")
    print("1. Enter your choice (rock, paper, or scissors) when prompted.")
    print("2. The computer will generate a random choice.")
    print("3. The winner of each round will be determined based on the game's rules.")
    print("4. The score will be displayed after each round.")
    print("5. You can choose to play another round or quit the game.")
    game.play_game()

if __name__ == "__main__":
    main()
