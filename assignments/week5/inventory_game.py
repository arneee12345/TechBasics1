# --- Game State ---
MAX_INVENTORY_SIZE = 5
checked_out = False
current_section = "supplements"

inventory = [
    {"name": "Water Bottle", "type": "tool", "uses": 2, "permanent": True},
    {"name": "Energy Bar", "type": "food", "uses": 1}
]

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

# --- Functions ---

def show_inventory():
    print("\n🎒 Your Inventory:")
    if not inventory:
        print("(empty)")
    else:
        for item in inventory:
            print(f"- {item['name']} (Type: {item['type']}, Uses: {item.get('uses', '∞')})")

def show_room_items():
    print(f"\n🛒 You are in the '{current_section}' section. Items here:")
    for item in store[current_section]:
        print(f"- {item['name']} (Type: {item['type']}, Uses: {item.get('uses', '∞')})")
    print("\nOther sections: " + ", ".join([key for key in store if key != current_section]))

def pick_up(item_name):
    global checked_out
    if checked_out:
        print("🚫 You can't pick up more items after checkout.")
        return
    if len(inventory) >= MAX_INVENTORY_SIZE:
        print("❌ Inventory full! Drop something first.")
        return
    for item in store[current_section]:
        if item["name"].lower() == item_name.lower():
            inventory.append(item)
            store[current_section].remove(item)
            print(f"✅ You picked up {item['name']}.")
            return
    print("❌ That item is not in this section.")

def drop(item_name):
    global checked_out
    if checked_out:
        print("🚫 You can't drop items after checkout.")
        return
    for item in inventory:
        if item["name"].lower() == item_name.lower():
            inventory.remove(item)
            store[current_section].append(item)
            print(f"🗑️ You dropped {item['name']} into this section.")
            return
    print("❌ You don't have that item.")

def use(item_name):
    if not checked_out:
        print("🚫 You must check out before using items.")
        return
    for item in inventory:
        if item["name"].lower() == item_name.lower():
            if item.get("uses", 0) > 1:
                item["uses"] -= 1
                print(f"⚡ Used {item['name']}. {item['uses']} uses left.")
            elif item.get("uses", 0) == 1:
                if item.get("permanent", False):
                    item["uses"] = 0
                    print(f"💧 {item['name']} is now empty but reusable.")
                else:
                    inventory.remove(item)
                    print(f"⚡ You used up {item['name']}.")
            else:
                print(f"🚫 {item['name']} is already empty.")
            return
    print("❌ That item is not in your inventory.")

def examine(item_name):
    all_items = inventory + store[current_section]
    for item in all_items:
        if item["name"].lower() == item_name.lower():
            print(f"🔍 {item['name']} is a {item['type']} item. Uses: {item.get('uses', '∞')}")
            return
    print("❌ Item not found here or in your bag.")

def change_section(new_section):
    global current_section, checked_out
    if checked_out:
        print("🚫 You already left the store. No more section changes.")
        return
    if new_section in store:
        current_section = new_section
        print(f"➡️ You moved to the '{current_section}' section.")
    else:
        print("❌ That section doesn't exist.")

# --- Game Loop ---

def game_loop():
    global checked_out
    print("🏪 Welcome to FitMart! Collect up to 5 items and check out!")
    print("Type 'help' to view commands.")

    while True:
        command = input("\n> ").strip().lower()
        if command == "help":
            print("Commands: inventory, look, pickup [item], drop [item], use [item], examine [item], go [section], leave, quit")
        elif command == "inventory":
            show_inventory()
        elif command == "look":
            show_room_items()
        elif command.startswith("pickup "):
            pick_up(command[7:].strip())
        elif command.startswith("drop "):
            drop(command[5:].strip())
        elif command.startswith("use "):
            use(command[4:].strip())
        elif command.startswith("examine "):
            examine(command[8:].strip())
        elif command.startswith("go "):
            change_section(command[3:].strip())
        elif command == "leave":
            confirm = input("💳 Ready to pay and leave? (yes/no): ").strip().lower()
            if confirm == "yes":
                checked_out = True
                print("✅ You checked out. You may now use your items.")
            else:
                print("🕓 Still browsing? No problem.")
        elif command == "quit":
            print("👋 Thanks for visiting FitMart!")
            break
        else:
            print("❓ Unknown command. Try 'help'.")

# Run the game
if __name__ == "__main__":
    game_loop()

