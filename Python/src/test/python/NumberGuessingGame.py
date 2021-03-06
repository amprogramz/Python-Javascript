'''
Alec McDaugale
This is a basic number guessing game i created for fun. There is a class to get the max num, create a random num, and
check if you can guess the num. The game is in a never ending loop that allows you to select a max number, then it loops
the game until you get the number right. Now you may select another max num and play as much as you want.
'''
import random


class NumberGame:
    def __init__(self, maxnum):
        self._maxnum = maxnum
        self._ranomnum = random.randint(0, self._maxnum)

    def set_maxnum(self, maxnum):
        self._maxnum = maxnum

    def get_maxnum(self):
        return self._maxnum

    def set_randomnum(self):
        self._ranomnum = random.randint(0, self._maxnum)

    def get_randomnum(self):
        return self._maxnum

    def compare_num(self, num):
        if num == self._ranomnum:
            print("Congratulations, you guessed the number.")
            return True
        elif num < 0 or num > self._maxnum:
            print("Guess a number between 0 and", self._maxnum)
            return False
        elif num < self._ranomnum:
            print("Number is too low, guess again.")
            return False
        else:
            print("number is too hi, guess again.")
            return False


while True:
    num = NumberGame(int(input("Enter a max number:")))
    correct = False

    while correct is False:
        correct = num.compare_num(int(input("Guess a number:")))




