import time  # to add suspense

def type_effect(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.05)
    print()

# Introduction
print("Hey there! This is your first match as the new coach! ⚽")
time.sleep(1)

coach_name = input("What's your name Coach?: ")
print("You have all the power how this important game plays out today,", coach_name, "‼️")
print("What formation do you want to play today?\n")
time.sleep(2)

# Formation decision
print("Choose your formation:")
print("1 - 4-4-2 (Balanced)")
print("2 - 3-4-3 (Offensive)")
print("3 - 5-3-2 (Defensive)")

formation = input("Enter 1, 2, or 3: ")

if formation == "1":
    print("You chose a balanced formation. Your players seem calm.")
elif formation == "2":
    print("️You chose an offensive starting eleven. The crowd is excited!")
elif formation == "3":
    print("You chose to play a defensive formation.")
else:
    print("🤔 Invalid choice. We'll go with the default 4-4-2.")
    formation = "1"

time.sleep(1)

# Player decision
print("\n🌟 A young talented player wants to start in today's big game.")
print("Do you let him play from the start?")
print("1 - Yes")
print("2 - No, just the second half")

young_player = input("Enter 1 or 2: ")

if young_player == "1":
    print("👏 The crowd loves your brave decision!")
elif young_player == "2":
    print("👴 You chose experience over talent. Let's see how it plays out!")
else:
    print("🤷 No decision made. The assistant coach went with the experienced lineup, but the young player will play the second half.")

type_effect("The crowd is going wild as your team steps onto the field...")
type_effect("The game is really even... But then!!!")
time.sleep(1)

# Penalty situation
print("\n⏱️ It's the 89th minute. Your team gets a penalty kick! The score is 2-2.")
print("Who takes the shot?")
print("1 - The experienced team captain")
print("2 - The young talented player")

penalty_choice = input("Choose 1 or 2: ")

if penalty_choice == "1":
    print("The captain walks to the ball...")
    time.sleep(2)
    print("He shoots!")
    time.sleep(1)
    print("💥 GOAL! You win the game!")
    result = "win"
elif penalty_choice == "2":
    print("The young player nervously steps up...")
    time.sleep(2)
    print("He shoots...")
    time.sleep(3)
    if young_player == "1":
        print("😱 The goalkeeper saves it! The opponents counter-attack and score. You lose the game...")
        result = "lose"
    else:
        print("😬 He wasn’t fully ready... the shot goes way off. It's a draw.")
        result = "draw"
else:
    print("😐 Another player takes the shot unexpectedly... He misses. The game ends 2-2.")
    result = "draw"

time.sleep(2)

# Upcoming Training strategy
print("\n⚽️ What is the focus of the upcoming training sessions?")
print("Do you focus your next training session on...")
print("1 - Defense")
print("2 - Attack")

training_focus = input("Choose 1 or 2: ")

if training_focus == "1":
    print("🥅 Your defense is excited for the upcoming training!")
elif training_focus == "2":
    print("🔥 Your strikers are eager to improve their performance!")
else:
    print("📋 Next Training is cancelled... Risky!")

time.sleep(1)

# Number input using while loop
print("\n🎤 Rate your own coaching performance today (1 to 10):")


while True:
    rating = input("Enter a number from 1 to 10: ")
    if rating.isdigit():
        rating = int(rating)
        if rating >= 1 and rating <= 10:
            break
        else:
            print("Please enter a number in the correct range!")
    else:
        print("That's not a valid number.")

if rating >= 8:
    print("🏅 Great job, Coach", coach_name + "!")
elif rating >= 5:
    print("👍 Decent effort. Room for improvement.")
else:
    print("😬 Tough day. Better luck next match!")

time.sleep(1)


# Final message
print("\n🎮 Game Over!")
print("📊 Final Result:", result.upper())
print("Thanks for playing,", coach_name, "!")