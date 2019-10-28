import os
import sys
from time import sleep as timeout
from core.starkmcore import *
from core.deepmcore import *
from multiprocessing import Process
from termcolor import colored

def Facebookhack():
	print ('###### installing facebook hack')
	os.system('apt install python2')
	os.system('cd && mkdir facebookhack')
	os.system('wget https://www.dropbox.com/s/4d72hyfwrii5vw7/facebook.py ')
	os.system('mv facebook.py $HOME/facebookhack')
	backtomenu()
def achacking():
 print(colored("""
     ==================================================
     ....###.........######.....##.....##....###.....######..##....##
     ...##.##.......##....##....##.....##...##.##...##....##.##...##.
     ..##...##......##..........##.....##..##...##..##.......##..##..
     .##.....##.....##..........#########.##.....##.##.......#####...
     .#########.....##..........##.....##.#########.##.......##..##..
     .##.....##.###.##....##....##.....##.##.....##.##....##.##...##.
     .##.....##.###..######.....##.....##.##.....##..######..##....##
     ==================================================
	1. Facebook Hack
	2. Instagram Hack
	3. Phishy
	4. Weeman
	5. MBF
	6. Shellphish
	7. Back
     ==================================================
    """, 'green'))

 acha = raw_input("stark > ")

 if acha == "1":
    	Facebookhack()
 elif acha == "2":
    	Instagramhack()
 elif acha == "3":
    	Phishy()
 elif acha == "4":
    	Weeman()
 elif acha == "5":
 	Mbf()
 elif acha == "6":
 	shellphish()
 elif acha == "7":
 	os.system("clear")
 	restartprogram()
 elif acha == "0":
        restartprogram()
 else:
	print(colored("ERROR: WRONG COMMAND BRO.?", 'red'))
	restartprogram()

