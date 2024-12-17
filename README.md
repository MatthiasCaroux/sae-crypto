# SAE-crypto

## Introduction :

Dans le cadre de cette deuxième partie de la SAE, 
nous sommes confrontés à un défi cryptographique imaginé par Alan et Blaise, 
deux membres du "Cercle des cryptographes disparus". 
Leur objectif est de tester nos compétences en cryptographie en nous proposant de déchiffrer des messages contenus dans une trace réseau

Ce rapport documente notre démarche pour analyser la trace réseau, 
identifier le chiffrement utilisé, et finalement accéder aux messages qu’elle contient.

Nous abordons également les erreurs commises par Alan et Blaise dans leur méthode de communication sécurisée, ainsi que les bonnes pratiques qu’ils auraient dû suivre pour protéger efficacement leurs échanges. 

## Analyse de la trace réseau :

Nous avons tout d'abord ouvert la trame de la capture réseau avec Wireshark en prenant le fichier
"trace.pcapng" fourni.
Nous avons ensuite visualisé les paquets de la trame et nous avons remarqué que les paquets étaient chiffrés.
Nous avons donc pris la décision de filtrer les paquets pour en extraire le maximum d'informations de la trame. Ensuite nous avons remarqué que lors de leur échanges, Alan et Blaise,
avaient échangé des messages chiffrés mais également des messages en clair.

## Identification du chiffrement :

### **Analyse des trames réseau et des images fournies**

Lors de l’analyse des données interceptées, plusieurs observations ont été faites :

1. **Messages chiffrés de taille fixe**  
   Les messages chiffrés extraits des trames réseau sont de taille fixe, à savoir **1024 octets**. Ces messages contiennent du binaire. La taille de ces messages, un multiple de 16 octets (128 bits), est cohérente avec l’utilisation d’un algorithme de chiffrement par blocs, comme AES.

2. **Analyse des images fournies**  
   Alan et Blaise ont également fourni des images. Une comparaison des bits de
   ces images a révélé qu’elles étaient **identiques à quelques octets près**.
   Pour se faire, ils avaient utilisé un outil de stéganographie pour cacher des données dans les images, ce qui explique les différences observées.

3. **Indices dans les messages en clair**  
   Après une analyse des messages en clair extraits des données, des indices explicites concernant le chiffrement ont été identifiés. Les termes retrouvés faisaient référence à la **stéganographie** et au **mode CBC (Cipher Block Chaining)**. Cela indique que les données cachées dans les images ont été chiffrées avant d’être intégrées dans les fichiers.

4. **Interprétation des données**

   Pour extraire les données cachées, il est nécessaire de déterminer les octets modifiés et de les analyser, nous avons donc relu les messages chiffrés pour voir si ils ne contenaient pas des informations cachées.
   Ainsi nous avons observé des éléments comme une page HTML, des informations sur le chiffrement utilisé et des informations sur le mode de chiffrement utilisé. Nous avons donc pu déterminer que les messages chiffrés étaient chiffrés en mode CBC avec de la stéganographie. Nous avons donc étudié le mode CBC pour comprendre comment il fonctionne et comment il est utilisé, ainsi que la stéganographie pour comprendre comment les données sont cachées dans les images. Ensuite nous les avons appliqué pour déchiffrer les messages chiffrés et extraire les données cachées dans les images.

    Cette observation suggère qu’elles contiennent des données cachées modifiées de manière subtile. Ce procédé correspond à une technique connue sous le nom de **stéganographie**, qui consiste à dissimuler des informations dans des supports tels que des images ou des fichiers multimédias.



4. **Mode CBC et stéganographie**  
   Le **mode CBC (Cipher Block Chaining)** est un mode de chiffrement par blocs dans lequel chaque bloc chiffré dépend du bloc précédent et d’un vecteur d’initialisation (IV) unique. Cette méthode, combinée à la stéganographie, suggère un double niveau de protection : 
   - Les données sont d'abord **chiffrées** en mode CBC pour sécuriser leur contenu.
   - Elles sont ensuite **intégrées dans les images** via des modifications discrètes, rendant leur détection plus difficile et renforçant la sécurité des échanges entre Alan et Blaise.

Après cette constatation nous avons donc conclu que les images étaient une combinaison de cryptographie et de stéganographie, rendant l’analyse et le déchiffrement complexes.


## Analyse des erreurs commises par Alan et Blaise :

### **Erreurs de sécurité**

1. **Communication en clair**  
   Alan et Blaise ont commis une erreur en communiquant des informations sensibles en clair, telles que des pages HTML et des informations sur le chiffrement utilisé. Les données interceptées nous ont permis de comprendre leur méthode de communication et de déchiffrement, ce qui a facilité notre analyse mais aussi notre compréhension des messages chiffrés.


## Processus de déchiffrement :

### **3.1. Étapes techniques**

#### **Étape 1 : Extraction des données**  

Introduction : Tout d'abord, nous avons remarqué des messages clair bizzares dans les trames réseau notamment des échanges comme " " et " ". Nous avons donc déduit que juste avant cette échange alan avait donc envoyé des données directement dans les trames réseau. Nous avons donc décidé de récupérer ces données pour les analyser.

- **Séparation de l’IV et du message chiffré** :  
  Les trames interceptées qui concerne les messsages ont été analysées pour isoler les 16 premiers octets (128 bits) correspondant au vecteur d’initialisation (IV). Les octets restants dans chaque trame ont été identifiés comme le message chiffré. Pour se faire nous avons identifié lors de notre analyse en mettant les données sous forme brut dans wireshark que les données chiffrées étaient identiques à partir des  . 

- **Analyse de la taille des blocs et vérification de la structure** :  
  Une vérification a été effectuée pour confirmer que la taille des messages chiffrés était un multiple de 16 octets, correspondant à la taille standard des blocs AES. L’alignement des données sur ces blocs suggère l’utilisation d’un remplissage (padding vu dans les données HTML envoyés dans leurs échanges) pour compléter les blocs incomplets.

##### **Étape 2 : Implémentation du déchiffrement**  
- **Présentation du code utilisé pour déchiffrer les messages** :  
  Le déchiffrement a été implémenté en utilisant Python avec la bibliothèque **cryptography**, nous avons utilisé la fonction `Cipher` pour configurer AES-256 en mode CBC. L’IV et la clé secrète ont été fournis comme entrées dans les fontions qui sont implémentées dans la bibliothèque cryptography.

- **Utilisation de cryptography** :  
  La fonction `Cipher` de la bibliothèque cryptography a été utilisée pour configurer AES-256 en mode CBC. L’IV et la clé secrète ont été fournis comme entrées. Nous avons aussi ajouter des conditions dans les clés, IV, et messages pour qu'ils correspondent au format attendu par la fonction `Cipher`.

##### **Étape 3 : Résultat**  
- **Présentation des messages déchiffrés** :  
  Les messages déchiffrés ont été récupérés sous forme de texte en clair. Ces messages ont été extraits des données chiffrées en utilisant la clé secrète et l’IV fournis. Les messages obtenus ont été analysés pour identifier leur contenu et leur signification et nous avons donc repérer d'abord des caractères bizzares et par la suite des chaines de caractères qui forme des mots et des phrases, "Oui on des v" et "Les rois de la c", j'ai donc déduit que les messages étaient "Oui on des voyous/voleurs" et "Les rois de la cryptographie".



