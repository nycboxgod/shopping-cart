print("🛒 GROK'S UNHINGED SHOPPING LIST APP 🛒\n")
shopping_list = [] # empty list to start
while True:
    item = input("Add an item to the cart (or type done to finish): ").strip()
    if item.lower() == "done":
        print("\nCart locked. Time to checkout.\n")
        break
    if item == "":
        print("type something bro. ")
        continue
    if item in shopping_list:
        print(f"You already have '{item}' in the cart, genius.")
        continue
    shopping_list.append(item)
    print(f" added: '{item}'")
# after loop ends - show the results
print("="*40)
print("FINAL CART CONTENTS:")
print("="*40)
if len(shopping_list) == 0:
    print("Cart is empty. You're either fasting or broke.")
else:
    shopping_list.sort()                     # alphabetical order
    for number, item in enumerate(shopping_list, 1):   # enumerate gives us 1,2,3...
        print(f"{number}. {item.upper()}")

    print(f"\nTotal items: {len(shopping_list)}")
    print("Now go touch grass (or smoke it).")