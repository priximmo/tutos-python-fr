%title: PYTHON
%author: xavki
%Site : xavki.blog


# PYTHON : Dictionnaires


<br>
* définition comme les Sets : {}

* principe de clefs valeurs

```
dictionnaire = { "clef1": "valeur1", "clef2": "valeur2"}
dictionnaire = { "clef1": "valeur1", "maliste": ["valeur1", "valeur2", "valeur3"]}
```

<br>
* interrogation

```
dictionnaire["clef1"]
```

* meilleur des valeurs non existantes

```
dictionnaire.get("clef1")
```

----------------------------------------------------------------------------------------

# PYTHON : Dictionnaires



<br>
* modification

```
dictionnaire[clef2] = "mavaleur2"
dictionnaire.update({"clef1": "nllevaleur1", "clef2": "nllevaleur2")
```

<br>
* suppression

```
del dictionnaire["clef2"]
```

<br>
* suppression avec utilsation

```
valeur1 = dictionnaire.pop("clef1")
```

<br>
* autres

```
len(dictionnaire)
dictionnaire.keys()
dictionnaire.values()
dictionnaire.items()
```

<br>
* boucle sur clefs / valeurs

```
for clef,valeur in dictionnaire.items():
  print(clef, valeur)
```
