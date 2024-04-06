import random

# Function to load words from file
def load_words(filename):
    with open(filename, 'r') as file:
        words = [line.strip().lower() for line in file]
    return words

# Function to provide feedback on the guess
def provide_feedback(guess, target):
    feedback = ['-' for _ in range(len(guess))]  # Start with all dashes
    guess_used = [False for _ in range(len(guess))]  # Track used letters in guess
    target_used = [False for _ in range(len(target))]  # Track used letters in target

    # First pass for correct letters in correct positions
    for i in range(len(guess)):
        if guess[i] == target[i]:
            feedback[i] = target[i].upper()  # Uppercase for correct position
            guess_used[i] = True
            target_used[i] = True

    # Second pass for correct letters in wrong positions
    for i in range(len(guess)):
        if not guess_used[i]:
            for j in range(len(target)):
                if not target_used[j] and guess[i] == target[j]:
                    feedback[i] = target[j]  # Lowercase for correct letter, wrong position
                    guess_used[i] = True
                    target_used[j] = True
                    break

    return ' '.join(feedback)

def play_wordle(filename):
    words = load_words(filename)
    target_word = random.choice(words)
    attempts = 6

    print("Welcome to Wordle!")
    print(f"You have {attempts} attempts to guess the right word.")

    while attempts > 0:
        guess = input("Enter your guess: ").lower().strip()
        if len(guess) != len(target_word):
            print("Invalid word length. Please try again.")
            continue
        if guess not in words:
            print("Word not in list. Please try again.")
            continue

        attempts -= 1

        feedback = provide_feedback(guess, target_word)
        print(feedback)

        if guess == target_word:
            print("Congratulations! You've guessed the word correctly.")
            break

        if attempts == 0:
            print("Sorry, you've run out of attempts. The correct word was:", target_word)

if __name__ == "__main__":
    play_wordle("valid-wordle-words.txt")
