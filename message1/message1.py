# Message crypté 1

# OQ FQJFQ P'MBBMDQZOQ MZAPUZQ OAZFUQZF X'
# UZPUHGXSMNXQ EQODQF PQ OQFFQ
# ZAGHQXXQ QZUSYQ. EQDQL-HAGE OQXGU AG OQXXQ
# CGU FDAGHQDM XM OXQ?

message_crypté_1 = "OQ FQJF Q P'MBBMDQZOQ MZAPUZQ OAZFUQZF X'UZPUHGXSMNXQ EQODQF PQ OQFFQ ZAGHQXXQ QZUSYQ. EQDQL-HAGE OQXGU AG OQXXQ CGU FDAGHQDM XM OXQ?"


def dechiffrement_de_cesar(message_crypté, décalage):
    message_décrypté = ''
    for lettre in message_crypté:
        if lettre.isalpha():
            lettre_decalée = chr((ord(lettre) - décalage - ord('A')) % 26 + ord('A'))
            message_décrypté += lettre_decalée
        else:
            message_décrypté += lettre
    return message_décrypté
            



print(dechiffrement_de_cesar(message_crypté_1, 12))