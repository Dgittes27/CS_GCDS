print("Your alarm went off")
while True:
    sleep = input("Do you want to go back to sleep?")
    if sleep == "yes":
        print("SNOOZE")
    elif sleep == "no":
        break
    else:
        print("Please answer with yes or no")
while True: 
    hungry = input("Are you hungry?")
    if hungry == "yes":
        print("Eat a Banana")
    elif hungry == "no":
        break
    else: 
        print("Please answer with yes or no")

while True:
    shower = input("Did you shower last night?")
    if shower == "yes":
        print("Make your bed")
        break
    elif shower == "no":
        print("SHOWER")
        print("Make your bed")
        break
    else: 
        print("Please answer with yes or no")
print("Brush your teeth")
while True:
    cold = input("Is it cold outside?")
    if cold == "yes":
        print("Put on a shirt and a hoodie")
        break
    elif cold == "no":
        print("Put on a shirt")
        break
    else:
        print("Please answer with yes or no")
while True:
    gas = input("Does your car have gas?")
    if gas == "yes":
        print("Drive to work")
        break
    elif gas == ("no"):
        print("Walk to work")
        break
    else:
        print("Please answer with yes or no")
