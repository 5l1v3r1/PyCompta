# for testing: 
hTax_F = 1000


	###################
	# 1 - Get rabais% #
	###################


def get_rabais():
	try:
		user_rabais_confirmation = input("[?_?] Il y a d'Rabais? (y/N): ")
		if user_rabais_confirmation == "y" or user_rabais_confirmation == "Y":
			rabais_looping = True
			while rabais_looping:
				user_input_rabais_S = str(input("[+_+] Entrez Votre Rabais (%): "))
				try:
					if not user_input_rabais_S:
						print(random.choice(blank_input_respond))
						rabais_looping = True
					else:
						try:
							# convert the String to a float
							global rab_float
							global rab1_val
							global net_comRabais1 # Global declarations
							rab_float = float(user_input_rabais_S)
							rab1_val = hTax_F * rab_float / 100	# rabais calculation and declaration
							net_comRabais1 = hTax_F - rab1_val
							print("['_'] Resultat Net Commercial après le Rabais et ", net_comRabais1)
							rabais_looping = False

							# ask the user for the second rab
							second_rab_respond = input("[?_?] Y a-t-il un deuxième Rabais? (y/n): ")
							if second_rab_respond == "y" or second_rab_respond == "Y":
								rab2_loop = True
								while rab2_loop:
									#print("Entret Votre 2em rabais(%): ")
									rab2_S = str(input("[+_+] Entrez Votre 2em rabais(%): "))
									
									try:
										if not rab2_S:
											print(random.choice(blank_input_respond))
											rab2_loop = True
										else:
											try:
												global net_comRabais2 # Global declaration
												global rab2_val
												global rab2_float
												rab2_float = float(rab2_S) # convert the String to a float
												rab2_val = net_comRabais1 * rab2_float / 100 # rabais calculation and daclaration
												net_comRabais2 = net_comRabais1 - rab2_val
												print("['_'] Resultat Net Commercial après le 2em Rabais et", net_comRabais2)
												rab2_loop = False

												# i can ask the user for the 3d rabais if i want to
												# second_rab_respond = input("is there a 3d rabais ?(y/n)")

											except ValueError:
												print(random.choice(invalid_user_input))
												rab2_loop = True
									except KeyboardInterrupt:
										print("")
										print(random.choice(keyboard_interrupt))
										rab2_loop = False
										exit()
									#---------

						except ValueError:
							print(random.choice(invalid_user_input))
							rabais_looping = True
				except KeyboardInterrupt:
					print("")
					print(random.choice(keyboard_interrupt))
					rabais_looping = False
					exit()
	except KeyboardInterrupt:
		print("")
		print(random.choice(keyboard_interrupt))
		exit()
		

get_rabais()

