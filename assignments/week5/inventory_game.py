import random

# CONFIGURATION / CONSTANTS
MAX_ITEMS = 5
has_checked_out = False

# PLAYER INVENTORY (Pre-filled with some starter items)
bag = [
    {"name": "Water Bottle", "type": "tool", "uses": 2, "permanent": True},
    {"name": "Energy Bar", "type": "food", "uses": 1}
]

# STORE AISLES
store = {
    "supplements": [
        {"name": "Protein Bar", "type": "food", "uses": 1},
        {"name": "Vitamin C", "type": "recovery", "uses": 1},
        {"name": "Pre-Workout", "type": "boost", "uses": 1},
        {"name": "Electrolytes", "type": "recovery", "uses": 2},
        {"name": "Shaker Bottle", "type": "tool"},
        {"name": "Magnesium", "type": "recovery", "uses": 1}
    ],
    "snacks": [
        {"name": "Granola Bar", "type": "food", "uses": 1},
        {"name": "Trail Mix", "type": "food", "uses": 2},
        {"name": "Protein Chips", "type": "food", "uses": 1}
    ],
    "vitamins": [
        {"name": "Vitamin D", "type": "recovery", "uses": 1},
        {"name": "Omega 3", "type": "recovery", "uses": 1},
        {"name": "Zinc", "type": "recovery", "uses": 1}
    ]
}

current_section = "supplements"

# CORE FUNCTIONS

def list_store_items():
    print("\n🛒 Store Overview:")
    for section, stock in store.items():
        print(f"\n📍 {section.title()} Section:")
        if stock:
            for product in stock:
                print(f"- {product['name']} (Type: {product['type']}, Uses: {product.get('uses', '∞')})")
        else:
            print("(Empty section.)")

def list_inventory():
    print("\n🎒 Your Inventory:")
    if bag:
        for obj in bag:
            print(f"- {obj['name']} (Type: {obj['type']}, Uses: {obj.get('uses', '∞')})")
    else:
        print("(Your bag is empty.)")

def take_item(item_name):
    if has_checked_out:
        print("🚫 You already checked out. No more picking allowed!")
        return
    if len(bag) >= MAX_ITEMS:
        print("❌ Bag full. Drop something to make space.")
        return
    for obj in store[current_section]:
        if obj['name'].lower() == item_name:
            bag.append(obj)
            store[current_section].remove(obj)
            print(f"✅ You picked up {obj['name']}.")
            return
    print("❌ Item not found in this section.")

def remove_item(item_name):
    if has_checked_out:
        print("🚫 You already left. No dropping allowed!")
        return
    for obj in bag:
        if obj['name'].lower() == item_name:
            bag.remove(obj)
            store[current_section].append(obj)
            print(f"🗑️ Dropped {obj['name']} into {current_section} section.")
            return
    print("❌ Item not in your bag.")

def consume_item(item_name):
    if not has_checked_out:
        print("🚫 You need to check out before using anything.")
        return
    for obj in bag:
        if obj['name'].lower() == item_name:
            if obj.get('uses', 0) > 1:
                obj['uses'] -= 1
                print(f"⚡ Used {obj['name']}. Remaining uses: {obj['uses']}")
            elif obj.get('uses', 0) == 1:
                if obj.get("permanent"):
                    obj['uses'] = 0
                    print(f"💧 You emptied your {obj['name']} but kept the bottle.")
                else:
                    bag.remove(obj)
                    print(f"⚡ You used up {obj['name']}. It's gone now.")
            else:
                print(f"🚫 {obj['name']} is empty.")
            return
    print("❌ You don’t have that item.")

def inspect_item(item_name):
    all_items = bag + store[current_section]
    for obj in all_items:
        if obj['name'].lower() == item_name:
            print(f"🔍 {obj['name']} is a {obj['type']} item. Uses: {obj.get('uses', '∞')}")
            return
    print("❌ Couldn't find that item.")

def switch_section(destination):
    global current_section
    if has_checked_out:
        print("🚫 Too late to explore more. You've checked out.")
        return
    if destination in store:
        current_section = destination
        print(f"➡️ Moved to the {current_section} section.")
    else:
        print("❌ Invalid section name.")

def show_help():
    print("\n📝 Commands Guide:")
    print("inventory - check your items")
    print("room - list items in all sections")
    print("pickup [item] - take an item")
    print("drop [item] - return an item")
    print("use [item] - consume or use something")
    print("examine [item] - inspect an item")
    print("go [section] - move to a new section")
    print("leave - checkout and exit the store")
    print("help - see this list again")
    print("exit - quit the game")

# GAME INTRO
print("Welcome to the first FitMart-Store in your town! 🛍️")
print("Your mission: Pick up to 5 useful items and check out!")
show_help()

# GAME LOOP
while True:
    action = input("\n👉 What would you like to do? ").strip().lower()
    if action == "inventory":
        list_inventory()
    elif action == "room":
        list_store_items()
    elif action.startswith("pickup "):
        take_item(action[7:].strip())
    elif action.startswith("drop "):
        remove_item(action[5:].strip())
    elif action.startswith("use "):
        consume_item(action[4:].strip())
    elif action.startswith("examine "):
        inspect_item(action[8:].strip())
    elif action.startswith("go "):
        switch_section(action[3:].strip())
    elif action == "leave":
        confirm = input("🧾 Ready to pay and leave? (yes/no): ").strip().lower()
        if confirm == "yes":
            has_checked_out = True
            print("💳 Checkout complete! You may now use your items.")
        else:
            print("👍 Got it, take your time.")
    elif action == "help":
        show_help()
    elif action == "exit":
        print("\n👋 Thanks for visiting your local FitMart-Store!e Stay energized!")
        break
    else:
        print("❓ Unknown command. Try 'help' for options.")
