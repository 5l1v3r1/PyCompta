last_NC_remis_result = 10101.11

	######################
	# 3 - Get Ristourn % #
	######################

def get_ristourn():
	try:
		user_ristourn_confirmation = input("[?_?] Il y a d'Ristourn? (y/N): ")
		if user_ristourn_confirmation == "y" or user_ristourn_confirmation == "Y":
			rist1_loop = True
			while rist1_loop:
				rist1_S = str(input("[+_+] Entrez Votre Ristourn (%): "))
				try:
					if not rist1_S:
						print(random.choice(blank_input_respond))
						rist1_loop = True
					else:
						try:
						
							# declaration of global declaration
							global net_comRistourn1
							global rist1_val
							global rist1_float
							
							# convert ristourn string to float
							rist1_float = float(rist1_S)
							# start the calculation
							rist1_val = last_NC_remis_result * rist1_float / 100
							net_comRistourn1 = last_NC_remis_result - rist1_val
							print("['_'] Resultat Net Commercial après Ristourn et ", net_comRistourn1)
							# i'll not print the result till the user confirm thet
							# there is no other ristourn
							rist1_loop = False
							
							""" i'll need just one ristourn
						#------------------------------------------------------
							# ask the user for the second Ristourn
							second_rist_res = input("is there a second Ristourn? (y/n): ")
							if second_rist_res == "y" or second_rist_res == "Y":
								rist2_loop = True

								while rist2_loop:
									rist2_S = str(input("Entret Votre 2em Ristourn (%): "))
									try:
										if not rist2_S:
											print("u didnt type any thing")
											rist2_loop = True
										else:
											try:
												# convert the String to a float
												rist2_float = float(rist2_S)
												# remis calculation
												rist2_val = net_comRistourn1 * rist2_float / 100
												net_comRistourn2 = net_comRistourn1 - rist2_val
												print("[*] Net Comercial 'NC' :", net_comRistourn2)
												rist2_loop = False
											#------------
												# you can ask the user for more remises
												# but you will need to edit the calculation passing between
												# the blocks of code  
											#------------
											except ValueError:
												print("what you typed is not an int, so it cant be converted..")
												rist2_loop = True
									except KeyboardInterrupt:
										print("")
										print("You Pressed CTRL+C..bye")
										rist2_loop = False
							else:
								# return a fonction or somethin else
								print("[*] Net Comercial 'NC' et :", net_comRistourn1)
								rist2_loop = False
								rist1_loop = False
						#------------------------------------------------------
						"""
						except ValueError:
							print(random.choice(invalid_user_input))
							rist1_loop = True
						except KeyboardInterrupt:
							print("")
							print(random.choice(keyboard_interrupt))
							rist1_loop = False
							exit()
				except KeyboardInterrupt:
					print("")
					print(random.choice(keyboard_interrupt))
					rist1_loop = False
					exit()
	except KeyboardInterrupt:
		print("")
		print(random.choice(keyboard_interrupt))
		rist1_loop = False
		exit()


