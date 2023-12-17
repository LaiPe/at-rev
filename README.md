# AT-REV (Aide à la Traduction pour REV)

**AT-REV** est une solution logicielle apportant une aide à l'utilisateur lors du travail de <u>sous-titrage</u> d'une vidéo.

Cette aide se place dans le contexte d'un travail réalisé pour la plateforme REV. Ainsi, afin de fonctionner correctement, cette aide nécessite l'apport d'une transcription présentée dans un format bien particulier qui sera détaillé plus bas.

  

Afin de faciliter le travail de l'utilisateur, AT-REV propose une traduction automatique se basant sur l'IA de traduction de [Google Cloud](https://cloud.google.com/translate?hl=fr). Il est donc nécessaire pour l'utilisateur de créer ou de posséder un compte Google Cloud ainsi que d'activer dans son espace personnel l'API de Google Cloud Translation. Vous trouverez ci-dessous des informations quant à l'authentification de l'utilisateur à son compte Google Cloud afin d'utiliser AT-REV.

  

**Cette aide ne constitue à aucun moment une automatisation complète du travail de sous-titrage.** Ainsi, l'utilisateur reste **responsable** quant à l'usage qu'il fait de cette aide et donc de la qualité finale de son travail.

Cette aide a pour objectif une augmentation de la productivité du travailleur ainsi qu'une réduction des erreurs involontaires comme les fautes de frappes par exemple.

  

Vous trouverez ici l'ensemble des informations relatives à l'**installation** du logiciel ainsi qu'à son **utilisation**.

  

## Installation

  

1. Installez [Python](https://www.python.org/downloads/) en fonction de votre système d'exploitation.

2. Téléchargez puis décompressez l'archive contenant AT-REV et placer le dossier extrait dans le répertoire de votre choix.

3. Activez l'API Google Cloud Translation depuis votre compte [Google Cloud](https://cloud.google.com/?hl=fr).

  

### Linux

4. Ouvrez un terminal Shell Bash dans ce répertoire et installez l'utilitaire `venv`:

	 ```
	 sudo apt install python<version>-venv
	 ```

	> Prenez bien soin de remplacez `<version>` par la version réelle de votre installation Python. Utilisez `python3 --version` pour la connaître.

5. Définissez un nouvel environnement de travail:

	 ```
	 python3 -m venv env
	 ```

6. Activez votre environnement :

	 ```
	 source ./env/bin/activate
	 ```

	> Si l’exécution vous est refusée, pensez à vous accorder les droits d’exécution avec `chmod +x ./env/bin/activate`.

7. Téléchargez l'ensemble des dépendances :
	
	 ```
	 pip install -r requirements.txt
	 ```

8. Authentifiez-vous à votre compte Google Cloud en suivant les instructions fournies [ici](https://cloud.google.com/sdk/docs/install?hl=fr)

	> Pensez à bien choisir votre projet Google Cloud correspondant à votre usage de AT-REV pour lequel vous avez activé l'API Google Cloud Translation.

### Windows

4. Ouvrez un terminal PowerShell dans ce répertoire et définissez un nouvel environnement de travail avec `venv`:

	 ```
	 python -m venv env
	 ```

5. Activez votre environnement :

	 ```
	 .\env\Scripts\Activate
	 ```

	> Si l’exécution vous est refusée, assurez-vous que l'exécution de scripts PowerShell soit autorisée. [*(plus d'informations)*](https://learn.microsoft.com/fr-fr/powershell/module/microsoft.powershell.security/set-executionpolicy?view=powershell-7.4)

6. Téléchargez l'ensemble des dépendances :

	 ```
	 pip install -r requirements.txt
	 ```

7. Authentifiez-vous à votre compte Google Cloud en suivant les instructions fournies [ici](https://cloud.google.com/sdk/docs/install?hl=fr)
	
	> Pensez à bien choisir votre projet Google Cloud correspondant à votre usage de AT-REV pour lequel vous avez activé l'API Google Cloud Translation.

  

## Utilisation

Afin de pouvoir être utilisé, AT-REV a besoin d'un fichier d'entrée contenant la transcription fournie par REV lors de la réclamation d'une mission de sous-titrage.

### Extraction de la transcription

1. Connectez-vous à votre espace travailleur sur REV.

2. Accédez à la page *Projet* de votre travail en cours.

3. Dans l'encart *Ressources* de cette page, cliquez sur le lien finissant par `.srt`.

4. Vérifiez que la page ouverte contienne bien la transcription **dans la langue d'origine**.

5. Enregistrez cette page avec votre navigateur. (`Ctrl + S`)

  

Un fichier avec pour extension `.htm` devrait alors être téléchargé par votre navigateur. Il est normalement également accompagné d'un fichier qui ne sera pas utile dans notre cas.

Pour plus de clarté dans votre travail, nous vous recommandons de **renommer** le fichier `.htm` avec le nom de votre choix puis de **supprimer** le dossier qui lui était associé.

  

### Premiers pas

1. Placez votre fichier `.htm` contenant la transcription dans le répertoire contenant les fichiers d'AT-REV.

2. Ouvrez un Bash/Powershell (en fonction de votre OS) dans ce répertoire et activez votre environnement comme vu dans l’**installation**.

3. Enfin, lancez AT-REV avec cette commande :

	 ```
	 python at-rev.py transcription.htm -c output.txt
	 ```

	> Prenez bien soin de remplacez `transcription.htm` par le nom réel de votre fichier de transcription.

  

Une fois le processus d'AT-REV terminé, vous pouvez ouvrir avec l'outil de traitement de texte de votre choix le fichier généré `output.txt`.

  

Pour plus d'informations sur les options que propose AT-REV, n’hésitez pas à consulter l'aide associé au programme avec la commande :
  
  ```
  python at-rev.py -h
  ```
