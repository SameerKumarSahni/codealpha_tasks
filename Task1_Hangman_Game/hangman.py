import random

words = ["python", "computer", "program", "coding", "developer"]

word = random.choice(words)

guessed_letters = []
incorrect_guesses = 0

print("===== HANGMAN GAME =====")

while incorrect_guesses < 6:

    display = ""

    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"

    print("\nWord:", display)
    print("Incorrect guesses:", incorrect_guesses, "/ 6")

    if "_" not in display:
        print("Congratulations! You won!")
        break

    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Correct guess!")
    else:
        incorrect_guesses += 1
        print("Wrong guess!")

else:
    print("\nGame Over!")
    print("The word was:", word)
