import random
import time
import sys

cards = ["A", 2, 3, 4, 5, 6, 7, 8, 9, "J", "Q", "K"] * 4
money = int(input("How much would you like to deposit: $"))


def convert_card(card, current_sum):
    """Convert card to its numeric value, handling Aces dynamically."""
    if card in ["J", "Q", "K"]:
        return 10
    elif card == "A":
        return 11 if current_sum + 11 <= 21 else 1
    else:
        return card

def play_again():
    """Ask the player if they want to play again."""
    response = input("Do you want to play again? (y/n): ").lower()
    if response == "y":
        game()
    else:
        print("Thanks for playing!")
        print(f"Your final earnings are: ${money - 1000}")
        time.sleep(5)
        sys.exit()

def game():
    """Main Blackjack game logic."""
    global money
    print("=========================================")
    print("Welcome to Blackjack!")
    print(f"Your current balance is: ${money}")

    # Betting logic
    while True:
        try:
            betamt = int(input("Enter your bet amount: $"))
            if money <= 0:
                print("You're broke. Better luck next time!")
                print("Kicking you out...")
                time.sleep(5)
                sys.exit()
            elif betamt > money:
                print("Invalid bet amount. Try again.")
            else:
                break
        except ValueError:
            print("Please enter a valid number.")

    money -= betamt

    # Deal initial cards
    player_hand = [random.choice(cards), random.choice(cards)]
    dealer_hand = [random.choice(cards), random.choice(cards)]

    player_sum = sum(convert_card(card, 0) for card in player_hand)
    dealer_sum = sum(convert_card(card, 0) for card in dealer_hand)

    print("=============================================")
    print(f"Your hand: {player_hand} (Total: {player_sum})")
    print(f"Dealer shows: {dealer_hand[0]}")
    print("=============================================")

    # Player's turn
    while player_sum < 21:
        choice = input("Do you want to hit or stand? (hit/stand): ").lower()
        if choice == "hit":
            new_card = random.choice(cards)
            player_sum += convert_card(new_card, player_sum)
            player_hand.append(new_card)
            print(f"You drew: {new_card} (Total: {player_sum})")
        elif choice == "stand":
            break
        else:
            print("Invalid choice. Please type 'hit' or 'stand'.")

    if player_sum > 21:
        print("=============================================")
        print("Bust! You lose.")
        print(f"Dealer's hand: {dealer_hand} (Total: {dealer_sum})")
        print("=============================================")
        play_again()
        return

    # Dealer's turn
    print(f"Dealer's hand: {dealer_hand} (Total: {dealer_sum})")
    while dealer_sum < 17:
        new_card = random.choice(cards)
        dealer_sum += convert_card(new_card, dealer_sum)
        dealer_hand.append(new_card)
        print(f"Dealer draws: {new_card} (Total: {dealer_sum})")

    # Determine winner
    if dealer_sum > 21 or player_sum > dealer_sum:
        print("=============================================")
        print("You win!")
        print("=============================================")
        money += betamt * 2
    elif player_sum < dealer_sum:
        print("=============================================")
        print("Dealer wins!")
        print("=============================================")
    else:
        print("=============================================")
        print("It's a tie!")
        print("=============================================")
        money += betamt

    print(f"Your final hand: {player_hand} (Total: {player_sum})")
    print(f"Dealer's final hand: {dealer_hand} (Total: {dealer_sum})")
    print("=============================================")
    play_again()

game()
