import pynput.keyboard as kb
from random_word import RandomWords
from time import sleep
import random
import string

keyboard = kb.Controller()

def startInput():
	number = input('How many searchs would you like to run: ')
	return number

def keyPress(input):
    for i in input:
        keyboard.press(i)
        keyboard.release(i)
def enter():
    sleep(1)
    keyboard.press(kb.Key.enter)
    keyboard.release(kb.Key.enter)

def launchHOME():
    keyboard.press(kb.Key.cmd)
    keyboard.press('s')
    sleep(1)
    keyboard.release('s')
    keyboard.release(kb.Key.cmd)

def closeTab():
	keyboard.press(kb.Key.ctrl)
	keyboard.press('w')
	sleep(1)
	keyboard.release('w')
	keyboard.release(kb.Key.ctrl)

def search(amount):
	count = 0
	while count < amount:
		count += 1
		foo = RandomWords()
		foo2 = foo.get_random_word()
		launchHOME()
		keyPress(str(foo2))
		sleep(1)
		enter()
		sleep(random.randint(3,21))
		closeTab()

def main():
	numberOfRuns = int(startInput())
	search(numberOfRuns)
	launchHOME()
	keyPress('https://account.microsoft.com/rewards/')
	enter()

main()