print("=== TIP CALCULATOR 2026 ===")

bill = float(input("Total bill amount? $"))
tip_percent = int(input("Tip %? (10, 12, 15, 20): "))
people = int(input("Split between how many people? "))

tip_amount = bill * (tip_percent / 100)
total = bill + tip_amount
per_person = total / people

print(f"Each person pays: ${per_person:.2f}")
print(f"Total with tip: ${total:.2f} | Tip amount: ${tip_amount:.2f}")