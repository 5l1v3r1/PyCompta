"""
# old calculation
	try:
		port_conf = input("[?_?] Il y a du Transport ? (y/n): ")
		if port_conf == "y" or port_conf == "Y":
			port_loop = True
			while port_loop:
				transport_type = str(input("[?_?] Votre Transport et Forfitaire(20%)-Debours(14%)-Personaliser(?%) (F/D/P): "))
				if transport_type
				
				
				
				# Calculation du port manual
				port_val = str(input("[+_+] Entrez Le Montant du Transport :  "))
				#------------- check the user input
				try:
					if not port_val:
						print(random.choice(blank_input_respond))
						port_loop = True
						
					else:
						#-------------- start the calculation
						try:
							global port_val_float # global declaration for later printing
							port_val_float = float(port_val) # convert the string to float
							tva_port_loop = True
							while tva_port_loop:
								tva_val_str = str(input("[+_+] Entre le Taux du TVA-Port: "))
								try:
									if not tva_val_str:
										print(random.choice(blank_input_respond))
										tva_port_loop = True
									else:
										try:
											global tva_val_float # global declaration for later printing
											global tva_port_result
											global port_ttc_result
											tva_val_float = float(tva_val_str) # convertion
											tva_port_result = port_val_float * tva_val_float / 100	# calculation du tva port
											port_ttc_result = port_val_float + tva_port_result
											print("['_'] Resultat du TVA-PORT : ", tva_port_result)
											
											# exit the loops
											tva_port_loop = False
											port_loop = False
											big_loop = False
											
										except ValueError:
											print("what you typed is not an int, so it cant be converted..")
											tva_port_loop = True
										except KeyboardInterrupt:
											print("")
											print(random.choice(keyboard_interrupt))
											exit()
								# handle Error from the second loop
								except ValueError:
									print(random.choice(invalid_user_input))
									tva_port_loop = True
								except KeyboardInterrupt: # say bye and quit
									print(random.choice(keyboard_interrupt))
									tva_port_loop = False
									exit()
						#----------
							print("['_'] Resultat du Transoirt + TVA-Port :", port_ttc_result)
							port_loop = False

						# handle error from conversion.
						except ValueError:
							print(random.choice(invalid_user_input))
							port_loop = True
						except KeyboardInterrupt: # Say bye and quit
							print(random.choice(keyboard_interrupt))
							exit()					
				except KeyboardInterrupt:
					print("")
					print(random.choice(keyboard_interrupt))
					port_loop = False
					exit()
	except KeyboardInterrupt:
		print("")
		print(random.choice(keyboard_interrupt))
		exit()
"""
tva_forfitaire_result = 0
trans_forfitaire_ttc_result = 0
tva_debours_result = 0
trans_debours_ttc_result = 0
tva_port_result = 0
port_ttc_result = 0

