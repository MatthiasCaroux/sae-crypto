# Données de l'exercice
clef = 'AJFB82YN9UX1GS0KPI3QOE74CZVHRLT5WD6M'
message = 'AFXFFG XADXGFV GDFDVVVVDAFX-FVDXXFAGFAGVF XGDDGAXXADFDV GFGVVDXDVFGXF FX VD GGGDVVXG GV VVGGGGV GAAF GVVXAVGFGG XDDFAVAF.AGGVXDG F VGVXVGGD VFXXFXAXDFAGGDAVG VGGG VVAXDGAGVVAGXAGFGXADGDVG:GXFXVFXDVFXDGGVGXDFG GGF V X VVGGGGD XVAGVAVVGDFFGGXGVAG!DAGFX AFDAGFFFVAAAGGAGXVFFG!FX G DGDAG 4XDG'
cle = 'CRYPTO'


def creer_dictionnaire_adfgvx(cle):
    """Cette fonction permet de créer un dictionnaire de substitution pour le chiffrement de ADFGVX et donc de remplir le tableau de substitution"""
    lettres_adfgvx = ['A', 'D', 'F', 'G', 'V', 'X']
    dico_substitution = {}

    for i in range(6):
        for j in range(6):
            lettre = cle[i*6 + j] # le tableau est en 6x6 donc on prend la lettre correspondante
            dico_substitution[lettres_adfgvx[i] + lettres_adfgvx[j]] = lettre
    return dico_substitution

def decrypt(message, clef,cle):
    """Cette fonction permet de déchiffrer un message chiffré avec la méthode de ADFGVX

    Args:
        message (String): le message que nous souhaitons déchiffrer qui doit etre chiffrer avec la méthode de ADFGVX
        clef (String): la clef de substitution pour déchiffrer le message
        cle (String): la clef pour déchiffrer le message = "CRYPTO"

    Returns:
        String : Message déchiffré
    """

    hauteur = len(message) // len(cle)
    # Trier la clé alphabétiquement pour l'ordre des colonnes
    cle_trier = ''.join(sorted(cle))
    dico_cle_trier = {}


    for i in range(len(cle_trier)):
        dico_cle_trier[cle_trier[i]] = message[i*hauteur:(i+1)*hauteur]


    print('')
    dico_cle = {"C": None, "R": None, "Y": None, "P": None, "T": None, "O": None}

    # Remettre les segments dans les colonnes selon l'ordre de la clé initiale
    for i in range(len(cle)):
        if cle[i] in dico_cle:
            dico_cle[cle[i]] = dico_cle_trier[cle[i]]


    dico_substitution = creer_dictionnaire_adfgvx(clef)

    
    reponse = ''
    message_dechiffre = ''
    for i in range(hauteur):
        for j in range(len(cle)):
            char = dico_cle[cle[j]][i]
            if char.isalpha():         # Si le caractère est une lettre, l'ajouter à la paire
                reponse += char
                print(f"Intermédiaire: {reponse}, longueur: {len(reponse)}")

                if len(reponse) == 2:             # Dès que la paire est complète, la déchiffrer
                    if reponse in dico_substitution:
                        message_dechiffre += dico_substitution[reponse]
                        print(f"Déchiffré: {dico_substitution[reponse]}")
                    else:
                        print(f"Erreur: la paire '{reponse}' n'a pas de correspondance.")
                    reponse = ''  # Réinitialiser pour la prochaine paire
            else:             # Si le caractère n'est pas une lettre, l'ajouter directement au message
                message_dechiffre += char 
                print(f"Intermédiaire: {reponse}, longueur: {len(reponse)}")
                if len(reponse) == 2 and reponse in dico_substitution: 
                    
                    # Si une paire est en cours et complète, la déchiffrer avant de continuer
                    message_dechiffre += dico_substitution[reponse]
                    print(f"Déchiffré: {dico_substitution[reponse]}")
                    reponse = ''

    print('')
    print('')
        
    return message_dechiffre

print(creer_dictionnaire_adfgvx(clef))
print(decrypt(message,clef, cle))



