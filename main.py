import random

# low , high value for numbers range
try:
    a, b = map(int, input("Enter the beginning and end of the range with a space: ").split())
except:
    print("Please enter a valid number.")

#generate the integer number between a and b
x = random.randint(a, b)

for i in range(5):
    try:
        guess = int(input("Guess the generated number: "))
        if guess < x:
            print("The generated number is bigger than you guessed.")
        elif guess > x:
            print("The generated number is smaller than you guessed.")
        else:
            print("Congratulations! Your guess is correct.")
            break
    except:
        print("Please enter a valid number.")
