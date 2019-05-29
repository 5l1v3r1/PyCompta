		
	###################
	# 2 - Get Remis % #
	###################

def get_remis():
	try:
		user_rabais_confirmation = input("[?_?] Il y a des Remises ? (y/N): ")
		if user_rabais_confirmation == "y" or user_rabais_confirmation == "Y":
			rem1_loop = True
			while rem1_loop:
				user_input_rem_S = str(input("[+_+] Entrez Votre Remise(%): "))
				try:
					if not user_input_rem_S:
						print(random.choice(blank_input_respond))
						rem1_loop = True
					else:
						try:
							# convert the String to a float and declare it
							global rem1_float
							rem1_float = float(user_input_rem_S)
							
							# remis calculation and declaration
							global net_comRemis1 # global declaration 
							global rem1_val
							rem1_val = last_netCom_rab_result * rem1_float / 100
							net_comRemis1 = last_netCom_rab_result - rem1_val
							print("['_'] Resultat Net Commercial après La Remise et ", net_comRemis1)
							rem1_loop = False
						#------------------------------------------------------
							# ask the user for the second remis
							second_rem_res = input("[?_?] Y a-t-il un deuxième Remise ? (y/n): ")
							if second_rem_res == "y" or second_rem_res == "Y":
								rem2_loop = True

								while rem2_loop:
									rem2_S = str(input("[+_+] Entrez Votre 2em Remise (%): "))
									try:
										if not rem2_S:
											print(random.choice(blank_input_respond))
											rem2_loop = True
										else:
											try:
												# convert the String to a float
												global rem2_float
												rem2_float = float(rem2_S)
												# remis calculation and declaration
												global net_comRemis2 # declaration
												global rem2_val
												rem2_val = net_comRemis1 * rem2_float / 100
												net_comRemis2 = net_comRemis1 - rem2_val
												print("['_'] Resultat Net Commercial après La 2em Remise et ", net_comRemis2)
												rem2_loop = False
											#------------
												# here i can ask the user for more remises
											#------------
											except ValueError:
												print(random.choice(invalid_user_input))
												rem2_loop = True
									except KeyboardInterrupt:
										print("")
										print(random.choice(keyboard_interrupt))
										rem2_loop = False
							#else:
							#	exit(0)
						#------------------------------------------------------
						except ValueError:
							print(random.choice(invalid_user_input))
							rem1_loop = True
						except KeyboardInterrupt:
							print("")
							print(random.choice(keyboard_interrupt))
							rem1_loop = False
							exit()
				except KeyboardInterrupt:
					print("")
					print(random.choice(keyboard_interrupt))
					rem1_loop = False
					exit()
	except KeyboardInterrupt:
		print("")
		print(random.choice(keyboard_interrupt))
		exit()
			

