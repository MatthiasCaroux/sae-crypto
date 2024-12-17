# Rapport

## Introduction

Dans le cadre de cette deuxième partie de la SAE, nous sommes confrontés à un défi cryptographique imaginé par Alan et Blaise, deux membres du "Cercle des cryptographes disparus". Leur objectif est de tester nos compétences en cryptographie en nous proposant de déchiffrer des messages contenus dans une trace réseau.

Ce rapport est une trace de nos démarche pour analyser la trace réseau, identifier le chiffrement utilisé, et finalement accéder aux messages qu’elle contient mais surtout des hypothèses sur les messages.

## Objectifs

- Identifier le chiffrement utilisé pour déchiffrer les messages
- Accéder aux messages contenus dans la trace réseau
- Identifier les messages contenus dans la trace réseau

## Sommaire

### Voici le plan que va suivre notre rapport : 

### 1. Introduction
### 2. Analyse de la trace réseau
### 3. Déchiffrement des messages
### 4. Difficultés rencontrées
### 5. Hypothèses
### 6. Conclusion



## 1. Introduction

Comme nous l'avons mentionné précédemment, nous sommes confrontés à un défi cryptographique imaginé par Alan et Blaise, deux membres du "Cercle des cryptographes disparus". Leur objectif est de tester nos compétences en cryptographie en nous proposant de déchiffrer des messages contenus dans une trace réseau fournie par eux.

Nous n'avions qu'a notre disposition une trace réseau contenant des messages chiffrés qu'il nous a fallu ouvrir avec Wireshark pour pouvoir les déchiffrer ainsi que les images fournies par Alan et Blaise.

Premièrement, il nous fallait déterminer ce qu'elle contenait et voir ce que nous pouvions en faire pour l'analyser. 

Ensuite, nous nous sommes aperçus que la trace réseau contenait des messages chiffrés, mais que nous n'avions pas pu les déchiffrer et qu'il nous fallait trouver comment les déchiffrer.

Puis nous avons décidé de nous concentrer sur le chiffrement utilisé pour déchiffrer les messages et de déterminer les messages contenus dans la trace réseau.

Enfin, nous avons, après maintes hypotheses, identifié les messages contenus dans la trace réseau.



## 2. Analyse de la trace réseau

### **2.1. Étude préliminaire des données**

#### **Taille des messages et contenu binaire**  
Dans les messages contenus dans la trame réseau nous nous sommes aperçu qu'il y avait des messages de tailles anormalement élevé **1024 octets** nous nous somme penchées dessus. Il y avait aussi des messages qui contenait en clair des pages HTML qui contenait des informations concernant un mode de chiffrement et un algorithme comme la stéganographie et le CBC qui était utilisé pour cacher des données dans les images.

#### **Analyse des images fournies**  
Ils nous a été fourni par la suite des images dont on savait qu’elles étaient **identiques à quelques octets près**. Cela suggère l’utilisation d’une méthode de **stéganographie**, où des informations sont dissimulées dans des images, probablement dans les octets modifiés. Ces modifications subtiles peuvent être liées à un chiffrement appliqué directement sur les données cachées.

#### **Informations contenues dans les messages**  
Après avoir déchiffré une partie des messages en clair, nous avons identifié des indices sur la méthode de chiffrement utilisée. Notamment, la notion de **stéganographie** a été explicitement mentionnée, confirmant que les données chiffrées sont dissimulées dans des supports comme des images. Cela met en évidence une combinaison de stéganographie et de cryptographie pour protéger les informations dans les messages et les images.

#### **Mode de chiffrement utilisé**  
L'analyse approfondie a révélé que le mode de chiffrement employé est le **CBC (Cipher Block Chaining)**. Ce mode est un standard pour le chiffrement symétrique par blocs, où chaque bloc chiffré dépend du bloc précédent grâce à l’utilisation d’un **vecteur d’initialisation (IV)**. La concaténation de l’IV et du message chiffré dans les trames observées confirme cette hypothèse.

#### **Lien entre stéganographie et CBC**  
Les données semblent avoir été chiffrées en mode **CBC** avant d’être intégrées dans les images via des techniques de **stéganographie**. Cela rend l’analyse plus complexe, car la détection et l’extraction des données cachées nécessitent de manipuler à la fois des outils de stéganographie et de cryptographie.


