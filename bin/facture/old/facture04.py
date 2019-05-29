# #!/usr/bin/env python3
# Copyright: Med Boutaleb @M3xB0
# contact M3xB0@protonmail.ch


import random
import os
import sys
from numbers import Number

logo = '''
==> i need a logo here <==
'''
notes = '''
-------------
look for a format to limit the output in the float type
-------------
'''
intro = '''
----
-- Coded by : Med Bouraleb | M3xB0
-- Supported: Every device with python3
----
'''



# declaration to handle Global declaration error
# mb
hTax_F = 0
# rabais
rab_float = 0
rab1_val = 0
net_comRabais1 = 0
rab2_float = 0
rab2_val = 0
net_comRabais2 = 0
rab3_float = 0
rab3_val = 0
net_comRabais3 = 0
# Remis
net_comRemis1 = 0
rem1_float = 0
rem1_val = 0
net_comRemis2 = 0
rem2_val = 0
rem2_float = 0
net_comRemis3 = 0
rem3_val = 0
rem3_float = 0
# Ristourn
net_comRistourn1 = 0
rist1_val = 0
rist1_float = 0
# Escompt
escom1_float = 0
escom1_val = 0
netF_Escomp1 = 0
# Port et TVa port
transport_value_float = 0
tva_forfitaire_val_float = 20
tva_forfitaire_result = 0
trans_forfitaire_ttc_result = 0
tva_debour_val_float = 14
tva_debours_result = 0
trans_debours_ttc_result = 0
port_val_float = 0
tva_val_float = 0
tva_port_result = 0
port_ttc_result = 0
# embalage
emb_unit_float = 0
emb_value = 0
emb_prix_unit_float = 0
# tva general
taux_tva_float = 0
tva_general = 0
# net ttc
last_NF_amount = 0
net_ttc = 0

# RESPONDS ARRAY
blank_input_respond = ["vous n'avez rien entré", "rien entré, essayez encore", "vous avez appuyé sur entrée sans rien entrer"]
invalid_user_input = ["ce que vous avez tapé n'est pas un nombre, je ne peux pas calculer autre chose que des nombres", "vous avez tapé autre chose que des chiffres, veuillez réessayer"]
keyboard_interrupt = ["Vous avez appuyé sur CTRL+C .. À plus tard."]


	#########################
	# 0 - Get Montant Brute #
	#########################

