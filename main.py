import json

# Initialize the inventory
inventory = {}

FILENAME = "inventory_data.json"

# Load and Save Functions

def load_inventory_from_file():
    """Load  data from a JSON file."""
    try:
        with open(FILENAME, "r") as file:
            global inventory
            inventory = json.load(file)
            print("Inventory loaded successfully!")
    except FileNotFoundError:
        print("No inventory file found.")
    except json.JSONDecodeError:
        print("File found .")

def save_inventory_to_file():
    """Save inventory data to a JSON file."""
    with open(FILENAME, "w") as file:
        json.dump(inventory, file, indent=4)
    print("\nInventory saved successfully!")


def add_item():
    """Add a new item """
    item_id = input("Enter item ID: ")
    if item_id in inventory:
        print("Item already exists")
        return
    name = input("Enter item name: ")
    description = input("Enter item description: ")
    quantity = int(input("Enter quantity: "))
    retail_price = int(input("Enter retail price per unit: "))
    wholesale_price = int(input("Enter wholesale price per unit: "))

    inventory[item_id] = {
        "name": name,
        "description": description,
        "quantity": quantity,
        "retail_price": retail_price,
        "wholesale_price": wholesale_price,
    }
    print(f"Item '{name}' added successfully!")
    save_inventory_to_file()  # Save after adding

def update_item():
    """Update details of an existing item."""
    item_id = input("Enter item ID to update: ")
    if item_id not in inventory:
        print("Item not found.")
        return

    print(f"Updating item '{inventory[item_id]['name']}'")
    description = input("Enter new description: ") or inventory[item_id]["description"]
    quantity = int(input("Enter new quantity: "))
    retail_price = float(input("Enter new retail price per unit: "))
    wholesale_price = float(input("Enter new wholesale price per unit: "))

    # Update the item with new data
    inventory[item_id].update({
        "description": description,
        "quantity": quantity,
        "retail_price": retail_price,
        "wholesale_price": wholesale_price,
    })
    print("Item updated successfully!")
    save_inventory_to_file()  # Save after updating

def delete_item():
    """Delete an item from the inventory."""
    item_id = input("Enter item ID to delete: ")
    if item_id in inventory:
        del inventory[item_id]
        print("Item deleted successfully!")
        save_inventory_to_file()  # Save after deleting
    else:
        print("Item not found.")

def view_inventory():
    """Display all items in the inventory."""
    if not inventory:
        print("Inventory is empty.")
        return

    print("\nCurrent Inventory:")
    print("ID\tName\tQuantity\tRetail Price\tWholesale Price\tSupplier\tDescription")
    print("-" * 80)
    for item_id, details in inventory.items():
        print(f"{item_id}\t{details['name']}\t{details['quantity']}\t{details['retail_price']}\t{details['wholesale_price']}\t{details['description']}")
    print("-" * 80)

# Step 4: Main loop to interact with the inventory system

def main():
    load_inventory_from_file()  # Load data on startup

    while True:
        print("\nInventory Management System")
        print("1. Add item")
        print("2. Update item")
        print("3. Delete item")
        print("4. View inventory")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_item()
        elif choice == "2":
            update_item()
        elif choice == "3":
            delete_item()
        elif choice == "4":
            view_inventory()
        elif choice == "5":
            print("Exiting the program.")
            save_inventory_to_file()  # Save on exit
            break
        else:
            print("Invalid choice. Please try again.")

# Run the main program loop
main()
