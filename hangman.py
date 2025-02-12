import random

def choose_word():
    words = ["pineapples", "banana", "cherry", "mangoes", "peach", "grapes"]
    return random.choice(words)

def display_word(word, guessed_letters):
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])

def hangman():
    print("Welcome to Hangman! Guess the word letter by letter.")
    
    word_to_guess = choose_word()
    guessed_letters = set()
    attempts = 6

    while attempts > 0:
        print("\nWord: ", display_word(word_to_guess, guessed_letters))
        print(f"Attempts remaining: {attempts}")
        print(f"Guessed letters: {', '.join(sorted(guessed_letters))}")

        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue

        guessed_letters.add(guess)

        if guess in word_to_guess:
            print("Good guess!")
            if all(letter in guessed_letters for letter in word_to_guess):
                print(f"\nCongratulations! You've guessed the word: {word_to_guess}")
                break
        else:
            print("Wrong guess.")
            attempts -= 1

    if attempts == 0:
        print(f"\nGame over! The word was: {word_to_guess}")

if __name__ == "__main__":
    hangman()
