print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
left_right = input("Left or Right?")
if left_right == "Right":
    print("Game Over.")
if left_right == "Left":
    swim_wait = input("Swim or wait?")
    if swim_wait == "Swim":
        print("Game Over.")
    if swim_wait == "Wait":
        which_door = input("Which door? Red Yellow Blue")
        if which_door == "Red" or which_door == "Blue":
            print("Game Over")
        if which_door == "Yellow":
               print("You win!")
        