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


