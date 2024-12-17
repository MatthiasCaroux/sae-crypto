from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

def decrypt_aes_cbc(iv: bytes, key: bytes, ciphertext: bytes) -> bytes:
    """Cette fonction permet de déchiffrer un message chiffré en mode AES-CBC-256.

    Args:
        iv (bytes):  Vecteur d'initialisation de 16 octets.
        key (bytes):  Clé de déchiffrement de 32 octets.
        ciphertext (bytes):  Message chiffré (taille multiple de 16).

    Returns:
        bytes:  Message déchiffré (bytes).
    """
    if len(iv) != 16 or len(key) != 32 or len(ciphertext) % 16 != 0:
        raise ValueError("L'IV ou  la clé ou le message chiffré ne sont pas valides.")

    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend()) # création de la clé de chiffrement
    decryptor = cipher.decryptor() # création du déchiffreur
    plaintext = decryptor.update(ciphertext) + decryptor.finalize() # déchiffrement du message
    # fonction fournit par la bibliothèque cryptography et dont l'utilisation est décrite dans la documentation
    # nous avons trouvé ce code sur un forum
    return plaintext

def bitstring_to_bytes(string: str) -> bytes:
    """Cette fonction permet de convertir une chaîne de bits en octets.

    Args:
        string (str):  Chaîne de bits.

    Returns:
        bytes:  Octets.
    """
    return int(string, 2).to_bytes((len(string) + 7) // 8, byteorder='big')


def binaire_texte(binaire):
    """Permet de traduire plusieurs octets codés en binaire en texte en ASCII, en ne gardant que les lettres de l'alphabet 
    (majuscules et minuscules) et les chiffres.
    Args:
        binaire (str): binaire
    Returns:
        str: des lettres et de chiffres
    """
    txt = ""
    i = 0
    avant = ""
    while i < len(binaire):
        octet = ""
        for num in range(i, i + 8):
            octet += binaire[num]
        i = i + 8
        char = chr(int(octet, 2))  # Converti en caractère, le binaire
        
        if char.isalpha() or char.isdigit(): # seulement les caractères de l'alphabet ou des chiffres
            txt += char
        
        if avant == " " and char == " ": # si deux espaces consécutifs sont détectés alors arrêter
            return txt
        avant = char

    return txt


# clé trouver dans la première trames des envois
cles1 = "0001110001011011011000000110010111110011110010101101000010010110000000000101101110101100001111111100000000000100101111101110110100001000000101010100000111110000111100000011111100000111010001100100111100110011110010011100000101010101110001001111110011010100110000111000101011100100110110011100110110110110011110011101100111101000000101011110011001101111000000101000000011111001101000110010010100000110101100111111100111000100111111010100111110001000011001101101101100110101100111001001111111100000110000011001111011100111111101100111010101100111101100001111000000010110110111101101111000101111111100000000100010011111111100110000100000110100000100000000010010001111010000110010001101000101100101010000011000100001000010111001001110100111111001101110101111011110011001100010001110011001111000101110011010000001111000010011001110000011000010010100100110110010010010111011110000111011011001001011001010111000111011001110110101001101101011101010110011000111110100000010010010111101100100010100110111100110110011100011000111011010"
cles2 = "0111110000010100111010011010110000100110101011111100100111001110111101001011000000100100000001100001010001010000001011000101010100001110101001000000010011101101110000011111101001001001011111100001000100011110100101111110010101100011001000011110100110111011110001110100001111000111001010111111010001000110000011100011001101011011110110010010001100110000111111101110011010110110011100100110100000000110101001101011000101101001001111101011011011111100010110001101111100001010001010011111000111001110100010111000101111011111010100010111101010100010111100001100011010111000001000000001000101111001111111011100110110101001000110010110001010000100101101011110100011000001011100111110111011000000101000100001111111110100011100000101011110001001010110110001010011100010100110010110101100010011100101100101111011111011101010010111111101110000001010001010101000111000000010100101000110000001100100000101010110011110000001101100100000001100011100101000011010000010100101100011111111110001111000100000001100110000011010110011011000000010"
#c'est mes clés de 1024 à diviser tout les 32 octets

IV1 = "ff9c793cff662dbbbaf912fa41f4f2fb" 
#c'est mon IV

IV2 = "d89cac6d4033722ac7328dab0a96cf96" 
#c'est mon IV aussi 

message1 = "236a4a979c9d931c97c93837786daeb23be5907b56d62a31d524c312a59675ef"
message2 = "0e36b7e4d0845176e563c49134a123a9d44f7379fc9ef545a1c93b1d174a92dc"
message3 = "49c0e23c45ef1b7c41783a3e0e3be716507c98421c696e19555c99a1452f795f"
message4 = "8ab705f9605526c62ccd848e6501b6fda4c532ee84514dc087967be0b8acb5e7"
# mes messages cryptés sans les IV qui sont les 16 derniers caractères du message

cles_brutes = cles1
keys = [bitstring_to_bytes(cles_brutes[i:i+256]) for i in range(0, len(cles_brutes), 256)]
lesmessages = [message1, message2, message3, message4]


for i in range(len(lesmessages)):
    for j in range(len(lesmessages)): # on teste tous les messages avec tous les autres
        cles = lesmessages[i] + lesmessages[j]
        ciphertext = bytes.fromhex(cles) # on convertit le message en binaire
        cipherlist = [ciphertext[i:i+16] for i in range(0, len(ciphertext), 16)] # on découpe le message en 16 octets
        cipherlist[0] = cipherlist[2] # on change le premier octet
        cipherlist[2] = cipherlist[0] # on change le troisième octet
        for key in keys: # on teste toutes les clés
            message = decrypt_aes_cbc(IV1, key, b"".join(cipherlist)) # on déchiffre le message
            print(message.decode('utf-8', errors='ignore')) # on affiche le message
    print("")


# une fois le message déchiffré on regarde dans le resultat si il y a des lettres ou des chiffres et on observe
# deux messages qui ont des lettres et des chiffres et qui forment une phrase
# "Oui on est v" et "Les rois de la c"