def get_mb():
	try:
		mb_looping = True
		while mb_looping:
			user_input_HT_S = str(input("[$_$] Entrez le Montant Brute 'Hors Taxe': "))
			try:
				if not user_input_HT_S:
					print(random.choice(blank_input_respond))
					mb_looping = True
				else:
					try:
						# convert the String to a float
						global hTax_F
						hTax_F = float(user_input_HT_S)
						mb_looping = False

					except ValueError:
						print(random.choice(invalid_user_input))
						mb_looping = True	
			except KeyboardInterrupt:
				print("")			
				print(random.choice(keyboard_interrupt))
				mb_looping = False
	except KeyboardInterrupt:
		print("")
		print(random.choice(keyboard_interrupt))
		exit()


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
							#--------------------------------
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
												#--------------------------------
												# ask the user for the 3th rab
												third_rab_confirm = input("[?_?] Y a-t-il un 3em Rabais? (y/n): ")
												if third_rab_confirm == "y" or third_rab_confirm == "Y":
													rab3_loop = True
													while rab3_loop:
														#print("Entret Votre 2em rabais(%): ")
														rab3_S = str(input("[+_+] Entrez Votre 3em rabais(%): "))														
														try:
															if not rab3_S:
																print(random.choice(blank_input_respond))
																rab3_loop = True
															else:
																try:
																	global net_comRabais3 # Global declaration
																	global rab3_val
																	global rab3_float
																	rab3_float = float(rab3_S) # convert the String to a float
																	rab3_val = net_comRabais2 * rab3_float / 100 # rabais calculation and daclaration
																	net_comRabais3 = net_comRabais2 - rab3_val
																	print("['_'] Resultat Net Commercial après le 3em Rabais et", net_comRabais3)
																	rab3_loop = False
																	rab2_loop = False
																	#---------
																	# i can ask the user for the 3d rabais if i want to
																	# second_rab_respond = input("is there a 3d rabais ?(y/n)")
																	#---------
																except ValueError:
																	print(random.choice(invalid_user_input))
																	rab3_loop = True
														except KeyboardInterrupt:
															print("")
															print(random.choice(keyboard_interrupt))
															rab3_loop = False
															exit()
												# else:
												#	exit_rabais3()
												#--------------------------------
											except ValueError:
												print(random.choice(invalid_user_input))
												rab2_loop = True
									except KeyboardInterrupt:
										print("")
										print(random.choice(keyboard_interrupt))
										rab2_loop = False
										exit()
							# else:
							#	exit_rabais2()
							#--------------------------------

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
											#------------------------------------------------------
												# ask the user for the 3th Remis
												third_rem_confirm = input("[?_?] Y a-t-il un 3em Remise ? (y/n): ")
												if third_rem_confirm == "y" or third_rem_confirm == "Y":
													rem3_loop = True

													while rem3_loop:
														rem3_S = str(input("[+_+] Entrez Votre 3em Remise (%): "))
														try:
															if not rem3_S:
																print(random.choice(blank_input_respond))
																rem3_loop = True
															else:
																try:
																	# convert the String to a float
																	global rem3_float
																	rem3_float = float(rem3_S)
																	# remis calculation and declaration
																	global net_comRemis3 # declaration
																	global rem3_val
																	rem3_val = net_comRemis2 * rem3_float / 100
																	net_comRemis3 = net_comRemis3 - rem3_val
																	print("['_'] Resultat Net Commercial après La 3em Remise et ", net_comRemis3)
																	rem3_loop = False
																#------------------------------------------------------
																	# here i can ask the user for more remises
																#------------------------------------------------------
																except ValueError:
																	print(random.choice(invalid_user_input))
																	rem3_loop = True
														except KeyboardInterrupt:
															print("")
															print(random.choice(keyboard_interrupt))
															rem3_loop = False
												#else:
												#exit_rem3(0)
											#------------------------------------------------------
											except ValueError:
												print(random.choice(invalid_user_input))
												rem2_loop = True
									except KeyboardInterrupt:
										print("")
										print(random.choice(keyboard_interrupt))
										rem2_loop = False
							#else:
							#	exit_rem2(0)
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
		#exit_rem1(0)
			

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
							escom1_loop = False 	# calculate, get of the loop and go to the next pieace of code.
							#------------------------------------------------------
							# here i can ask the user for the second Escompt
							#------------------------------------------------------
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



	###################
	# 5 - Get last NF #
	###################

def get_last_nf():
	global last_NF_result
	
	if netF_Escomp1 > 0:
		# print("use the last result", netF_Escomp1, "from The Escompt.")
		last_NF_result = netF_Escomp1

	elif net_comRistourn1 > 0:
		# print("use the last result", net_comRistourn1, "from the Ristourn.")
		last_NF_result = net_comRistourn1

	elif net_comRemis3 > 0:
		# print("use the last result", net_comRemis2,"from 3em remis.")
		last_NF_result = net_comRemis3

	elif net_comRemis2 > 0:
		# print("use the last result", net_comRemis1,"from 2em remis.")
		last_NF_result = net_comRemis2

	elif net_comRemis1 > 0:
		# print("use the last result", net_comRemis1,"from 1er remis.")
		last_NF_result = net_comRemis1

	elif net_comRabais3 > 0:
		# print("use the last result", net_comRabais3,"from 3em rabais.")
		last_NF_result = net_comRabais3

	elif net_comRabais2 > 0:
		# print("use the last result", net_comRabais2,"from 2em rabais.")
		last_NF_result = net_comRabais2
		
	elif net_comRabais1 > 0:
		# print("use the last result", net_comRabais1,"from 1er rabais.")
		last_NF_result = net_comRabais1
		
	else:
		# print("use the last result", hTax_F,"from 'Montant brut.")
		last_NF_result = last_MB



	#############################
	# 6/7-Get Port and Tva-port #
	#############################

