import random

def guessing_game():
    secret_number = random.randint(1, 100)
    max = 5
    for i in range(max):
        guess = int(input(f"Guess the secret number (between 1 and 100): "))
        
        if guess < secret_number:
            print("Too low!")
        elif guess > secret_number:
            print("Too high!")
        else:
            print("Success!")
            break
    else:
        print("Failed!")

guessing_game()

#2. Coin Toss Challenge
print("--------------------------------------------------------------------------------------------------------------------------------------------")

def coin_toss_game():
    while True:
        user_choice = input("Do you want to toss a coin? (y/n): ").lower()
        
        if user_choice != 'y':
            break
        
        outcome = random.choice(["Heads", "Tails"])
        print(f"The coin landed on: {outcome}")

coin_toss_game()