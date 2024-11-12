import random

comp_choice = random.randint(1, 100)

while True:
    try:
        user_input = int(input("Guess the number between 1 and 100: "))
        if (1 < user_input < 100) and (user_input > comp_choice):
            print("Too high!")
        elif (1 < user_input < 100) and (user_input < comp_choice):
            print("Too low!")
        elif user_input == comp_choice:
            print(f"Congratulations! You guessed the number: {comp_choice}")
            break
        else:
            print("Invalid input. Out of range.")
    except ValueError:
        print("Invalid input. Please enter a whole number.")