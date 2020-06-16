import pynput.keyboard as kb
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

def randomStringDigits(stringLength=6):
    lettersAndDigits = string.ascii_uppercase + string.digits
    return ''.join(random.choice(lettersAndDigits) for i in range(stringLength))

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

def launchEdge():
	keyPress("Microsoft Edge")
	enter()

def newTab():
    keyboard.press(kb.Key.ctrl)
    keyboard.press('t')
    sleep(1)
    keyboard.release('t')
    keyboard.release(kb.Key.ctrl)

def closeTab():
	keyboard.press(kb.Key.ctrl)
	keyboard.press('w')
	sleep(1)
	keyboard.release('w')
	keyboard.release(kb.Key.ctrl)

def searchInput(amount):
	count = 0
	while count < amount:
		count += 1
		foo = randomStringDigits(10)
		newTab()
		keyPress(str(foo))
		sleep(1)
		enter()
		sleep(3)
		closeTab()

def main():
	numberOfRuns = int(startInput())
	launchHOME()
	launchEdge()
	newTab()
	searchInput(numberOfRuns)
	newTab()
	keyPress('https://account.microsoft.com/rewards/')
	enter()

main()