import random

def check_winner(player1, player2):
    """Checks who wins the round."""
    if player1 == player2:
        return "tie"
    if (player1 == 'rock' and player2 == 'scissors') or \
       (player1 == 'paper' and player2 == 'rock') or \
       (player1 == 'scissors' and player2 == 'paper'):
        return "player1"
    return "player2"

def play_game():
    print("Choose mode:\n1 for Single Player\n2 for Player-1 vs Player-2")
    while True:
        mode = input("Enter your mode preference: ")
        if mode in ['1', '2']:
            mode = int(mode)
            break
        print("Invalid choice. Please enter 1 or 2.")

    if mode == 1:
        # Single-player mode
        print("You are playing with the computer!")
        game = ['rock', 'paper', 'scissors']
        single_player_points = 0
        computer_points = 0

        while single_player_points < 3 and computer_points < 3:
            print("\nChoose one option: rock, paper, or scissors")
            single_player = input("Your choice: ").lower()
            if single_player not in game:
                print("Invalid input. Please try again!")
                continue

            computer = random.choice(game)
            print(f"Computer chose: {computer}")

            result = check_winner(single_player, computer)
            if result == "tie":
                print("No points this round!")
            elif result == "player1":
                single_player_points += 1
                print("You score a point!")
            else:
                computer_points += 1
                print("Computer scores a point!")

            print(f"Scores -> You: {single_player_points}, Computer: {computer_points}")

        if single_player_points > computer_points:
            print("\nCongratulations, you win!")
        else:
            print("\nComputer wins. Better luck next time!")

    elif mode == 2:
        # Two-player mode
        print("Player-1 vs Player-2")
        player_1_score = 0
        player_2_score = 0

        while player_1_score < 3 and player_2_score < 3:
            print("\nChoose one option: rock, paper, or scissors")
            player_1 = input("Player 1: ").lower()
            player_2 = input("Player 2: ").lower()

            if player_1 not in ['rock', 'paper', 'scissors'] or \
               player_2 not in ['rock', 'paper', 'scissors']:
                print("Invalid input. Please try again!")
                continue

            result = check_winner(player_1, player_2)
            if result == "tie":
                print("No points this round!")
            elif result == "player1":
                player_1_score += 1
                print("Player 1 scores a point!")
            else:
                player_2_score += 1
                print("Player 2 scores a point!")

            print(f"Scores -> Player 1: {player_1_score}, Player 2: {player_2_score}")

        if player_1_score > player_2_score:
            print("\nPlayer 1 wins the game!")
        else:
            print("\nPlayer 2 wins the game!")

play_game()