def get_port_and_tva_port():
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
						transport_value = str(input("[+_+] Entrez Le Montant du Transport Forfitaire :  "))
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
								transport_forfitaire_loop = False
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
						transport_value = str(input("[+_+] Entrez Le Montant du Transport Debours :  "))
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
													print("['_'] Resultat du TVA-PORT : ", tva_port_result)
													
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



						
	####################
	# 8 - get Embalage #
	####################
# emb_unit........ = is how many unit of embalage u have
#	emb_prix_unit... = is the price of each unit

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


	#######################
	# 9 - get TVA General #
	#######################

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


	###################
	# 10- get NET TTC #
	###################
	
def get_net_ttc():
	global net_ttc
	net_ttc = last_NF_result + port_val_float + tva_port_result + emb_value + tva_general
	print("['_'] Resultat Net TTC :", net_ttc)



########################
# 11- Print everything #
########################

def print_all():
	global net_ttc
	print(" [-_-] La Facture :")
	print(" ___________________________________")
	print("/-----------------------------------")
	print("| MB                    ", hTax_F)
	print("| Rabais  ", rab_float, 	"%	", rab1_val)
	print("| Rabais2 ", rab2_float,	"%	", rab2_val)
	print("| ----------------------")
	print("| NetC                  ", last_netCom_rab_result)
	print("| Remise1 ", rem1_float,	"%	", rem1_val)
	print("| Remise2 ", rem2_float,	"%	", rem2_val)
	print("| ----------------------")
	print("| NetC                  ", last_NC_remis_result)
	print("| Ristourn", rist1_float,"%	", net_comRistourn1)
	print("| ----------------------")
	print("| NetC                  ", last_NC_rist_result)
	print("| Escompt ", escom1_float ,"%	", escom1_val)
	print("| ----------------------")
	print("| NetF                  ", last_NF_result)
	
	if tva_forfitaire_result > 0 and trans_forfitaire_ttc_result > 0:
		print("| Transport         	", transport_forfitaire_value_float)
		print("| Tva Port 20 %	", last_tva_transport_result)
		
	elif tva_debours_result > 0 and trans_debours_ttc_result > 0:
		print("| Transport         	", transport_debours_value_float)
		print("| Tva Port 14 %	", last_tva_transport_result)
		
	else:
		print("| Transport         	", port_val_float)
		print("| Tva Port", tva_val_float, "%	", last_tva_transport_result)
	
	print("| Embalage          	", emb_value)
	print("| TVA     ", taux_tva_float, 	"%	", tva_general)
	print("| ----------------------")
	print("| Net TTC           	", net_ttc)
	print("|___________________________________")
	print("\-----------------------------------")



		################################
		# 		The Main program
		################################

# introduction
os.system("clear")
print (logo)
print (notes)
print (intro)

# 0
print("             ____________")
print("   ----------| Hors Tax |-----------")
get_mb()

# Passing the results from mb to rabais
last_MB = hTax_F

# 1
print("            ______________")
print("   ---------|  Le Rabais |----------")
get_rabais()

# pass the results from rabais to remis
if net_comRabais3 > 0:
	# print("use the last result", net_comRabai3,"from 'net_comRabais3'.")
	last_netCom_rab_result = net_comRabais3
elif net_comRabais2 > 0:
	# print("use the last result", net_comRabais1,"from 'net_comRabais2'.")
	last_netCom_rab_result = net_comRabais2
