
import random


# User Selection 

d = {
    "s": "Snake",
    "a": "Water",
    "d": "Gun"
}

print(d)

c = input("Select your choice: ")

if c == "s" or c == "a" or c == "d":
    u = print(f"Your choice is: {d[c]}")
else:
    print("Invalid")


#Computer Selection 

l1 = ["Snake", "Water", "Gun"]

p = random.choice(l1)

print("The bot choice:", p)


# Condition Checking 

# Snake
if c == "s" and p == "water":
    print("You won")
elif c == "s" and p == "Gun":
    print("Bot won")
elif c == "s" and p == "Snake":
    print("Tie")

# Water
elif c == "a" and p == "Gun":
    print("You won")
elif c == "a" and p == "Snake":
    print("Bot won")
elif c == "a" and p == "Water":
    print("Tie")

# Gun
elif c == "d" and p == "Snake":
    print("You won")
elif c == "d" and p == "Water":
    print("Bot won")
elif c == "d" and p == "Gun":
    print("Tie")