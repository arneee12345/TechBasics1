import time

# constants
TYPING_DELAY = 0.05
SHORT_DELAY = 1
LONG_DELAY = 2


# Helping functions (modularizing)

def type_effect(text):  # Prints text with typing effect
    for char in text:
        print(char, end='', flush=True)
        time.sleep(TYPING_DELAY)
    print()


def get_input(prompt, valid_options):  # Asks for input and checks if it's in valid options
    choice = input(prompt)
    if choice not in valid_options:
        print("🤷 Invalid input, using default.")
        return valid_options[0]
    return choice


def choose_formation():  # asks for input to choose formation and prints fitting answer
    print("Choose your formation:")
    print("1 - 4-4-2 (Balanced)")
    print("2 - 3-4-3 (Offensive)")
    print("3 - 5-3-2 (Defensive)")
    choice = get_input("Enter 1, 2, or 3: ", ["1", "2", "3"])
    if choice == "1":
        print("You chose a balanced formation. Your players seem calm.")
    elif choice == "2":
        print("️You chose an offensive starting eleven. The crowd is excited!")
    elif choice == "3":
        print("You chose to play a defensive formation.")
    time.sleep(SHORT_DELAY)
    return choice


def player_decision():  # asks for input and prints fitting answer
    print("\n🌟 A young talented player wants to start in today's big game.")
    print("Do you let him play from the start?")
    print("1 - Yes")
    print("2 - No, just the second half")
    choice = get_input("Enter 1 or 2: ", ["1", "2"])
    if choice == "1":
        print("👏 The crowd loves your brave decision!")
    elif choice == "2":
        print("👴 You chose experience over talent. Let's see how it plays out!")
    return choice


def penalty_scene(young_player_choice):  # asks for input and prints fitting answer
    print("\n⏱️ It's the 89th minute. Your team gets a penalty kick! The score is 2-2.")
    print("Who takes the shot?")
    print("1 - The experienced team captain")
    print("2 - The young talented player")
    choice = get_input("Choose 1 or 2: ", ["1", "2"])

    if choice == "1":
        print("The captain walks to the ball...")
        time.sleep(LONG_DELAY)
        print("He shoots!")
        time.sleep(SHORT_DELAY)
        print("💥 GOAL! You win the game!")
        return "win"

    elif choice == "2":
        print("The young player nervously steps up...")
        time.sleep(LONG_DELAY)
        print("He shoots...")
        time.sleep(LONG_DELAY)
        if young_player_choice == "1":
            print("😱 The goalkeeper saves it! The opponents counter-attack and score. You lose the game...")
            return "lose"
        else:
            print("😬 He wasn’t fully ready... the shot goes way off. It's a draw.")
            return "draw"


def training_decision():  # asks for input and prints fitting answer
    print("\n⚽️ What is the focus of the upcoming training sessions?")
    print("1 - Defense")
    print("2 - Attack")
    choice = get_input("Choose 1 or 2: ", ["1", "2"])
    if choice == "1":
        print("🥅 Your defense is excited for the upcoming training!")
    elif choice == "2":
        print("🔥 Your strikers are eager to improve their performance!")


def rate_performance(coach_name):  # ask for input and print fitting answer
    print("\n🎤 Rate your own coaching performance today (1 to 10):")
    while True:
        rating = input("Enter a number from 1 to 10: ")
        if rating.isdigit():
            rating = int(rating)
            if 1 <= rating <= 10:
                break
        print("❌ Please enter a valid number in range.")

    if rating >= 8:
        print(f"🏅 Great job, Coach {coach_name}!")
    elif rating >= 5:
        print("👍 Decent effort. Room for improvement.")
    else:
        print("😬 Tough day. Better luck next match!")


# main function

def main():
    print("Hey there! This is your first match as the new coach! ⚽")
    time.sleep(SHORT_DELAY)

    coach_name = input("What's your name Coach?: ")
    print(f"You have all the power how this important game plays out today, {coach_name} ‼️\n")
    time.sleep(SHORT_DELAY)

    formation = choose_formation()
    young_player = player_decision()

    type_effect("The crowd is going wild as your team steps onto the field...")
    type_effect("The game is really even... But then!!!")

    result = penalty_scene(young_player)
    training_decision()
    rate_performance(coach_name)

    time.sleep(SHORT_DELAY)
    print("\n🎮 Game Over!")
    print("📊 Final Result:", result.upper())
    print(f"Thanks for playing, {coach_name}!")


# Entry Point
if __name__ == "__main__":
    main()
