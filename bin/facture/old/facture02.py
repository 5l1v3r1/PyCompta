from numbers import Number

# program pour generer une facture:

# global variable

######################
#  The main program  #
######################

big_loop = True
while big_loop:

	#########################
	# 0 - Get Montant Brute #
	#########################

	mb_looping = True
	while mb_looping:
		print("Entrer le Montant Brute 'HT'.")
		user_input_HT_S = str(input("-> "))

		try:
			if not user_input_HT_S:
				print("u didnt type any thing")
				mb_looping = True
			else:
				try:
					# convert the String to a float
					hTax_F = float(user_input_HT_S)
					mb_looping = False

				except ValueError:
					print("what you typed is not an int, so it cant be converted..")
					mb_looping = True	
		except KeyboardInterrupt:
			print("")			
			print("You Pressed CTRL+C..bye")
			mb_looping = False


		###################
		# 1 - Get rabais% #
		###################
	net_comRabais1 = None
	
	user_rabais_confirmation = input("Is there a rabais? (y/N)")
	if user_rabais_confirmation == "y" or user_rabais_confirmation == "Y":
		rabais_looping = True
		while rabais_looping:
			user_input_rabais_S = str(input("Entret Votre rabais(%): "))
			try:
				if not user_input_rabais_S:
					print("u didnt type any thing")
					rabais_looping = True
				else:
					try:
						# convert the String to a float
						rab_float = float(user_input_rabais_S)
						# print(rab_floatrabais_val)
						# rabais calculation
						rab1_val = hTax_F * rab_float / 100
						net_comRabais1 = hTax_F - rab1_val
						print("Net Comercial 'NC' et ", net_comRabais1)
						rabais_looping = False
						# ask the user for the second rab
						second_rab_respond = input("is there a second rab ?(y/n): ")
						if second_rab_respond == "y" or second_rab_respond == "Y":
							rab2_loop = True
							while rab2_loop:
								#print("Entret Votre 2em rabais(%): ")
								rab2_S = str(input("Entret Votre 2em rabais(%): "))
								
								try:
									if not rab2_S:
										print("u didnt type any thing")
										rab2_loop = True
									else:
										try:
											# convert the String to a float
											rab2_float = float(rab2_S)
											# rabais calculation
											rab2_val = net_comRabais1 * rab2_float / 100
											net_comRabais2 = net_comRabais1 - rab2_val
											print( "Net Comercial 'NC' et ", net_comRabais2 )
											rab2_loop = False

											# i can ask the user for the 3d rabais if i want to
											# second_rab_respond = input("is there a 3d rabais ?(y/n)")

										except ValueError:
											print("what you typed is not an int, so it cant be converted..")
											rab2_loop = True
								except KeyboardInterrupt:
									print("")
									print("You Pressed CTRL+C..bye")
									rab2_loop = False
								#---------
						#else:
							#exit(0)
					except ValueError:
						print("what you typed is not an int, so it cant be converted..")
						rabais_looping = True
			except KeyboardInterrupt:
				print("")
				print("You Pressed CTRL+C..bye")
				rabais_looping = False
	else:
		print("No rabais. pass to the next code.")



		## the calculation passing: get the last result from the previus calculation
	if net_comRabais1 >= 0:
		last_netCom_rab_result = net_comRabais2
	else:
	 	last_netCom_rab_result = net_comRabais1

		
	###################
	# 2 - Get Remis % #
	###################

	# need to make a condition if the net_com2 is created or not in the last rabais,, i think no i dnt need to
	rem1_loop = True
	while rem1_loop:
		user_input_rem_S = str(input("Entret Votre Remis (%): "))
		try:
			if not user_input_rem_S:
				print("u didnt type any thing")
				rem1_loop = True
			else:
				try:
					# convert the String to a float
					rem1_float = float(user_input_rem_S)
					# remis calculation
					rem1_val = last_netCom_rab_result * rem1_float / 100
					net_comRemis1 = last_netCom_rab_result - rem1_val
					print("Net Comercial 'NC' et ", net_comRemis1)
					rem1_loop = False
				#------------------------------------------------------
					# ask the user for the second remis
					second_rem_res = input("is there a second Remis? (y/n): ")
					if second_rem_res == "y" or second_rem_res == "Y":
						rem2_loop = True

						while rem2_loop:
							rem2_S = str(input("Entret Votre 2em Remis (%): "))
							try:
								if not rem2_S:
									print("u didnt type any thing")
									rem2_loop = True
								else:
									try:
										# convert the String to a float
										rem2_float = float(rem2_S)
										# remis calculation
										rem2_val = net_comRemis1 * rem2_float / 100
										net_comRemis2 = net_comRemis1 - rem2_val
										print("Net Comercial 'NC' et ", net_comRemis2)
										rem2_loop = False
									#------------
										# you can ask the user for more remises
									#------------
									except ValueError:
										print("what you typed is not an int, so it cant be converted..")
										rem2_loop = True
							except KeyboardInterrupt:
								print("")
								print("You Pressed CTRL+C..bye")
								rem2_loop = False
					#else:
					#	exit(0)
				#------------------------------------------------------
				except ValueError:
					print("what you typed is not an int, so it cant be converted..")
					rem1_loop = True
		except KeyboardInterrupt:
			print("")
			print("You Pressed CTRL+C..bye")
			rem1_loop = False



	# pass the results
	if net_comRemis1 >= 1:
		last_NC_remis_result = net_comRemis2
	else:
 		last_NC_remis_result = net_comRemis1


	######################
	# 3 - Get Ristourn % #
	######################

	user_ristourn_confirmation = input("Is there a Ristourn ? (y/N):")
	if user_ristourn_confirmation == "y" or user_ristourn_confirmation == "Y":
		rist1_loop = True
		while rist1_loop:
			rist1_S = str(input("Entret Votre Ristourn (%): "))
			try:
				if not rist1_S:
					print("u didnt type any thing")
					rist1_loop = True
				else:
					try:
						rist1_float = float(rist1_S)
						rist1_val = last_NC_remis_result * rist1_float / 100
						net_comRistourn1 = last_NC_remis_result - rist1_val
						print("[*] Net Comercial 'NC' et :", net_comRistourn1)
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
						print("what you typed is not an int, so it cant be converted..")
						rist1_loop = True
			except KeyboardInterrupt:
				print("")
				print("You Pressed CTRL+C..bye")
				rist1_loop = False



	"""
	# pass the results:
	if net_comRistourn1 >= 1:
		last_NC_rist_result = net_comRistourn2
	else:
 		last_NC_rist_result = net_comRistourn1
	"""
	last_NC_rist_result = net_comRistourn1


	######################
	# 4 - Get Escompte % #
	######################

	escom1_loop = True
	while escom1_loop:
		user_escompt_confirmation = input("y'a d'escompt ? (y/n): ")
		if user_escompt_confirmation == "y" or user_escompt_confirmation == "Y":
			escom1_S = str(input("Entrez taux Escompt (%): "))
			try:
				if not escom1_S:
					print("u didnt type any thing")
					escom1_loop = True
				else:
					try:
						escom1_float = float(escom1_S)
						escom1_val = last_NC_rist_result * escom1_float / 100
						netF_Escomp1 = last_NC_rist_result - escom1_val
						print("[*] Net Financier 'NF' et:", netF_Escomp1)
						escom1_loop = False # calculate, get of the loop and go to the next pieace of code.

						"""  because most of the time there is 1 escompt 
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
						print("what you typed is not an int, so it cant be converted..")
						escom1_loop = True
			except KeyboardInterrupt:
				print("")
				print("You Pressed CTRL+C..bye")
				escom1_loop = False
		else:
			# print("pas descompt. pass to the next code seccesfully.")
			escom1_loop = False
			big_loop = False



	###################
	# 5 - Get last NF #
	###################

	# pass the last results
	""" # because there is just one escompt. 
	if net_fin2 >= 1:
		last_escompt_result = net_fin2
		print("last NF is net_fin2 =", net_fin2)
	else:
 		last_escompt_result = net_fin1
		print("last NF is net_fin1 =", net_fin1)
		
	last_NF_result = last_escompt_result

	"""

	
	last_NF_result = netF_Escomp1


	#############################
	# 6/7-Get Port and Tva-port #
	#############################

	port_conf = input("Ya d'transPort? (y/n): ")
	if port_conf == "y" or port_conf == "Y":
		port_loop = True
		while port_loop:
			port_val = str(input("Entre le montant du port: ")) # i need to add a random choice function
			#------------- check the user input
			try:
				if not port_val:
					print("U didn't type any thing.") # add a random choice function
					port_loop = True
					
				else:
					#-------------- start the calculation
					try:
						port_val_float = float(port_val) # convert the string to float
						tva_port_loop = True
						while tva_port_loop:
							tva_val_str = str(input("Entre le Taux du TVA-Port: "))
							try:
								if not tva_val_str:
									print("please Enter a valid Number")
									tva_port_loop = True
								else:
									try:
										tva_val_float = float(tva_val_str)
										# calculation du tva port
										tva_port_result = port_val_float * tva_val_float / 100
										port_ttc_result = port_val_float + tva_port_result
										print("[*] Resulat du TVA-port :", tva_port_result)
										
										# exit the loops
										tva_port_loop = False
										port_loop = False
										big_loop = False
										
									except ValueError:
										print("what you typed is not an int, so it cant be converted..")
										tva_port_loop = True
							
							# handle Error from the second loop
							except KeyboardInterrupt: # say bye and quit
								print("You Pressed CTRL+C, Bye..")
								tva_port_loop = False
								exit(0)
							except ValueError:
								print("The Value you Entred Is incorrect. Try Again.")
								tva_port_loop = True
					#----------
						print("[*] Resulat du Port + TVA :", port_ttc_result)
						port_loop = False
					
					# handle error from conversion.
					except ValueError:
						print("what you typed is not a number,it can't be procesed..")
						port_loop = True
					except KeyboardInterrupt: # Say bye and quit
						print("You Pressed CTRL+C, Bye..")
						exit(0)
						
			except KeyboardInterrupt:
				print("")
				user_quit_respond = input("You pressed CTRL+C..Bye")
				port_loop = False
				sexit(0)
	
	
	
	####################
	# 8 - get Embalage #
	####################

	"""
	emb_unit........ = is how many unit of embalage u have
	emb_prix_unit... = is how mush the price of 1 unit
	"""
	embalage_confirmation = input("yia d'embalage ? (y/n): ")
	if embalage_confirmation == "y" or embalage_confirmation == "Y":
		emb_loop = True
		while emb_loop:
			emb_unit_str = str(input("Entrer la quantiter d'embalage: "))
			try:
				if not emb_unit_str:
					print("u didnt type any thing")
					emb_loop = True
				else:
					try:
						emb_unit_float = float(emb_unit_str) # convert the quant from str to float
						#-------
						# ask the user for the prix unitaire
						emb_prix_unit_str = input("Entrer le prix unitaire d'embalage: ")
						emb_prix_unit_loop = True
						# enter an other loop to check the user input
						while emb_prix_unit_loop:
							try:
								if not emb_prix_unit_str:
									print("please specify a prix unitaire")
									emb_prix_unit_loop = True
								else:
									# conver the prix unitaire to float for calculation
									emb_prix_unit_float = float(emb_prix_unit_str) 
									emb_value = emb_prix_unit_float * emb_unit_float
						#-------
									print("[*] Resultat Embalage : ", emb_value)
									emb_prix_unit_loop = False
									emb_loop = False
							except ValueError:
								print("what you typed is not an int, so it cant be converted..")
								emb_loop = True
					except ValueError:
						print("what you typed is not an int, so it cant be converted..")
						emb_loop = True
				
			except KeyboardInterrupt: # ask the user if he wana quit or not
				print("")
				user_quit_respond = input("You pressed CTRL+C..Do you want to quit? (y/n): ")
				if user_quit_respond == "y" or user_quit_respond == "Y":
					emb_loop = False
					exit(0)
				else:
					emb_loop = True


	#######################
	# 9 - get TVA General #
	#######################

	taux_tva_loop = True
	while taux_tva_loop:
		try:
			taux_tva_string = str(input("Entrer le montant du TVA general: "))
			if not taux_tva_string:
				print("you typed nothin")
			else:
				# Convert the strg to float
				taux_tva_float = float(taux_tva_string)
				# Calculate TVA general from the last NF:
				tva_general = last_NF_amount * taux_tva_float / 100
				print("[*] Resultat TVA-General :", tva_general)
				# Exit the loop
				taux_tva_loop = False

		#if the value is incorrect trow an error
		except KeyboardInterrupt: # ask the user if he wana quit or not
			print("")
			user_quit_respond = input("You pressed CTRL+C..Do you want to quit? (y/n): ")
			if user_taux_tva_quit_respond == "y" or user_taux_tva_quit_respond == "Y":
				taux_tva_loop = False
				exit(0)
			else:
				taux_tva_loop = True
		except ValueError:
			print("The value you entred is Incorrect, please try again.")
			taux_tva_loop = True
		
		
	###################
	# 10- get NET TTC #
	###################

	net_ttc = last_NF_result + port_val_float + tva_port_result + emb_value + tva_general
	print("[*] Resultat Net TTC :", net_ttc)



########################
# 11- Print everything #
########################
print(" ________________________________________")
print("|*---------------------------------------")
print("| MB                 	", hTax_F)
print("| Rabais", rab_float, 	"%		", rab1_val)
print("| Rabais2", rab2_float,	"%		", rab2_val)
print("| ----------------------")
print("| NetC 1            	", last_netCom_rab_result)
print("| Remise1", rem1_float,	"%		", rem1_val)
print("| Remise2", rem2_float,	"%		", rem2_val)
print("| ----------------------")
print("| NetC 2            	", last_NC_remis_result)
print("| Ristourn", rist1_float,"%		", net_comRistourn1)
print("| ----------------------")
print("| NetC              	", last_NC_rist_result)
print("| Escompt", escom1_float ,"%		", escom1_val)
print("| ----------------------")
print("| NetF              	", last_NF_result)
print("| Transport         	", port_val_float)
print("| Tva Port", tva_val_float, "%		", tva_port_result)
print("| Embalage          	", emb_value)
print("| TVA", taux_tva_float, 	"%		", tva_general)
print("| ----------------------")
print("| Net TTC           	", net_ttc)
print("|________________________________________")
print("*----------------------------------------")


