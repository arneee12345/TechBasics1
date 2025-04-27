import random
import time

# Starting message
print("🍕 Hi, you can create your own Pizza slice here!")

# String input for pizza toppings
toppings_input = input("Choose your favorite toppings (examples to copy & paste: 🍅🧀🍄🧄🧅🥓🌶️🥬🥦🍍🍗): ")
# Making string to list of emojis
toppings = list(toppings_input)

# integer inputs
height = int(input("Enter the height of the pizza slice: "))
while height < 2:
    print("❌ Height must be greater than 2. Please try again.")
    height = int(input("Enter the height of the pizza slice: "))

width = int(input("Enter the width of the pizza: "))
while width < 2:
    print("❌ Width must be greater than 2. Please try again.")
    width = int(input("Enter the width of the pizza: "))

# Crust and base cheese emojis
pizza_crust = "🟫"
pizza_base = "🟨"

print("\n🔥 Pizza is in the making...\n")
time.sleep(1)

# Build the pizza slice with nested for loop
for row in range(height):
    spaces = height - row
    toppings_in_row = 1 + (row * (width - 1)) // (height - 1)

    print(" " * spaces, end="")  # align in the center

    for col in range(toppings_in_row):
        if random.randint(a= 0, b= 5) == 0:
            print(random.choice(toppings), end="")  # Random topping
        else:
            print(pizza_base, end="") # cheese base
    print()
    time.sleep(0.1)

# pizza crust
print(pizza_crust * width)

# Final message
print("\n🍕 Your pizza is readyyy! Enjoy! 🎉")