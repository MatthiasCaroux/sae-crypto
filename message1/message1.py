# Message crypté 1

# OQ FQJFQ P'MBBMDQZOQ MZAPUZQ OAZFUQZF X'
# UZPUHGXSMNXQ EQODQF PQ OQFFQ
# ZAGHQXXQ QZUSYQ. EQDQL-HAGE OQXGU AG OQXXQ
# CGU FDAGHQDM XM OXQ?

message_crypté_1 = "OQ FQJFQ P'MBBMDQZOQ MZAPUZQ OAZFUQZF X'\nUZPUHGXSMNXQ EQODQF PQ OQFFQ\nZAGHQXXQ QZUSYQ. EQDQL-HAGE OQXGU AG OQXXQ\nCGU FDAGHQDM XM OXQ?"
def dechiffrement_de_cesar(message_crypté, décalage):
    message_décrypté = ''
    for lettre in message_crypté:
        if lettre.isalpha():
            lettre_decalée = chr((ord(lettre) - décalage - ord('A')) % 26 + ord('A'))
            message_décrypté += lettre_decalée
        else:
            message_décrypté += lettre
    return message_décrypté
            


message_decrypte1 = dechiffrement_de_cesar(message_crypté_1, 12)



def trouve_clef(le_message_decrypte):
    clef = ''
    msg_final=le_message_decrypte.split('\n')
    for ligne in msg_final:
        clef += ligne[0]
    return clef

print(trouve_clef(message_decrypte1))
