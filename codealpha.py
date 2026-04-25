import random


words = ["apple", "tiger", "chair", "robot", "ocean"]


word = random.choice(words)
guessed_letters = []
incorrect_guesses = 0
max_attempts = 6


display = ["_"] * len(word)

print("🎮 Welcome to Hangman!")
print("Guess the word, one letter at a time.")
print("You have 6 incorrect guesses allowed.\n")


while incorrect_guesses < max_attempts and "_" in display:
    print("Word:", " ".join(display))
    guess = input("Enter a letter: ").lower()

   
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single valid letter.\n")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.\n")
        continue

    guessed_letters.append(guess)

    
    if guess in word:
        print("Correct!\n")
        for i in range(len(word)):
            if word[i] == guess:
                display[i] = guess
    else:
        incorrect_guesses += 1
        print(f"Wrong! Attempts left: {max_attempts - incorrect_guesses}\n")


if "_" not in display:
    print("🎉 You won! The word was:", word)
else:
    print("💀 You lost! The word was:", word)
