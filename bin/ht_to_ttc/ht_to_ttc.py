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

def logo_ht_to_ttc():
	print("                  ╦ ╦╔╦╗  ┌┬┐┌─┐  ╔╦╗╔╦╗╔═╗")
	time.sleep(0.08)
	print("                  ╠═╣ ║    │ │ │   ║  ║ ║  ")
	time.sleep(0.08)
	print("╔──────────────── ╩ ╩ ╩    ┴ └─┘   ╩  ╩ ╚═╝ ──────────────────────╗")
	time.sleep(0.08)
	print("| Ce Module Calcule la Résultat 'TTC' basé sur le Montant 'HT' et |")
	time.sleep(0.08)
	print("| le Taux 'TVA' Entrée par l'utilisateur.                         |")
	time.sleep(0.08)
	print("╚─────────────────────────────────────────────────────────────────╝")

# RESPONDS ARRAY
blank_input_respond = ["vous n'avez rien entré", "rien entré, essayez encore", "vous avez appuyé sur entrée sans rien entrer"]
invalid_user_input = ["ce que vous avez tapé n'est pas un nombre, je ne peux pas calculer autre chose que des nombres", "vous avez tapé autre chose que des chiffres, veuillez réessayer"]
keyboard_interrupt = ["Vous avez appuyé sur CTRL+C..Retour vers le Menu General"]

try:
	ht_to_ttc_loop = True
	while ht_to_ttc_loop:
		# START THE SCRIPT
		os.system("clear")
		logo_ht_to_ttc()

		# ASK THE USER FOR INPUR
		time.sleep(0.1)
		print("             _____________________")
		print("   ----------| Hors Tax vers TTC |-----------")
		ht_str = str(input("[?_?] Entrez la valeur HT: "))

		try:
			if not ht_str:
				print(random.choice(blank_input_respond))
				ht_to_ttc_loop = True
			else:
				ht_to_ttc_tva_loop = True
				while ht_to_ttc_tva_loop:
					try:
						time.sleep(0.1)
						tva_str = str(input("[?_?] Entrez le Taux du TVA % : "))
						if not tva_str:
							print(random.choice(blank_input_respond))
							ht_to_ttc_tva_loop = True
						else:
							# CONVERT ENTRED STRING TO FLOATS
							ht = float(ht_str)
							tva = float(tva_str)
							# CALCULATE THE OUTPUT
							tva_result = ( ht * tva ) / 100
							ttc = tva_result + ht
							# PRINT THE RESULT
							time.sleep(0.1)
							print ("['_'] Resultat TTC et :", "{0:.2f}".format(ttc))
							print("")
							# ASK FOR PERMISION TO EXIT
							time.sleep(0.1)
							user_repitition = str(input("['_'] Appuyer Sur La touch Entre pour continuer "))
							# EXIT THE LOOPS
							ht_to_ttc_loop = False
							exit()
					except ValueError:
						print(random.choice(invalid_user_input))
						ht_to_ttc_loop = True
					except KeyboardInterrupt:
						print("")
						print(random.choice(keyboard_interrupt))
						ht_to_ttc_loop = False
						exit()

		except ValueError:
			print(random.choice(invalid_user_input))
			ht_to_ttc_loop = True
		except KeyboardInterrupt:
			print("")
			print(random.choice(keyboard_interrupt))
			ht_to_ttc_loop = False
			exit()

except ValueError:
	print(random.choice(invalid_user_input))
	ht_to_ttc_loop = True

except KeyboardInterrupt:
	print("")
	print(random.choice(keyboard_interrupt))
	ht_to_ttc_loop = False
	exit()

