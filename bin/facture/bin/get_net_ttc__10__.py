###################
# real variable but not real value - just for testing pupus
###################
# montant brut
hTax_F = 123456789

# rabais 1 et 2
rab_float = 10.0 # %
rab1_val = 123456
rab2_float = 10.0 # %
rab2_val = 123456

last_netCom_rab_result = 123456789

# remis 1 et 2
rem1_float = 10.0 # %
rem1_val = 123456
rem2_float = 10.0 # %
rem2_val = 123456

last_NC_remis_result = 123456789

# Ristourn
rist1_float = 10.0 # %
rist1_val = 123456

net_comRistourn1 = 123456789
last_NC_rist_result = 123456789

# escompt
escom1_float = 10.0 # %
escom1_val = 123456

# net financier
last_NF_result = 123456789

# tvaport only 
tva_val_float = 10.0 # %
tva_port_result = 123456

# port+TVA result
port_val_float = 123456789

# embalage
emb_value = 123456789
# tva general
taux_tva_float = 10.0
tva_general = 123456789



	###################
	# 10- get NET TTC #
	###################
	
def get_net_ttc():
	global net_ttc
	net_ttc = last_NF_result + port_val_float + tva_port_result + emb_value + tva_general
	print("['_'] Resultat Net TTC :", net_ttc)


get_net_ttc()

