print(" groks degenerate shopping cart v2 - now with prices ")
cart = [] # each item will be a dictionary → {"name": "weed", "price": 60.00}
while True:
    item_name = input("item name (or done to checkout): ").strip()
    if item_name.lower() == "done":
        break
    if item_name == "":
        print("dont waste my time. ")
        continue
    # avoid duplicates
    if any(item["name"].lower() == item_name.lower() for item in cart):
        print(f"you already have {item_name} in the cart bro")
        continue
    # get price 
    while True:
        price_input = input(f"price for {item_name} (in $): ").strip()
        try:
            price= float(price_input)
            if price < 0:
                print("price cant be negative pablo")
                continue
            break
        except:
            print("type a real number")
    # add to cart 
    cart.append({"name": item_name, "price": price})
    print(f"{item_name} - ${price:.2f} added\n")
# checkout time 
print("\n" + "="*50)
print("final receipt - you degenerate ")
print("="*50)

if not cart:
    print("cart empty. you bought nothing. congrats. ")
else: 
    cart.sort(key=lambda x: x["name"].lower()) # sort alphabetically by name 
    total = 0
    for i, item in enumerate(cart, 1):
        print(f"{i:2}. {item['name'].upper():<20} ${item['price']:>8.2f}")
        total += item['price']
    
    tax = total * 0.08   # 8% tax
    grand_total = total + tax
    
    print("-" * 50)
    print(f"{'SUBTOTAL':<30} ${total:>8.2f}")
    print(f"{'TAX (8%)':<30} ${tax:>8.2f}")
    print(f"{'GRAND TOTAL':<30} ${grand_total:>8.2f}")
    print("="*50)
    print("Now go touch grass… or smoke it.")