print("Vampire Hunter 3000\n")

name = input("What is your name? ")
age = int(input("How old are you? "))
weight = int(input("How much do you weigh (in pounds)? "))

if name.lower() == "alice":
    print("Ahh Alice, the legendary slayer — welcome back!")
elif age < 16:
    print("You're too young — go home.")
elif weight < 120:
    print("You need to eat more and build strength.")
else:
    print(f"Welcome {name}, you're cleared to enter the forbidden lands.")

print("\nSuddenly the creatures attack!\n")

stakes = 3  # you start with 3 wooden stakes
vampires_killed = 0  # counter that goes up when you win
while stakes > 0:  # this loop keeps running as long as you have stakes left
    print(f"You have {stakes} stake(s) remaining.")
    action = input("Type 'stake' to kill a vampire or 'run' to escape: ").lower()
    if action == "stake":
        print("You drive the stake through its heart!")
        stakes -= 1  # same as stakes = stakes - 1
        vampires_killed += 1  # same as vampires_killed = vampires_killed + 1
    elif action == "run":
        print("You barely escape with your life.")
        break
    else:
        print("Invalid move — the enemy laughs at you.")
        # nothing happens — you waste a turn but keep the stake

# This part only runs AFTER the loop ends (either stakes == 0 or you ran away)
print("\nBattle over!")
print(f"Vampires killed: {vampires_killed}")

if vampires_killed >= 3:
    print("Absolute legend. The village throws you a party.")
elif vampires_killed >= 1:
    print("You survived… barely respectable.")
else:
    print("Zero kills. The village now uses you as bait.")
print("\nNew Years eve countdown starting in ... \n")
for seconds in range(20, 0, -1):
    print(f"{seconds} seconds until midnight! ")
print("happy motherfucking new new year !!!")
