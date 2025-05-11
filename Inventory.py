# Inventory Tracker for a Small Shop

inventory = {}

def add_item():
    item = input("Enter item name: ").capitalize()
    if item in inventory:
        print("🔄 Item already exists. Use 'Update' to change quantity.")
    else:
        try:
            quantity = int(input(f"Enter quantity for {item}: "))
            price = float(input(f"Enter price per unit for {item}: ₹"))
            inventory[item] = {'quantity': quantity, 'price': price}
            print(f"✅ {item} added to inventory.")
        except ValueError:
            print("⚠️ Please enter valid numeric values for quantity and price.")

def update_item():
    item = input("Enter item name to update: ").capitalize()
    if item in inventory:
        try:
            new_quantity = int(input("Enter new quantity: "))
            new_price = float(input("Enter new price: ₹"))
            inventory[item]['quantity'] = new_quantity
            inventory[item]['price'] = new_price
            print(f"🔁 {item} updated.")
        except ValueError:
            print("⚠️ Please enter valid numeric values.")
    else:
        print("❌ Item not found.")

def remove_item():
    item = input("Enter item name to remove: ").capitalize()
    if item in inventory:
        del inventory[item]
        print(f"🗑️ {item} removed from inventory.")
    else:
        print("❌ Item not found.")

def view_inventory():
    if not inventory:
        print("📭 Inventory is empty.")
    else:
        print("\n📦 Current Inventory:")
        print("Item\t\tQuantity\tPrice per Unit")
        print("------------------------------------------------")
        for item, details in inventory.items():
            print(f"{item}\t\t{details['quantity']}\t\t₹{details['price']}")
        print("------------------------------------------------")

def inventory_menu():
    print("📦 Welcome to Small Shop Inventory Tracker")
    while True:
        print("\nMenu:")
        print("1. Add Item ➕")
        print("2. Update Item ✏️")
        print("3. Remove Item 🗑️")
        print("4. View Inventory 📄")
        print("5. Exit 🚪")

        choice = input("Enter your choice (1-5): ")
        if choice == '1':
            add_item()
        elif choice == '2':
            update_item()
        elif choice == '3':
            remove_item()
        elif choice == '4':
            view_inventory()
        elif choice == '5':
            print("👋 Exiting... Have a great day!")
            break
        else:
            print("⚠️ Invalid choice. Please select from 1 to 5.")

if __name__ == "__main__":
    inventory_menu()
