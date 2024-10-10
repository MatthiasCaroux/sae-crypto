# Message chiffré num 2
# UCVLGH YUU BEQEMF TG ORETORI RIVDXQA
# QLNO82OP9CK1WU0SCY3SWR74SBDUHNB5JT6O
# KEORBB

message_crypte2 = "UCVLGH YUU BEQEMF TG ORETORI RIVDXQA QLNO82OP9CK1WU0SCY3SWR74SBDUHNB5JT6O KEORBB"
cle = "CINQ"



def dechiffrement_de_vignere(message, cle):
    """Cette fonction permet de dechiffrer un mesaage chiffré avec la méthode de Vigenère

    Args:
        message (string): message que nous souhaitons dechiffrer
        cle (String): cle pour dechiffrer le message

    Returns:
        String: message dechiffré avec la méthode de Vigenère
    """
    message_dechiffre = ''
    cle_allongee = ''
    index_cle = 0
    # On parcourt le message et on ajoute chaque lettre au cle allongé
    for lettre in message:
        # on ne prend que les lettres
        if lettre.isalpha():
            cle_allongee += cle[index_cle % len(cle)]
            index_cle += 1
        else:
            cle_allongee += lettre

    # Ensuite on déchiffre le message avec la méthode de Vigenère
    for i, lettre in enumerate(message):
        if lettre.isalpha():
            lettre_decalee = chr(((ord(lettre) - ord(cle_allongee[i]) + 26) % 26) + ord('A')) # On prend le Unicode de chaque lettre du message et on le décale avec la lettre correspondante de la clé
            # puis on ajoute 26 pour éviter les valeurs négatives et on prend le modulo 26 pour éviter les valeurs supérieures à 26 
            # enfin on ajoute le Unicode de 'A' pour avoir la lettre correspondante
            message_dechiffre += lettre_decalee
        else:
            message_dechiffre += lettre  # Si ce n'est pas une lettre, on garde le caractère inchangé

    return message_dechiffre

print(dechiffrement_de_vignere(message_crypte2, cle))





# Message déchiffré num 2
# SUIVEZ LES TRACES DE GEORGES PAINVIN
# AJFB82YN9UX1GS0KPI3QOE74CZVHRLT5WD6M
# CRYPTO