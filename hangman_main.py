import os
import random

def clear():
    """Clear the console screen."""
    # Check if the OS is Windows or not
    if os.name == 'nt':
        os.system('cls')  # Clear screen on Windows
    else:
        os.system('clear')  # Clear screen on Linux/Unix/Mac

def main():
    
    from hangman_words import word_list
    from hangman_art import logo, stages
    
    generate = random.choice(word_list)
    word_lth = len(generate)
    lives = 6

    print(logo)

    # First and last letter given
    display = ['_'] * word_lth
    display[0] = generate[0]
    display[-1] = generate[-1]

    print(' '.join(display))

    end_game = False

    while not end_game:
        guess = input("Guess a letter: ").lower()
        clear()

        if guess in display:
            print(f"You've already guessed {guess}")

        for position in range(word_lth):
            letter = generate[position]
            if letter == guess:
                display[position] = letter

        if guess not in generate:
            print(f"You guessed {guess}, that is not in the word, you lose a life!")
            lives -= 1

            if lives == 0:
                end_game = True
                print(f"You lose! The word was {generate}")

        print(' '.join(display))

        if "_" not in display:
            end_game = True
            print("You win!")

        print(stages[lives])

if __name__ == '__main__':
    main()
