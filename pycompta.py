#!/usr/bin/env python3
#
# Author  : Med Boutaleb @m3dsec
# Contact : m3d5ec@protonmail.ch
#

import os
import sys
import random
import time

pycompta_logo = '''
 ____           ____                                __              
/\  _`\        /\  _`\                             /\ \__            
\ \ \L\ \__  __\ \ \/\_\    ___     ___ ___   _____\ \ ,_\    __       
 \ \ ,__/\ \/\ \\ \ \/_/_  / __`\ /' __` __`\/\ '__`\ \ \/  /'__`\      
  \ \ \/\ \ \_\ \\ \ \L\ \/\ \L\ \/\ \/\ \/\ \ \ \L\ \ \ \_/\ \L\.\_    
   \ \_\ \/`____ \\ \____/\ \____/\ \_\ \_\ \_\ \ ,__/\ \__\ \__/.\_\   
    \/_/  `/___/> \\/___/  \/___/  \/_/\/_/\/_/\ \ \/  \/__/\/__/\/_/   
             /\___/ -=[ PyCompta v1.4-dev ]=-   \ \_\                   
             \/__/ --=[ 4 Modules         ]=--   \/_/ 
                  ---=[ Coded By Med Boutaleb @m3dsec  ]=---    
                 ----=[ Contact : m3d5ec@protonmail.ch ]=----  '''

def menu_general():
	time.sleep(0.1)
	print(" ┌──────────────┐")
	time.sleep(0.08)
	print(" │ Menu General │")
	time.sleep(0.08)
	print(" ├┬┬┬┬──────────┘")
	time.sleep(0.1)
	print(" ││││└─┬─> 1 - Calculation d'Facture Complet")
	time.sleep(0.1)
	print(" │││└─┬┤─> 2 - HT vers TTC")
	time.sleep(0.1)
	print(" ││└┬─│┤─> 3 - TTC vers HT")
	time.sleep(0.1)
	print(" │├─│─│┤─> 4 - TVA depuis TTC")
	time.sleep(0.1)
	print(" ├│─│─│┤─> 99 - Quité")
	time.sleep(0.08)
	print(" └┴┬┴─┴┘ ")
   

# RESPONDS ARRAY
blank_input_respond = ["   vous n'avez rien entré", "   rien entré, essayez encore", "   vous avez appuyé sur entrée sans rien entrer"]
invalid_user_input = ["   ce que vous avez tapé n'est pas un nombre, je ne peux pas calculer autre chose que des nombres", "   vous avez tapé autre chose que des chiffres, veuillez réessayer"]
keyboard_interrupt = ["   Vous avez appuyé sur CTRL+C .. À plus tard."]
wrong_number = ["   ce que vous avez tapé n'est pas un nombre du list"] 

	############
	### MAIN ###
	############

os.system("clear")
print (pycompta_logo)
time.sleep(1)
print (menu_general)

big_loop = True
while big_loop:
	try:
		os.system("clear")
		print (pycompta_logo)
		menu_general()
		user_choice = int(input("   └PyCompta~#  "))
		if not user_choice:
			print(random.choice(blank_input_respond))
			big_loop = True
		else:
			if user_choice == 1:
				os.system("python3 bin/facture/facture__5__.py")
				big_loop = True
				time.sleep(0.6)
			elif user_choice == 2:
				os.system("python3 bin/ht_to_ttc/ht_to_ttc.py")
				big_loop = True
				time.sleep(0.6)
			elif user_choice == 3:
				os.system("python3 bin/ttc_to_ht/ttc_to_ht.py")
				big_loop = True
				time.sleep(0.6)
			elif user_choice == 4:
				os.system("python3 bin/tva_from_ttc/tva_depuis_ttc.py")
				big_loop = True
				time.sleep(0.6)
			elif user_choice == 99:
				big_loop = False
				exit(0)
			else:
				print(random.choice(wrong_number))
				big_loop = True
	except KeyboardInterrupt:
		print("")
		print(random.choice(keyboard_interrupt))
		big_loop = False
		exit()
	except ValueError:
		print(random.choice(invalid_user_input))
		big_loop = True