### **3. Processus de déchiffrement**

#### **3.1. Étapes techniques**

##### **Étape 1 : Extraction des données**  
- **Séparation de l’IV et du message chiffré** :  
  Les trames interceptées ont été analysées pour isoler les 16 premiers octets (128 bits) correspondant au vecteur d’initialisation (IV). Les octets restants dans chaque trame ont été identifiés comme le message chiffré. Cette séparation est essentielle pour effectuer un déchiffrement correct en mode CBC.  

- **Analyse de la taille des blocs et vérification de la structure** :  
  Une vérification a été effectuée pour confirmer que la taille des messages chiffrés était un multiple de 16 octets, correspondant à la taille standard des blocs AES. L’alignement des données sur ces blocs suggère l’utilisation d’un remplissage (padding) pour compléter les blocs incomplets.

##### **Étape 2 : Implémentation du déchiffrement**  
- **Présentation du code utilisé pour déchiffrer les messages** :  
  Le déchiffrement a été implémenté en utilisant Python avec la bibliothèque **cryptography**, une bibliothèque robuste et largement utilisée pour les opérations cryptographiques. Cette bibliothèque offre une interface intuitive pour gérer les algorithmes symétriques comme AES en mode CBC.  

- **Utilisation d'une bibliothèque cryptographique fiable** :  
  La fonction `Cipher` de la bibliothèque cryptography a été utilisée pour configurer AES-256 en mode CBC. L’IV et la clé secrète ont été fournis comme entrées, et le déchiffrement a été effectué en appliquant les transformations inverses sur chaque bloc.  

- **Gestion des éventuels remplissages (padding)** :  
  Le mode CBC nécessite que la taille des données soit un multiple de 16 octets. Si des données de remplissage (padding) sont présentes dans les blocs déchiffrés, elles sont automatiquement supprimées pour obtenir les données en clair originales.

##### **Étape 3 : Résultat**  
- **Présentation des messages déchiffrés** :  
  Les messages déchiffrés ont été récupérés sous forme de texte en clair. Ils contiennent des informations cruciales liées au défi cryptographique, confirmant la validité de la méthode utilisée.  

- **Validation des résultats obtenus** :  
  Les messages obtenus ont été comparés aux hypothèses initiales, et leur contenu a permis de vérifier la cohérence des résultats avec les données analysées. Cette validation a également confirmé la bonne utilisation des clés et de l’IV lors du processus de déchiffrement.


### **4. Limites et défis rencontrés**

#### **Problèmes rencontrés pendant l’analyse et le déchiffrement**  
Au cours du processus d’analyse et de déchiffrement, plusieurs défis ont été identifiés :  
- **Identification précise des données** : La séparation entre l’IV, le message chiffré, et les éventuelles métadonnées n’était pas immédiatement évidente. Les trames contenaient des informations supplémentaires qui ont nécessité une analyse approfondie pour isoler les segments pertinents.  
- **Absence de clé secrète** : Le défi n’incluait pas directement la clé nécessaire pour déchiffrer les messages. Cela a nécessité de formuler des hypothèses basées sur des indices cachés dans les données en clair ou les trames réseau.  
- **Complexité de la stéganographie** : Les données chiffrées étaient intégrées dans des images via des techniques de stéganographie, ajoutant une étape supplémentaire pour les détecter et les extraire correctement.

#### **Hypothèses initiales invalidées ou erreurs détectées**  
- **Structure des données mal interprétée** : Initialement, il avait été supposé que tout le contenu des trames était directement chiffré. Cependant, une partie des octets correspondait à des métadonnées, nécessitant une révision de notre approche.  
- **Erreur dans le padding** : Une erreur a été détectée lors du traitement des données chiffrées contenant des blocs de remplissage (padding). Cela a conduit à des résultats incohérents jusqu’à ce que le problème soit corrigé.

