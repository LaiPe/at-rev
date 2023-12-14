# AT-REV (Aide à la Traduction pour REV)
**AT-REV** est une solution logicielle apportant une aide à l'utilisateur lors du processus de sous-titrage d'une vidéo. 
Cette aide se place dans le contexte d'un travail réalisé pour  la plateforme REV. Ainsi, afin de fonctionner correctement, cette aide nécessite l'apport d'une transcription présentée dans un format bien particulier qui sera détaillé plus bas.

Afin de faciliter le travail de l'utilisateur, AT-REV propose une traduction automatique se basant sur l'IA de traduction de [Google Cloud](https://cloud.google.com/translate?hl=fr). Il est donc nécessaire pour l'utilisateur de créer ou de posséder un compte Google Cloud ainsi que d'activer dans son espace personnel l'API de Google Cloud Translation. Vous trouverez ci-dessous des informations quant à l'authentification de l'utilisateur à son compte Google Cloud afin d'utiliser AT-REV.  

**Cette aide ne constitue à aucun moment une automatisation complète du travail de sous-titrage.** Ainsi, l'utilisateur reste **responsable** quant à l'usage qu'il fait de cette aide et donc de la qualité finale de son travail.
Cette aide a pour objectif une augmentation de la productivité du travailleur ainsi qu'une réduction des erreurs involontaires comme les fautes de frappes par exemple.

Vous trouverez ici l'ensemble des informations relatives à l'**installation** du logiciel, à son **utilisation** ainsi que **quelques conseils** supplémentaires.  

## Installation
1. Installez [Python](https://www.python.org/downloads/) en fonction de votre système d'exploitation.
2. Téléchargez puis décompressez l'archive contenant AT-REV et placer le dossier extrait dans le répertoire de votre choix.
3. Ouvrez un Bash/Powershell (en fonction de votre OS) dans ce répertoire et définissez un nouvel environnement de travail avec `venv`:
	 ```
	 python -m venv env
	 ```
4. Activez votre environnement :
	```
	.\env\Scripts\Activate
	```
	> Si vous êtes sur Windows, assurez-vous que l'exécution de scripts PowerShell est autorisée. [*(plus d'informations)*](https://learn.microsoft.com/fr-fr/powershell/module/microsoft.powershell.security/set-executionpolicy?view=powershell-7.4)
5. Téléchargez l'ensemble des dépendances :
	```
	pip install -r requirements.txt
	```
6. Connexion à votre compte Google Cloud :
	- Téléchargez et installez l'outil d’authentification [gcloud CLI](https://cloud.google.com/sdk/docs/install?hl=fr)
	- Ouvrez gcloud CLI et authentifiez vous avec vos identifiants de compte Google Cloud :
		```
		gcloud auth application-default login
		```


>Crée par [Léo Peyronnet](https://github.com/LaiPe)

