						
	####################
	# 8 - get Embalage #
	####################
# emb_unit........ = is how many unit of embalage u have
# emb_prix_unit... = is how mush the price of 1 unit

def get_embalage():
	try:
		embalage_confirmation = input("[?_?] Y a-t-il d'Embalage (y/N): ")
		if embalage_confirmation == "y" or embalage_confirmation == "Y":
			emb_loop = True
			while emb_loop:
				emb_unit_str = str(input("[+_+] Entrez la Quantiter d'Embalage: "))
				try:
					if not emb_unit_str:
						print(random.choice(blank_input_respond))
						emb_loop = True
					else:
						try:
							global emb_unit_float
							emb_unit_float = float(emb_unit_str) # convert the quant from str to float
							#-------
							# ask the user for the prix unitaire
							emb_prix_unit_str = input("[+_+] Entrez le Prix Unitaire des piece : ")
							emb_prix_unit_loop = True
							# enter an other loop to check the user input
							while emb_prix_unit_loop:
								try:
									if not emb_prix_unit_str:
										print(random.choice(blank_input_respond))
										emb_prix_unit_loop = True
									else:
										# global declaration
										global emb_value
										global emb_prix_unit_float
										# conver the prix unitaire to float for calculation
										emb_prix_unit_float = float(emb_prix_unit_str) 
										emb_value = emb_prix_unit_float * emb_unit_float
							#-------
										print("['_'] Resultat d'Embalage : ", emb_value)
										emb_prix_unit_loop = False
										emb_loop = False
								except ValueError:
									print(random.choice(invalid_user_input))
									emb_loop = True
								except KeyboardInterrupt:
									print(random.choice(keyboard_interrupt))
									emb_loop = False
									
						except ValueError:
							print(random.choice(invalid_user_input))
							emb_loop = True
					
				except KeyboardInterrupt: # ask the user if he wana quit or not
					print("")
					user_quit_respond = input("[._.] Vous avez appuyé sur CTRL+C, quite le Program ? (y/n): ")
					if user_quit_respond == "y" or user_quit_respond == "Y":
						emb_loop = False
						exit(0)
					else:
						emb_loop = True
	except KeyboardInterrupt:
		print("")
		print(random.choice(keyboard_interrupt))
		exit()


