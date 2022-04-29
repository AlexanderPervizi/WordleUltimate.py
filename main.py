from Game_Logic import Game  # For importing the game logic of Wordle Ultimate
from User_Input import Input  # For importing the introduction of Worlde Ultimate


def main():
    intro = Input()  # Sets word 'intro' as the class for user input
    intro.introduction()  # Reads the introduction to user from static method
    intro.params()  # Asks user for game parameters
    game = Game(intro)  # Sends game parameters to the game logic class to be used throughout
    game.load_dictionary()  # Loads dictionary here such that main() knows target word

    while game.won is False:  # Loops across each guess iteration
        valid_guess = False  # Initializes variable for valid guess
        while valid_guess is False:  # For looping across guesses
            attempt_raw = input(f'Enter guess number {game.guess_num}:\n')  # Displays guess # to user, asks for input
            attempt = attempt_raw.lower().strip()  # Takes guessed word and lower cases each letters and strips spaces
            valid_guess = game.guess(attempt)  # Checks whether valid guess triggers win condition, returns boolean val
        if game.check_lost():  # Condition for when user loses
            print('You Lost!')
            print('Target word is:', game.target)  # Displays target word and breaks from loop
            break


if __name__ == "__main__":
    main()
