# Guessing number game


import random
number = random.randint(1, 100)
print(number)
attepts = 0
print("Welcome to the Number Guessing Game!")

while True:
    guess = int(input("Enter your guess:"))
    attepts += 1
    if guess < number:
     print("Too Low! Try again.")
    elif guess > number:
        print("Too High! try again.")
    else:
        print(f"Congratulation you have guessed the number {number} in attempts {attepts}")
        break


    #Guesssing jumbled word

    import random
word_list = ["Python", "Javascript", "Java", "Automation", "Pytest", "Guvi", "Selenium"]
secret_word =random.choice(word_list).lower()
jumble = list(secret_word)x
random.shuffle(jumble)
jumble = ''.join(jumble)
while True:
    user_guess = input(f"Guess the jumbled word '{jumble}':").lower()
    if user_guess == secret_word:
        print("Congratulations! You guessed the word correctly.")
        break
    else:
        print("Sorry, that's not correct. Please try again.")
