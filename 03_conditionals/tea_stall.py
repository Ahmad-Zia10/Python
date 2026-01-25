tea_cup_size = input("Choose your cup size(small/medium/large) :").lower()

if tea_cup_size == "large":
    print("Your Bill is 20 rupees")
elif tea_cup_size == 'medium':
    print("Your Bill is 15 rupees")
elif tea_cup_size == 'small':
    print("Your Bill is 10 rupees")
else:
    print("Unknown Cup size!!")