#### **Solutions mises en place pour surmonter ces difficultés**  
- **Analyse approfondie des trames** : Des outils d’analyse réseau tels que Wireshark ont été utilisés pour visualiser la structure des trames et confirmer la séparation entre IV, message chiffré et autres segments.  
- **Recherche de la clé secrète** : La clé a été récupérée en analysant les indices laissés par Alan et Blaise dans les messages en clair ou les métadonnées des images. Des essais systématiques ont également été réalisés pour tester des hypothèses plausibles.  
- **Utilisation d’outils de stéganographie** : Des logiciels spécialisés, comme **StegSolve**, ont été utilisés pour détecter et extraire les données cachées dans les images. Cette étape a permis de récupérer les messages chiffrés de manière fiable.  
- **Gestion correcte du padding** : La bibliothèque cryptographique a été configurée pour gérer automatiquement le remplissage et son retrait lors du déchiffrement, garantissant ainsi l’intégrité des données en clair récupérées.

Ces solutions ont permis de surmonter les principaux défis rencontrés et d’assurer un déchiffrement précis des messages. Cependant, ils soulignent également la complexité du problème posé et l’importance de combiner différentes techniques pour parvenir à un résultat.  


### **5. Analyse critique de la méthode d'Alan et Blaise**

#### **Défaillances identifiées dans leur mise en œuvre**

- **Concaténation de l’IV et du message chiffré** :  Dans la trace réseau, l’IV était directement concaténé au message chiffré sans protection supplémentaire. Bien que courant, cela peut poser problème si l’IV est exposé ou manipulé.

- **Mauvaise gestion de l’IV** : 
   - **Réutilisation potentielle** : Réutiliser le même IV pour plusieurs messages avec une même clé compromet la sécurité, car CBC devient vulnérable à des attaques par texte clair partiel.
   - **IV faible ou prévisible** : Un IV non généré de manière aléatoire ou cryptographiquement sûr permet à un attaquant de deviner des données sous-jacentes.

- **Absence de vérification d’intégrité** : Aucun mécanisme comme un **HMAC (Hash-based Message Authentication Code)** n’a été utilisé pour authentifier les messages. Cela ouvre la porte à des modifications non détectées du contenu chiffré.



#### **Bonnes pratiques qu'ils auraient dû adopter**

- **Génération d’IV aléatoires et sécurisés** : Assurer que chaque IV soit unique et aléatoire pour chaque message chiffré. Cela garantit que deux messages contenant les mêmes données auront des résultats chiffrés différents.

- **Chiffrement authentifié** : Utiliser des modes comme **AES-GCM** ou **AES-CCM**, qui offrent simultanément chiffrement et authentification des données.

- **Mécanismes pour détecter les modifications** : Associer un HMAC ou une signature numérique à chaque message pour détecter toute modification et garantir son authenticité.

- **Séparation stricte entre stéganographie et cryptographie** : Ne pas mélanger ces deux techniques sans précautions. Elles doivent être correctement isolées pour éviter des vulnérabilités.



### **Conclusion**

#### **Résumé des étapes suivies et des résultats obtenus**

- Une analyse de la trace réseau a permis d’identifier et d’isoler l’IV, le message chiffré, et de confirmer l’utilisation du mode CBC.  
- Des données cachées dans des images ont été extraites grâce à des outils de stéganographie.  
- Le déchiffrement, réalisé avec Python et des bibliothèques robustes, a permis de récupérer les messages en clair et de valider les hypothèses formulées.



#### **Importance de sécuriser les communications**

Ce défi souligne l’importance de suivre des pratiques de sécurité rigoureuses :  
- Génération correcte des IV.  
- Utilisation de modes de chiffrement modernes avec authentification.  
- Inclusion d’une couche de vérification d’intégrité des messages.



#### **Leçons tirées et recommandations pour des implémentations futures**

- **Intégration systématique de l’authentification** : Protéger la confidentialité sans garantir l’intégrité des messages affaiblit la sécurité globale.

- **Bonne gestion des clés et des IV** : Une clé bien protégée et des IV robustes sont essentiels pour maintenir la sécurité d’un système.

- **Combinaison prudente de stéganographie et de cryptographie** : Bien que l’idée soit intéressante, elle introduit une complexité qui doit être maîtrisée pour éviter les vulnérabilités.

---

En conclusion, ce défi a permis de mettre en pratique des techniques avancées d’analyse réseau et de cryptographie tout en mettant en évidence des erreurs classiques à éviter. Ces leçons renforcent l’importance des meilleures pratiques en sécurité informatique.
