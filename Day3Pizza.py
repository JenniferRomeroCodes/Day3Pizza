print("Welcome")
size = input("What size pizza? S M L?")
pepperoni = input("Do you want pepperoni on your pizza? Y or N")
extra_cheese = input("Do you want extra cheese? Y or N?")
#how much based on size choice
bill = 0 
if size == "S":
    bill += 15
if size == "M":
    bill += 20
elif size == "L":
    bill += 25
else:
    print("You typed the wrong inputs.")
# how much based on pepperoni choice
if pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3
#extra cheese
if extra_cheese == "Y":
    if extra_cheese == "Y":
        bill += 1
 
print(f"Your final bill is: ${bill}.")

    