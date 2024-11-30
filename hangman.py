import random

# List of predefined words
word_list = ["python", "hangman", "programming", "openai", "computer", "science"]

def choose_word():
    return random.choice(word_list)

def display_word(word, guessed_letters):
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])

def hangman():
    word = choose_word()
    guessed_letters = set()
    attempts = 6  # Number of allowed wrong guesses

    print("Welcome to Hangman!")
    print("Try to guess the word, letter by letter.")

    while attempts > 0:
        # Display the current state of the word
        current_display = display_word(word, guessed_letters)
        print(f"\nWord: {current_display}")
        print(f"Attempts remaining: {attempts}")
        print(f"Guessed letters: {' '.join(sorted(guessed_letters))}")

        # User guesses a letter
        guess = input("Guess a letter: ").lower().strip()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue
        
        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print("Good guess!")
        else:
            print("Incorrect guess.")
            attempts -= 1

        # Check if the player has guessed the word
        if set(word).issubset(guessed_letters):
            print(f"\nCongratulations! You guessed the word: {word}")
            break
    else:
        print(f"\nGame Over! The word was: {word}")

    # Prompt to restart the game
    restart = input("\nDo you want to play again? (yes/no): ").lower().strip()
    if restart == "yes":
        hangman()
    else:
        print("Thanks for playing Hangman!")

# Run the game
hangman()
