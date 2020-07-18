%title: PYTHON
%author: xavki
%Site : xavki.blog


# PYTHON : Youtube API récupération des commentaires


<br>
Doc1 :https://developers.google.com/youtube/v3/docs/commentThreads
Doc2 : https://developers.google.com/youtube/v3/docs/commentThreads/list

<br>
* petite modification du SCOPES

```
#SCOPES = ['https://www.googleapis.com/auth/youtube.readonly']
SCOPES = ['https://www.googleapis.com/auth/youtube.force-ssl']
```

<br>
* traitement de la récup des commentaires youtube

```
video_id = input("Quel est l'ID de la video ?")
result=get_video_comments(service, part='snippet', videoId=video_id, textFormat='plainText')
print(result)
```

<br>
* récupération des arguments passés à notre fonction (kwargs et service pour authent)

```
def get_video_comments(service, **kwargs):
    comments = []
```

<br>
* passage de la requête à l'API

```
    # request google api
    results = service.commentThreads().list(**kwargs).execute()
```

<br>
* parcourir les résultats et filtre de la collecte

```
    while results:
        # keep comments and authors
        for item in results['items']:
            comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
            author = item['snippet']['topLevelComment']['snippet']['authorDisplayName']
            comments.append([author,comment])
```

<br>
* d'autres pages :

```
        # Check if another page exists
        if 'nextPageToken' in results:
            kwargs['pageToken'] = results['nextPageToken']
            results = service.commentThreads().list(**kwargs).execute()
        else:
            break
```

<br>
* la fonction retourne le résultat

```
    return comments
```
