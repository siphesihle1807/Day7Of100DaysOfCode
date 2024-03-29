import random
from fruit_list import fruits 
from game_art import game, stages

print(game)
print("Let's play a hangman game.")
print("The catergory for this game is fruits.")
print("It's a bit hard. So have your thinking cap on.")

random_word = random.choice(fruits)
word_length = len(random_word)

end_game = False
lives = 6

# print(f"This is the chosen word {random_word}")

#This creates the blanks in the game.
hangman = []
for _ in range(word_length):
    hangman += "_"

while not end_game:
    user_guess = input("Guess a letter: ")
    user_guess = user_guess.lower()

    if user_guess in hangman:
        print(f"Ooops, you've already guessed {user_guess}")

    for i in range(word_length):
        char =random_word[i]

        if char == user_guess:
            hangman[i] = char

    if user_guess not in random_word:
        print(f"You guessed {user_guess}, which is incorrect.\nOoops, you lose a life.")
        lives -= 1
        print("You have {lives} lives left.")
        if lives == 0:
            end_game = True
            print("You are out of lives. You lose.")


    print(f"{' '.join(hangman)}")
    if "_" not in hangman:
        end_game = True
        print("You completed the game. You win.")

    print(stages[lives])