elif net_comRabais1 > 0:
	# print("use the last result", net_comRabais1,"from 'net_comRabais1'.")
	last_netCom_rab_result = net_comRabais1
else:
	# print("use the last result", hTax_F,"from 'Montan Brute'.")
	last_netCom_rab_result = last_MB

# 2
print("            _______________")
print("   ---------| Les Remises |----------")
get_remis()

# pass the results from remis to ristourns
if net_comRemis3 > 0:
	# print("use the last result", net_comRemis2,"from 3em remis.")
	last_NC_remis_result = net_comRemis3

elif net_comRemis2 > 0:
	# print("use the last result", net_comRemis1,"from 2em remis.")
	last_NC_remis_result = net_comRemis2

elif net_comRemis1 > 0:
	# print("use the last result", net_comRemis1,"from 1er remis.")
	last_NC_remis_result = net_comRemis1

elif net_comRabais3 > 0:
	# print("use the last result", net_comRabais3,"from 3em rabais.")
	last_NC_remis_result = net_comRabais3

elif net_comRabais2 > 0:
	# print("use the last result", net_comRabais2,"from 2em rabais.")
	last_NC_remis_result = net_comRabais2
	
elif net_comRabais1 > 0:
	# print("use the last result", net_comRabais1,"from 1er rabais.")
	last_NC_remis_result = net_comRabais1
else:
	# print("use the last result", hTax_F,"from 'Montant brut.")
	last_NC_remis_result = last_MB

# 3
print("           _______________")
print("   --------| Le Ristourn |----------")
get_ristourn()

# pass the result Ristourn to Escompt
if net_comRistourn1 > 0:
	# print("use the last result", net_comRistourn1, "from the Ristourn.")
	last_NC_rist_result = net_comRistourn1

elif net_comRemis3 > 0:
	# print("use the last result", net_comRemis2,"from 3em remis.")
	last_NC_rist_result = net_comRemis3

elif net_comRemis2 > 0:
	# print("use the last result", net_comRemis1,"from 2em remis.")
	last_NC_rist_result = net_comRemis2

elif net_comRemis1 > 0:
	# print("use the last result", net_comRemis1,"from 1er remis.")
	last_NC_rist_result = net_comRemis1

elif net_comRabais3 > 0:
	# print("use the last result", net_comRabais3,"from 3em rabais.")
	last_NC_rist_result = net_comRabais3

elif net_comRabais2 > 0:
	# print("use the last result", net_comRabais2,"from 2em rabais.")
	last_NC_rist_result = net_comRabais2
	
elif net_comRabais1 > 0:
	# print("use the last result", net_comRabais1,"from 1er rabais.")
	last_NC_rist_result = net_comRabais1
	
else:
	# print("use the last result", hTax_F,"from 'Montant brut.")
	last_NC_rist_result = last_MB


# 4
print("            _____________")
print("   ---------| L'Escompt |-----------")
get_escompt()

# 5
# pass the result from escompt to the last NET_Financier
get_last_nf()

# 6 / 7 
print("            _____________")
print("   ---------| Transport |-----------")
get_port_and_tva_port()

	# get the last transport result
if tva_forfitaire_result > 0 and trans_forfitaire_ttc_result > 0:
	last_tva_transport_result = tva_forfitaire_result
	last_ttc_transport_result = trans_forfitaire_ttc_result

elif tva_debours_result > 0 and trans_debours_ttc_result > 0:
	last_tva_transport_result = tva_debours_result
	last_ttc_transport_result = trans_debours_ttc_result

else:
	last_tva_transport_result = tva_port_result
	last_ttc_transport_result = port_ttc_result	


# 8
print("            ______________")
print("   ---------| L'embalage |----------")
get_embalage()

# 9
print("           _______________")
print("   --------| TVA-General |----------")
get_tva_general()

# 10
print("          __________________")
print("   -------| Le Net a Payer |---------")
get_net_ttc()

# 11
print("           ______________")
print("   --------| La Facture |----------")
print_all()



