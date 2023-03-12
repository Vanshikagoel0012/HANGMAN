import random

# List of words to choose from
words_list = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon"]

# Select a random word from the list
selected_word = random.choice(words_list)

# Create a list to store the letters guessed by the player
guesses = []

# Create a variable to store the number of attempts left
attempts_left = 6

# Create a variable to store the current state of the game
game_state = ""

# Loop until the player runs out of attempts or guesses the word
while attempts_left > 0:
    # Display the current state of the game
    print("Attempts left:", attempts_left)
    print("Word:", game_state)

    # Prompt the player to guess a letter
    guess = input("Guess a letter: ")

    # Check if the letter has already been guessed
    if guess in guesses:
        print("You've already guessed that letter!")
    else:
        # Add the letter to the list of guesses
        guesses.append(guess)

        # Check if the letter is in the selected word
        if guess in selected_word:
            print("Correct!")
            # Update the game state with the guessed letter
            for i in range(len(selected_word)):
                if selected_word[i] == guess:
                    game_state += guess
                else:
                    game_state += "-"
        else:
            print("Incorrect!")
            # Decrement the number of attempts left
            attempts_left -= 1

    # Check if the player has won
    if game_state == selected_word:
        print("Congratulations, you've won!")
        break

# If the player has run out of attempts, end the game
if attempts_left == 0:
    print("Sorry, you've run out of attempts. The word was", selected_word)
