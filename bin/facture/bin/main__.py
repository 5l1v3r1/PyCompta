
		################################
		# 		The Main program
		################################

# introduction
os.system("clear")
print (logo)

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
if net_comRabais2 > 0:
	# print("use the last result", net_comRabais2,"from 'net_comRabais2'.")
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
if net_comRemis2 > 0:
	# print("use the last result", net_comRemis2,"from 2em remis.")
	last_NC_remis_result = net_comRemis2

elif net_comRemis1 > 0:
	# print("use the last result", net_comRemis1,"from 1er remis.")
	last_NC_remis_result = net_comRemis1

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
# there is only one ristourn so i'll add on other if condition
if net_comRistourn1 > 0:
	# print("use the last result", net_comRistourn1, "from the Ristourn.")
	last_NC_rist_result = net_comRistourn1

elif net_comRemis2 > 0:
	# print("use the last result", net_comRemis2,"from 2em remis.")
	last_NC_rist_result = net_comRemis2

elif net_comRemis1 > 0:
	# print("use the last result", net_comRemis1,"from 1er remis.")
	last_NC_rist_result = net_comRemis1

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

