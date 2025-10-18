import random

def welcome ():
    print ("Hello and welcome to the Number Guessing Game!")
    print ("You should try numbers between 1 to 100 to userNumber the secret secretNumber")
    print("the computer will tell you if its bigger or smaller")
         
welcome()

secretNumber = random.randint(1,100)

print("Choose the difficult:")
print("1 - Easy (10 trys)")
print("2 - Medium (5 trys)")
print("3 - Hard (3 trys)")

level =input("Choose 1, 2 or 3 ")

if level == "1":
    trys = 10
elif level == "2":
    trys = 5
elif level == "3":
    trys = 3
else:
    print("Not a valid option, will have 7 tries")
    trys = 8
    
print(f"\n You choose {trys} trys to userNumber the secretNumber.\n")

# This is the Game loop
def gameLoop():
    for intento in range(1, trys + 1):
        userNumber = int(input(f"Try {intento}: Guess a number between 1 & 100 → "))
        
        if userNumber == secretNumber:
            print(f"🎉 ¡Congrats! You guessed the number in {intento} tries.")
            break
        elif userNumber < secretNumber:
            print("The secret secretNumber is bigger.\n")
        else:
            print("The secret secretNumber is smaller.\n")

        if intento == trys:
            print(f"😢 You have no more trys. The secret secretNumber was {secretNumber}.")
            
gameLoop()