# def get_port_and_tva_port():
big_loop = True
while big_loop:
	try:
		port_conf = input("[?_?] Il y a du Transport ? (y/n): ")
		if port_conf == "y" or port_conf == "Y":
			port_loop = True
			while port_loop:
				transport_type = str(input("[?_?] Votre Transport et Forfitaire(20%) / Debours(14%) / Personaliser(!%) (F/D/P): "))

				if transport_type == "F" or transport_type == "f":
					# DEBUT DU CALCULATION FORFITAIRE
					transport_forfitaire_loop = True
					while transport_forfitaire_loop:
						transport_value = str(input("[+_+] Entrez Le Montant du Transport :  "))
						try:
							if not transport_value:
								print(random.choice(blank_input_respond))
								transport_forfitaire_loop = True
							else:	
								global transport_forfitaire_value_float
								global tva_forfitaire_result
								global trans_forfitaire_ttc_result
								transport_forfitaire_value_float = float(transport_value)
								tva_forfitaire_result = transport_forfitaire_value_float * 20 / 100
								trans_forfitaire_ttc_result = transport_forfitaire_value_float + tva_forfitaire_result
								# prit the results
								print("['_'] Resultat du TVA-Forfitaire : ", tva_forfitaire_result)	
								print("['_'] Resultat du Transport + TVA-Forfitaire :", trans_forfitaire_ttc_result)
								# exit the loops
								transport_debours_loop = False
								port_loop = False
								big_loop = False
						except ValueError:
							print(random.choice(invalid_user_input))
							transport_forfitaire_loop = True
						except KeyboardInterrupt:
							print("")
							print(random.choice(keyboard_interrupt))
							exit()
					# FIN DU CALCULATION FORFITAIRE


				elif transport_type == "D" or transport_type == "d":
					# DEBUT DU CALCULATION DEBOURS
					transport_debours_loop = True
					while transport_debours_loop:
						transport_value = str(input("[+_+] Entrez Le Montant du Transport :  "))
						try:
							if not transport_value:
								print(random.choice(blank_input_respond))
								transport_debours_loop = True
							else:	
								global transport_debours_value_float
								global tva_debours_result
								global trans_debours_ttc_result
								transport_debours_value_float = float(transport_value)
								tva_debours_result = transport_debours_value_float * 20 / 100
								trans_debours_ttc_result = transport_debours_value_float + tva_debours_result
								# prit the results
								print("['_'] Resultat du TVA-Debours : ", tva_debours_result)	 
								print("['_'] Resultat du Transport + TVA-Debours :", trans_debours_ttc_result)
								# exit the loops
								transport_debours_loop = False
								port_loop = False
								big_loop = False
						except ValueError:
							print(random.choice(invalid_user_input))
							transport_debours_loop = True
						except KeyboardInterrupt:
							print("")
							print(random.choice(keyboard_interrupt))
							exit()
					# FIN DU CALCULATION DEBOURS


				else:					
					# DEBUT DU CALCULATION MANUAL
					manual_transport_loop = True
					while manual_transport_loop:
						
						port_val = str(input("[+_+] Entrez Le Montant du Transport :  "))
						#------------- check the user input
						try:
							if not port_val:
								print(random.choice(blank_input_respond))
								manual_transport_loop = True
								
							else:
								#-------------- start the calculation
								try:
									global port_val_float # global declaration for later printing
									port_val_float = float(port_val) # convert the string to float
									tva_port_loop = True
									while tva_port_loop:
										tva_val_str = str(input("[+_+] Entre le Taux du TVA sur Transport: "))
										try:
											if not tva_val_str:
												print(random.choice(blank_input_respond))
												tva_port_loop = True
											else:
												try:
													global tva_val_float # global declaration for later printing
													global tva_port_result
													global port_ttc_result
													tva_val_float = float(tva_val_str) # convertion
													tva_port_result = port_val_float * tva_val_float / 100	# calculation du tva port
													port_ttc_result = port_val_float + tva_port_result
													print("['_'] Resultat du TVA sur Transport : ", tva_port_result)
													
													# exit the loops
													tva_port_loop = False
													manual_transport_loop = False
													port_loop = False
													big_loop = False
													
												except ValueError:
													print(random.choice(invalid_user_input))
													tva_port_loop = True
												except KeyboardInterrupt:
													print("")
													print(random.choice(keyboard_interrupt))
													exit()
										# handle Error from the second loop
										except ValueError:
											print(random.choice(invalid_user_input))
											tva_port_loop = True
										except KeyboardInterrupt:
											print(random.choice(keyboard_interrupt))
											tva_port_loop = False
											exit()
								#----------
									print("['_'] Resultat du Transoirt + TVA sur Tansport :", port_ttc_result)
									manual_transport_loop = False
						
								# handle error from conversion.
								except ValueError:
									print(random.choice(invalid_user_input))
									manual_transport_loop = True
								except KeyboardInterrupt:
									print(random.choice(keyboard_interrupt))
									exit()
						except KeyboardInterrupt:
							print("")
							print(random.choice(keyboard_interrupt))
							port_loop = False
							exit()
					# FIN DU CALCULATION MANUAL
					
	except KeyboardInterrupt:
		print("")
		print(random.choice(keyboard_interrupt))
		exit()


