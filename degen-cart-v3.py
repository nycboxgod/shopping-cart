import os
from datetime import datetime
print("DEGENERATE CART v3 – FINAL FORM")
print("commands: 'add items', 'list', 'delete 3', 'edit 2', 'done'\n")
cart = []
def show_cart():
    if not cart:
        print("cart is empty")
        return
    else:
        subtotal = sum(item["price"] for item in cart)
        print(f"\n{'#':>2} {'item':<20} {'price':>10}")
        print("-"*35)
        for i, item in enumerate(cart,1):
            print(f"{i:>2}. {item['name'].upper():<20} ${item['price']:>8.2f}")
        print("-"*35)
        print(f"{'subtotal':<25} ${subtotal:>8.2f}\n")
while True:
    command = input("what now? ").strip()
    if command.lower() == "done":
        break
    elif command.lower() == "list":
        show_cart()
        continue
    elif command.lower().startswith("delete "):
        try:
            idx = int(command.split()[1]) - 1
            if idx < 0 or idx >= len(cart):
                print("That item doesn't exist.")
            else:
                removed = cart.pop(idx)
                print(f"Removed {removed['name']} from cart.\n")
        except:
            print("Type 'delete 2' correctly.")
        continue
    elif command.lower().startswith("edit "):
        try:
            idx = int(command.split()[1]) - 1
            if idx < 0 or idx >= len(cart):
                print("That item doesn't exist.")
            else:
                item = cart[idx]
                new_price = float(input(f"New price for {item['name']} (was ${item['price']}): "))
                if new_price >= 0:
                    item["price"] = new_price
                    print(f"Updated {item['name']} → ${new_price:.2f}\n")
                else:
                    print("No negative prices, Escobar.")
        except:
            print("Type 'edit 2' correctly.")
        continue
    
    # If we get here, user is trying to add a normal item
    if command == "":
        print("Type something.")
        continue
    
    item_name = command
    
    # duplicate check
    if any(item["name"].lower() == item_name.lower() for item in cart):
        print("Already in cart, bro. Use 'edit' if you want to change price.")
        continue
    
    # get price with validation
    while True:
        try:
            price = float(input(f"Price for '{item_name}' → $"))
            if price >= 0:
                break
            print("Price can't be negative.")
        except:
            print("Type a real number.")
    
    cart.append({"name": item_name, "price": price})
    print(f"Added {item_name} – ${price:.2f}\n")

# ————— CHECKOUT —————
print("\n" + "═"*60)
print("FINAL RECEIPT – YOU ABSOLUTE DEGENERATE")
print("═"*60)

if not cart:
    print("You bought nothing. Minimalism king.")
else:
    cart.sort(key=lambda x: x["name"].lower())
    total = sum(item["price"] for item in cart)
    tax = total * 0.08875   # real California tax vibes
    grand_total = total + tax
    
    for i, item in enumerate(cart, 1):
        print(f"{i:>2}. {item['name'].upper():<25} ${item['price']:>8.2f}")
    
    print("—" * 60)
    print(f"{'SUBTOTAL':<40} ${total:>8.2f}")
    print(f"{'TAX (8.875%)':<40} ${tax:>8.2f}")
    print(f"{'GRAND TOTAL':<40} ${grand_total:>8.2f}")
    print("═"*60)

    # SAVE TO FILE
    filename = f"receipt_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt"
    desktop = os.path.join(os.path.expanduser("~"), "Desktop")
    filepath = os.path.join(desktop, filename)
    
    with open(filepath, "w") as f:
        f.write("DEGENERATE RECEIPT\n")
        f.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        for i, item in enumerate(cart, 1):
            f.write(f"{i:>2}. {item['name'].upper():<25} ${item['price']:>8.2f}\n")
        f.write("\n" + "—" * 60 + "\n")
        f.write(f"{'SUBTOTAL':<40} ${total:>8.2f}\n")
        f.write(f"{'TAX (8.875%)':<40} ${tax:>8.2f}\n")
        f.write(f"{'GRAND TOTAL':<40} ${grand_total:8.2f}\n")
    
    print(f"\nRECEIPT SAVED TO YOUR DESKTOP → {filename}")

print("\nNow go touch grass… or whatever’s in the cart.")                   