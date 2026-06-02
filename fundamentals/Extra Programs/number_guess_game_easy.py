import random

secret_number = random.randint(1, 20)

guess = int(input("Guess the number (1-20): "))

if guess == secret_number:
    print("🎉 Correct!")

else:
    print("❌ Wrong!")
    print("The correct number was:", secret_number)
