import random
'''
1 for snake 🐍
-1 for water💧
0 for gun 🔫

'''
computer = random.choice([-1, 0, 1])

youDict = {"s": 1, "w": -1, "g": 0}
reverseDict = {1 : "Snake 🐍", -1 : "Water 💧", 0 : "Gun 🔫"}
youstr = input("Enter your choice (s for Snake 🐍, w for Water 💧, g for Gun 🔫): ").lower()
if youstr not in youDict:
    print("❌ Invalid input! Please enter 's', 'w', or 'g'.")
    exit()

you = youDict[youstr]

# By now we havew 2 numbers (variables), you and computer 

# Game rules:
# 🐍 drinks 💧 → 🐍 wins
# 🔫 kills 🐍 → 🔫 wins
# 💧 damages 🔫 → 💧 wins


print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")

if(computer == you):
    print("It's a draw 🤝")
else:
    if(computer == -1 and you == -1):
        print("You Win! 🎉")

    elif(computer == -1 and you == 0):
        print("You Lose! 😢")   

    elif(computer == 1 and you == -1):
        print("You Lose! 😢")

    elif(computer == 1 and you == 0):
        print("You Win!🎉")

    elif(computer == 0 and you == -1):
        print("You Win!🎉")

    elif(computer == 0 and you == 1):
        print("You Lose! 😢")

    else:
        print("Something went wrong 🥴")

