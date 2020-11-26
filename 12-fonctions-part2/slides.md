%title: PYTHON
%author: xavki
%Site : xavki.blog


# PYTHON : les Fonctions args kwargs


<br>


* "*args" : récupérer un tuple

* exemple :

```
def mafonction(*args):
    liste = []
    for action in args:
        liste.append("{} Xavki !!!".format(action))
    return liste
liste_phrases = mafonction("Salut", "Hello")
print(liste_phrases)
```

---------------------------------------------------------------

# PYTHON : les Fonctions args kwargs


<br>


* "**kwargs" : récupérer un dictionnaire

* exemple :

```
def mafonction(*args, **kwargs):
    liste = []
    for action in args:
        for clef, valeur in kwargs.items():
            liste.append("{} {} {} !!!".format(action, clef, valeur))
    return liste
liste_phrases = mafonction("Salut", "Hello", nom="Xavki", ville="Caen")
print(liste_phrases)
```

