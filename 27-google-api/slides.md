%title: PYTHON
%author: xavki
%Site : xavki.blog


# PYTHON : Connexion à Google API


<br>


* google api pour youtube

* doc : https://developers.google.com/youtube/v3/guides/auth/client-side-web-apps

* création de credentials : https://console.developers.google.com/apis/

<br>


* librairies : pip install --upgrade google-auth-oauthlib google-auth-httplib2

<br>


1- création des creds
2- modules : 

```
pip3 install click google-auth-oauthlib google-auth-httplib2 google-api-python-client
```

<br>


* import des modules

```
import click, random, csv, os, pickle, time, sys
import google.oauth2.credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from pathlib import Path
```

<br>


* settings des principales variables

```
SCOPES = ['https://www.googleapis.com/auth/youtube.readonly']
API_SERVICE_NAME = 'youtube'
API_VERSION = 'v3'
HOME = str(Path.home())
CACHE_CREDENTIALS_DIR = HOME + "/.ytube/"
CACHE_CREDENTIALS_FILE = CACHE_CREDENTIALS_DIR + "token.pickle"
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
```

<br>


* passage du fichier de creds à la fonction d'authentification

```
service = get_authenticated_service("creds.json")
```

<br>


* création de la fonction

```
def get_authenticated_service(CLIENT_SECRETS_FILE):
    credentials = None
```

<br>


* si le répertoire pour stocker le pickle existe pas on le créé

```
    # check if creds path exist
    if not os.path.exists(CACHE_CREDENTIALS_DIR):
      os.makedirs(CACHE_CREDENTIALS_DIR)
```

<br>


* si le répertoire existe on vérifie si le pickle est présent

```
    # check if creds file exist
    if os.path.exists(CACHE_CREDENTIALS_FILE):
        with open(CACHE_CREDENTIALS_FILE, 'rb') as token:
            credentials = pickle.load(token)
```

<br>


* à partir du pickle on check si les creds sont valides

```
    #  Check if the credentials are invalid or do not exist
    if not credentials or not credentials.valid:
```

<br>


* on check si les credentials on expiré sinon on rafraichit

```
        # Check if the credentials have expired
        if credentials and credentials.expired and credentials.refresh_token:
            credentials.refresh(Request())
```

<br>


* sinon si pas de rafraichissement possible, réauthentification

```
        else:
            # else auth by google
            flow = InstalledAppFlow.from_client_secrets_file(
                CLIENT_SECRETS_FILE, SCOPES)
            credentials = flow.run_console()
```

<br>


* dans tous les cas enregistrement dans le fichiers pickle (si invalid ou pas de creds)
```
        # Save the credentials into the pickle for the next run
        with open(CACHE_CREDENTIALS_FILE, 'wb') as token:
            pickle.dump(credentials, token)
```

<br>


* dans tous les cas on retourne le build avec le passage de 3 variables dont credentials :

```
    return build(API_SERVICE_NAME, API_VERSION, credentials = credentials)
```


