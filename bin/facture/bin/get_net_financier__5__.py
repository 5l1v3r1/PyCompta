# testing variables
netF_Escomp1 = 0
net_comRistourn1 = 0
net_comRemis2 = 0
net_comRemis1 = 343
net_comRabais2 = 0
net_comRabais1 = 15


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

	elif net_comRemis2 > 0:
		# print("use the last result", net_comRemis2,"from 2em remis.")
		last_NF_result = net_comRemis2

	elif net_comRemis1 > 0:
		# print("use the last result", net_comRemis1,"from 1er remis.")
		last_NF_result = net_comRemis1

	elif net_comRabais2 > 0:
		# print("use the last result", net_comRabais2,"from 2em rabais.")
		last_NF_result = net_comRabais2
		
	elif net_comRabais1 > 0:
		# print("use the last result", net_comRabais1,"from 1er rabais.")
		last_NF_result = net_comRabais1
	else:
		# print("use the last result", hTax_F,"from 'Montant brut.")
		last_NF_result = hTax_F

		
# testing purpuses
get_last_net_financier()
print("Last amount used is", last_NF_result)

