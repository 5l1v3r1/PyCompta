last_NF_amount = 6000

#######################
# 9 - get TVA General #
#######################

#	i need to replace last_NF_amount with the last variable
last_NF_amount = 6000


def get_tva_general():
	try:
		taux_tva_loop = True
		while taux_tva_loop:
			try:
				taux_tva_string = str(input("[+_+] Entrez le montant du TVA general: "))
				if not taux_tva_string:
					print(random.choice(blank_input_respond))
				else:
					# global declaration
					global taux_tva_float
					global tva_general
					global last_NF_amount
					# Convert the strg to float
					taux_tva_float = float(taux_tva_string)
					# Calculate TVA general from the last NF:
					tva_general = last_NF_result * taux_tva_float / 100
					print("['_'] Resultat TVA-General :", tva_general)
					# Exit the loop
					taux_tva_loop = False

			#if the value is incorrect trow an error
			except KeyboardInterrupt: # ask the user if he wana quit or not
				print("")
				user_quit_respond = input("[._.] Vous avez appuyé sur CTRL+C, quite le Program ? (y/n): ")
				if user_taux_tva_quit_respond == "y" or user_taux_tva_quit_respond == "Y":
					taux_tva_loop = False
					exit(0)
				else:
					taux_tva_loop = True
			except ValueError:
				print(random.choice(invalid_user_input))
				taux_tva_loop = True
			
	except KeyboardInterrupt:
		print("")
		print(random.choice(keyboard_interrupt))
		exit()

