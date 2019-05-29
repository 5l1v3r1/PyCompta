

# declare the last amount to work with
last_NC_rist_result = 1000

	######################
	# 4 - Get Escompte % #
	######################
def get_escompt():
	try:
		escom1_loop = True
		while escom1_loop:
			user_escompt_confirmation = input("[?_?] Il y a d'Escompt? (y/N): ")
			if user_escompt_confirmation == "y" or user_escompt_confirmation == "Y":
				escom1_S = str(input("[+_+] Entrez Votre Escompt (%): "))
				try:
					if not escom1_S:
						print(random.choice(blank_input_respond))
						escom1_loop = True
					else:
						try:
							# global declaration
							global escom1_float
							global netF_Escomp1
							global escom1_val
							escom1_float = float(escom1_S)
							escom1_val = last_NC_rist_result * escom1_float / 100
							netF_Escomp1 = last_NC_rist_result - escom1_val
							print("['_'] Resultat Net Financier après L'escompt et ", netF_Escomp1)
							escom1_loop = False # calculate, get of the loop and go to the next pieace of code.

							"""  because most of the time there is 1 escompt i'll get enaught with one escompt
							#------------------------------------------------------
							# ask the user for the second Ristourn
							second_escompt_res = input("is there a second Escompt? (y/n): ")
							if second_escompt_res == "y" or second_escompt_res == "Y":
							
								escom2_loop = True # define a second loop
								while escom2_loop:
									escom2_S = str(input("Entret Votre 2em Escompt (%): "))
									try:
										if not escom2_S:
											print("u didnt type any thing")
											escom2_loop = True
										else:
											try:
												escom2_float = float(escom2_S)

												# 2nd Escompt calculation
												escom2_val = net_fin1 * escom2_float / 100
												net_fin2 = net_fin1 - escom2_val
												print("Net Financier 'NF' et ", net_fin2)
												escom1_loop = False
												escom2_loop = False
											#------------
											# i can add more escompts here
											#------------
											except ValueError:
												print("what you typed is not an int, so it cant be converted..")
												escom2_loop = True
											except KeyboardInterrupt:
												print("You Pressed CTRL+C..bye")
												escom2_loop = False

									except ValueError:
										print("")
										print("what you typed is not an int, so it cant be converted..")
										escom2_loop = False
									except KeyboardInterrupt:
										print("")
										print("You Pressed CTRL+C..bye")
										escom2_loop = False
							elif second_escompt_res == "n" or second_escompt_res == "N":
								escom1_loop = False
								escom2_loop = False
								
							elif not second_escompt_res:
								print("Please specify an answer!!")
								escom1_loop = False
								escom2_loop = True
							#------------------------------------------------------
							"""

						except ValueError:
							print(random.choice(invalid_user_input))
							escom1_loop = True
						except KeyboardInterrupt:
							print("")
							print(random.choice(keyboard_interrupt))
							exit()
							
				except ValueError:
					print(random.choice(invalid_user_input))
					escom1_loop = True	
				except KeyboardInterrupt:
					print("")
					print(random.choice(keyboard_interrupt))
					escom1_loop = False
					exit()
			else:
				# print("|-_-| pas descompt. pass to the next code seccesfully.")
				escom1_loop = False
				big_loop = False
				
	except KeyboardInterrupt:
		print("")
		print(random.choice(keyboard_interrupt))
		escom1_loop = False
		exit()

get_escompt()
