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

def logo_ttc_to_ht():
	time.sleep(0.08)
	print("                   ╔╦╗╔╦╗╔═╗  ┌┬┐┌─┐  ╦ ╦╔╦╗")
	time.sleep(0.08)
	print("                    ║  ║ ║     │ │ │  ╠═╣ ║ ")
	time.sleep(0.08)
	print("╔────────────────── ╩  ╩ ╚═╝   ┴ └─┘  ╩ ╩ ╩ ──────────────────────╗")
	time.sleep(0.08)
	print("| Ce module inverse la resultat TTC vers le hors tax(HT)          |")
	time.sleep(0.08)
	print("╚─────────────────────────────────────────────────────────────────╝")
	time.sleep(0.1)


# RESPONDS ARRAY
blank_input_respond = ["vous n'avez rien entré", "rien entré, essayez encore", "vous avez appuyé sur entrée sans rien entrer"]
invalid_user_input = ["ce que vous avez tapé n'est pas un nombre, je ne peux pas calculer autre chose que des nombres", "vous avez tapé autre chose que des chiffres, veuillez réessayer"]
keyboard_interrupt = ["Vous avez appuyé sur CTRL+C, Rerour vers le Menu General"]

try:
	ttc_to_ht_loop = True
	while ttc_to_ht_loop:
		# START THE SCRIPT
		os.system("clear")
		logo_ttc_to_ht()

		# ASK THE USER FOR INPUR
		print("             _____________________")
		print("   ----------| TTC vers Hors Tax |-----------")
		time.sleep(0.07)
		ttc = str(input("[?_?] Entrez la valeur TTC : "))

		try:
			if not ttc:
				print(random.choice(blank_input_respond))
				ttc_to_ht_loop = True
			else:
				tcc_to_ht_tva_loop = True
				while tcc_to_ht_tva_loop:
					try:
						time.sleep(0.07)
						tva_int = str(input("[?_?] Entrez le Taux du TVA % : "))
						if not tva_int:
							print(random.choice(blank_input_respond))
							tcc_to_ht_tva_loop = True
						else:
							# ADD 1. TO THE TVA
							tva_method = "1."
							
							# CONVERT VERIABLES
							tva_to_str = str(tva_int)
							tva_stringed = tva_method + tva_to_str
							tva_to_str_rev = float(tva_stringed)
							ttc_float = float(ttc)

							# CALCULATE HT
							ht = ttc_float / tva_to_str_rev

							# PRINT THE RESULT
							time.sleep(0.08)
							print ("['_'] Resultat HT et :", "{0:.2f}".format(ht))
							print("")
							# ASK FOR PERMISION TO EXIT
							time.sleep(0.1)
							user_repitition = str(input("['_'] Appuyer Sur La touch Entre pour continuer "))
							# EXIT THE LOOPS
							ht_to_ttc_loop = False
							exit()
					except ValueError:
						print(random.choice(invalid_user_input))
						ttc_to_ht_loop = True
					except KeyboardInterrupt:
						print()
						print(random.choice(keyboard_interrupt))
						ttc_to_ht_loop = False
						exit()
		except ValueError:
			print(random.choice(invalid_user_input))
			ttc_to_ht_loop = True
		except KeyboardInterrupt:
			print()
			print(random.choice(keyboard_interrupt))
			ttc_to_ht_loop = False
			exit(0)
except ValueError:
	print(random.choice(invalid_user_input))
	ttc_to_ht_loop = True
except KeyboardInterrupt:
	print()
	print(random.choice(keyboard_interrupt))
	ttc_to_ht_loop = False
	exit(0)

