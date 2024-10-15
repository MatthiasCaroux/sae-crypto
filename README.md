# Rapport de Projet : SAE Cryptographie - Partie 1
## Le cercle des cryptographes disparus

### Membres du groupe
- Niveau Samuel
- Familiar-Marais Enzo
- Lima Romain
- Caroux Matthias


## 1. Introduction

Dans le cadre de la SAE "Le cercle des cryptographes disparus", nous avons été mis au défi de déchiffrer trois messages cryptés. Chaque message décodé fournit un indice pour le suivant, et le but est de concevoir un programme Python capable de décrypter ces messages en utilisant différentes méthodes vues en cours ou découvertes au fil du projet. 


## 2. Objectifs du Projet

- Déchiffrer les trois messages secrets
- Identifier les méthodes de chiffrement utilisées
- Développer un programme en Python pour le déchiffrement
- Documenter les messages et les techniques dans ce rapport

---

## 3. Méthodes de Chiffrement Utilisées

### 3.1 Premier Message
- **Message chiffré** : 
```
OQ FQJFQ P'MBBMDQZOQ MZAPUZQ OAZFUQZF X'
UZPUHGXSMNXQ EQODQF PQ OQFFQ
ZAGHQXXQ QZUSYQ. EQDQL-HAGE OQXGU AG OQXXQ
CGU FDAGHQDM XM OXQ?
```
- **Méthode de chiffrement** : Chiffrement de César le code est ici : `message1/message1.py`
- **Message déchiffré** : 
```
CE TEXTE D'APPARENCE ANODINE CONTIENT L'
INDIVULGABLE SECRET DE CETTE
NOUVELLE ENIGME. SEREZ-VOUS CELUI OU CELLE
QUI TROUVERA LA CLE?
```

### 3.2 Deuxième Message
- **Message chiffré** : 
```
UCVLGH YUU BEQEMF TG ORETORI RIVDXQA
QLNO82OP9CK1WU0SCY3SWR74SBDUHNB5JT6O
KEORBB
```
- **Méthode de chiffrement** : Chiffrement de Vigenère le code est ici : `message2/message2.py`
- **Message déchiffré** :
```
SUIVEZ LES TRACES DE GEORGES PAINVIN
AJFB82YN9UX1GS0KPI3QOE74CZVHRLT5WD6M
CRYPTO
```

### 3.3 Troisième Message
- **Message chiffré** : 
```
AFXFFG XADXGFV GDFDVVVVDAFX-FVDXXFAGFAGVF XGDDGAXXADFDV GFGVVDXDVFGXF FX
VD GGGDVVXG GV VVGGGGV GAAF GVVXAVGFGG XDDFAVAF.AGGVXDG
F VGVXVGGD
VFXXFXAXDFAGGDAVG VGGG VVAXDGAGVVAGXAGFGXADGDVG:GXFXVFXDVFXDGGVGXDFG GGF V X VVGGGGD
XVAGVAVVGDFFGGXGVAG!DAGFX AFDAGFFFVAAAGGAGXVFFG!FX G DGDAG 4XDG
```
- **Méthode de chiffrement** : Chiffrement de ___ le code est ici : `message3/message3.py`
- **Message déchiffré** : [Message déchiffré ici]

---

## 4. Implémentation Python

### 4.1 Structure du programme
Décrire brièvement l'architecture du programme, les fonctions principales, et comment il fonctionne pour déchiffrer les messages.

### 4.2 Exemples de code
Inclure des extraits de code pertinents pour chaque méthode de déchiffrement.

---

## 5. Conclusion

Résumé du projet, des défis rencontrés, des solutions apportées, et des enseignements tirés.

---

## 6. Références

Lister les sources, cours ou documents utilisés pour le projet.

