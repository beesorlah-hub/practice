# import random no
import random
# promt
print("WELCOME TO THE GUESS NUMBER GAME ! ")
print("I have selected a random number between 1 and 10.")
#gen ran int
computer = random.randint(1, 10)
print(computer)
#test when true
while True:
    user = int(input("Guess a number: "))

    if user > computer:
        print("Too high! Try again.")

    elif user < computer :
        print("Too low! Try again.")

    else: 
        print(f"Congratulation! You guessed the correct number {user}")
        break


