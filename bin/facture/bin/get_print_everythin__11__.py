

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
	print("| Transport         	", port_val_float)
	print("| Tva Port", tva_val_float, "%	", tva_port_result)
	print("| Embalage          	", emb_value)
	print("| TVA     ", taux_tva_float, 	"%	", tva_general)
	print("| ----------------------")
	print("| Net TTC           	", net_ttc)
	print("|___________________________________")
	print("\-----------------------------------")


