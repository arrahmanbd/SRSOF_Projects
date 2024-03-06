# This is a Number Guessing Game....
'''
This program is created by:
    1. Jabir Hasan Sadan
    2. Nafiz Iqbal
    3. Abdullah Al Limon
    4. Shiddhartho Biswas
    5. Labib Sheikh
'''

import random
import time
import pyfiglet
def a(min,max):
    ran = random.randint(min,max)
    while True:
        user = int(input('\n\nGuess a number: '))
        print(pyfiglet.figlet_format("      Trying......", font = "slant"  ))
        time.sleep(2)
        if user == ran:
            print(pyfiglet.figlet_format("\nYou Won ! ! !", font = "slant"  ),'             👌👍👍😊😊😊😊')
            break
        else:
            print(pyfiglet.figlet_format("\nSorry ! Try again.....", font = "slant"  ),'                😒😒😒😒')
        
        time.sleep(2)

time.sleep(2)
min = int(input('Please enter minimum number: '))
max = int(input('Please enter maximum number: '))
time.sleep(2)
a(min,max)

