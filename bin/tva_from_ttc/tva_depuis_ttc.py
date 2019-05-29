#!/usr/bin/env python3
#
# Author  : Med Boutaleb @M3xB0
# Contact : M3xB0@protonmail.ch
#

import os
import sys
import random
import time
from numbers import Number

def tva_from_ttc_logo():
	time.sleep(0.08)
	print("             ╔╦╗╦  ╦╔═╗  ┌┬┐┌─┐┌─┐┬ ┬┬┌─┐  ╔╦╗╔╦╗╔═╗")
	time.sleep(0.08)
	print("              ║ ╚╗╔╝╠═╣   ││├┤ ├─┘│ ││└─┐   ║  ║ ║  ")
	time.sleep(0.08)
	print("╔──────────── ╩  ╚╝ ╩ ╩  ─┴┘└─┘┴  └─┘┴└─┘   ╩  ╩ ╚═╝──────────────╗")
	time.sleep(0.08)
	print("| Ce Module Calcule le Montant TVA depuis le Montat TTC           |")
	time.sleep(0.08)
	print("╚─────────────────────────────────────────────────────────────────╝")


# RESPONDS ARRAY
blank_input_respond = ["vous n'avez rien entré", "rien entré, essayez encore", "vous avez appuyé sur entrée sans rien entrer"]
invalid_user_input = ["ce que vous avez tapé n'est pas un nombre, je ne peux pas calculer autre chose que des nombres", "vous avez tapé autre chose que des chiffres, veuillez réessayer"]
keyboard_interrupt = ["Vous avez appuyé sur CTRL+C .. À plus tard."]

try:
	tva_from_ttc_loop = True
	while tva_from_ttc_loop:
		# START THE SCRIPT
		os.system("clear")
		tva_from_ttc_logo()

		# ASK THE USER FOR INPUR
		print("             _____________________")
		print("   ----------| TTC vers Hors Tax |-----------")
		ttc = str(input("[?_?] Entrez la valeur TTC : "))

		try:
			if not ttc:
				print(random.choice(blank_input_respond))
				tva_from_ttc_loop = True
			else:
				tva_from_ttc_loop2 = True
				while tva_from_ttc_loop2:
					try:
						tva_int = str(input("[?_?] Entrez le Taux du TVA % : "))
						if not tva_int:
							print(random.choice(blank_input_respond))
							tva_from_ttc_loop2 = True
						else:
							# ADD 1. TO THE TVA
							tva_method = "1."
							# CONVERT VERIABLES
							tva_to_str = str(tva_int)
							tva_stringed = tva_method + tva_to_str
							tva_to_str_rev = float(tva_stringed)
							ttc_float = float(ttc)
							# calculating HT
							ht = ttc_float / tva_to_str_rev
							# calculating tva
							tva_value = ttc_float - ht 
							# PRINT THE RESULT
							print ("['_'] TAUX TVA et :", "{0:.2f}".format(tva_value))
							print("")
							# ASK FOR PERMISION TO EXIT
							time.sleep(0.1)
							user_repitition = str(input("['_'] Appuyer Sur La touch Entre pour continuer "))
							# EXIT THE LOOPS
							ht_to_ttc_loop = False
							exit()
					except ValueError:
						print(random.choice(invalid_user_input))
						tva_from_ttc_loop = True
					except KeyboardInterrupt:
						print()
						print(random.choice(keyboard_interrupt))
						tva_from_ttc_loop = False
						exit()
		except ValueError:
			print(random.choice(invalid_user_input))
			tva_from_ttc_loop = True
		except KeyboardInterrupt:
			print()
			print(random.choice(keyboard_interrupt))
			tva_from_ttc_loop = False
			exit()
except ValueError:
	print(random.choice(invalid_user_input))
	tva_from_ttc_loop = True
except KeyboardInterrupt:
	print()
	print(random.choice(keyboard_interrupt))
	tva_from_ttc_loop = False
	exit()

