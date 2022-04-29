from colorama import Fore, Style  # Imports colorama library for color display of introduction
import pyfiglet  # Imports pyfiglet library to display of title screen


class Input:
    """
    Class for taking user input of game parameters to be used in game logic
    Displays introduction of our game to user and instructions on how to play
    """

    def __init__(self):
        """Initialized object state and attributes that change concerning user input"""
        self.guess_num2 = None  # Open container for the user's decision of guess numbers
        self.choice_dic = None  # Open container for the user's language choice (1 or 2)
        self.chars_num = None  # Open container for the user's choice of word length

    @staticmethod
    def introduction():
        """Static method for displaying introduction and instructions to user"""
        print('\033[1mWelcome to \033[0m')
        result = pyfiglet.figlet_format("WORDLE ULTIMATE!!", font="slant")
        print(result, end='')
        print('====================================================================================================='
              '==================')
        print('You are tasked with guessing the randomized word provided by the computer with the parameters that you '
              'will provide.')
        print('We provided an alphabet which will change on each iteration depending on letter availability.')
        # Uses colorama for display of what green and yellow letters will look like to user
        print(Fore.GREEN + 'GREEN' + Style.RESET_ALL, 'indicates that a letter of the word you guessed is in the'
                                                      ' same place as in the target word.')
        print(Fore.YELLOW + 'YELLOW' + Style.RESET_ALL, 'indicates that a letter of the word you guessed is in the '
                                                        'target word, but not necessarily in the same place.')
        print('GRAY indicates that the letter is not in the word and this letter will be removed from the alphabet '
              'provided')
        print('====================================================================================================='
              '==================\n')

    def params(self):
        """Asks for parameters of game from user to fill containers in __init__"""
        self.guess_num2 = int(input('How many guesses would you like? '))  # Asks for amount of guesses for user
        self.choice_dic = int(input('Please enter dictionary choice (1 for English | 2 for Spanish): '))  # Language
        self.chars_num = int(input('How long would you like the target word to be?: '))  # Asks for user word length
