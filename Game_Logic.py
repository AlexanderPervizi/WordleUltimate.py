import random  # Uses random library for randomizing word from language dictionary (set)
from colorama import Fore, Style  # Uses colorama library for color display in python command console
from User_Input import Input  # Imports user input from the Input class for game parameters


class Game(Input):
    """
    Represents the logic of Wordle Ultimate, and overall display of output to user
    Inherits 'Input' from User_Input class which is representative of user decided parameters for the game
    """
    def __init__(self, input_class):
        """Initialized object state and attributes that change concerning user input"""
        self.won = False  # Sets 'won' to false which is the condition for looping across guesses
        self.lost = False  # Sets 'lost' to false which is used in counting the number of user guesses
        self.guess_num = 1  # Guess number is 1 which is used for display and as base value
        self.target = None  # Open container for target word to be taken from dic
        self.words = None  # Open container for all words in dic chosen by user
        # Below are the alphabets for spanish and english to be used depending on user choice
        self.remain_let_eng = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
                               's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        self.remain_let_esp = ['a', 'á', 'b', 'c', 'd', 'e', 'ê', 'f', 'g', 'h', 'i', 'í', 'j', 'k', 'l', 'm', 'n', 'ñ',
                               'o', 'ó', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        self.remain_let = []  # Appends with current alphabet altered on each iteration of guesses
        self.all_guesses = []  # List of all user guesses to be displayed
        super().__init__()  # Extends __init__ class for user input
        self.num_guess = input_class.guess_num2  # Number of guesses indicated by user
        self.dic_choice = input_class.choice_dic  # Language choice indicated by user
        self.num_chars = input_class.chars_num  # Word length indicated by user

    def load_dictionary(self):
        """
        Loads the necessary language dictionary into empty set and iterates over all words in set to set a
        randomized target word for user to guess
        """
        dic = set()  # Creates an open set for adding all words from language .txt file (unordered for efficiency)
        if self.dic_choice == 1:  # Condition for when user chooses english
            with open('english.txt', 'r') as f:  # Opens and reads from specified .txt file
                self.words = f.readlines()   # Adds all words from .txt file to open container
        elif self.dic_choice == 2:  # Condition for when user chooses spanish, same process applies
            with open('espanol.txt', 'r') as f:
                self.words = f.readlines()
        for i in self.words:  # Iterates over full list retrieved from language .txt file
            if self.num_chars + 1 is len(i):  # Adds all words of specified length to set
                dic.add(i)
        self.target = random.choice(tuple(dic)).strip()  # Random word (more efficient than taking first index of set)

    def guess(self, word):
        """Method for taking user guess (word) and determining whether word results in a win, loss or another guess"""
        if self.valid_guess(word):  # Checks whether word is valid guess (calls method)
            self.split_and_check(word)  # Checks word accuracy and displays to user
            if word == self.target:  # Condition for when user guesses the target word (win)
                self.won = True    # Sets 'won' to true, loop breaks
                print('You WIN!')
            else:  # Condition for when user does not win
                self.guess_num += 1  # Increases win counter (initially 1)
                if not self.check_lost():  # Checks whether user loses, displays 'try again' if not
                    print('\nTry again')

    def split_and_check(self, word):
        """
        Splits the given word into characters and manipulates each character based on accuracy with target word
        Displays accuracy to user using the colorama library, and displays a list of the words remaining
        """
        # Chooses which alphabet to use based on user input of language choice
        if self.dic_choice == 1:  # For english
            self.remain_let = self.remain_let_eng  # Appends english alphabet
        elif self.dic_choice == 2:  # For spanish
            self.remain_let = self.remain_let_esp  # Appends spanish alphabet

        letters = list(word)  # Creates a list of the letters of the word guessed by user
        guessed_word = []  # Creates an empty list for all guessed words from user
        for i in range(len(letters)):  # Iterates over length of characters in word
            if letters[i] in self.target and letters[i] == self.target[i]:  # Param for guessed letter = target letter
                guessed_word.append(Fore.GREEN + letters[i] + Style.RESET_ALL)  # Outputs green letter and appends
            elif letters[i] in self.target:  # Param for when guessed letter is in target word
                guessed_word.append(Fore.YELLOW + letters[i] + Style.RESET_ALL)  # Outputs yellow letter and appends
            else:  # Param for when letter is not in word
                guessed_word.append(Style.RESET_ALL + letters[i])  # Appends letter with gray color
                try:  # Uses try to void exceptions
                    self.remain_let.remove(letters[i])  # Removes uncolored letters from alphabet list
                except ValueError:  # Exception for when letter is already removed from alphabet list
                    continue
        self.all_guesses.append(guessed_word)  # Takes list of all letters in guessed word and appends it to total list

        print('')
        print((len(guessed_word) + 4) * '=')
        for i in self.all_guesses:  # Iterates over all words in our guessed words total list
            print('|', ''.join(i), '|')  # Displays them neatly
        print((len(guessed_word) + 4) * '=')
        print('Remaining Possible Letters: \n', self.remain_let)  # Displays remaining letters to user

    def valid_guess(self, guess):
        """Determines whether user guess is in dictionary, making it a valid guess"""
        if self.dic_choice == 1:  # For english dictionary
            file = open('english.txt')  # Opens english dictionary .txt document
            if len(guess) == len(self.target) and guess in file.read():  # Checks that length of guess = length target
                return True  # Returns true which allows user to continue
            else:  # Condition for when lengths do not equal
                print('Guess invalid, please guess again:')  # Asks user to guess a valid word

        # Same process as above, but for spanish dictionary
        elif self.dic_choice == 2:
            file = open('espanol.txt')
            if len(guess) == len(self.target) and guess in file.read():
                return True
            else:
                print('Guess invalid, please guess again:')

    def check_lost(self):
        """Checks for a loss which ends looping"""
        if self.guess_num > self.num_guess:  # When the amount of guesses is higher than the guess limit, user loses
            self.lost = True  # True is returned, user losses
        return self.lost  # If not, we return false again
