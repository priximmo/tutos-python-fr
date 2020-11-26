%title: PYTHON
%author: xavki
%Site : xavki.blog


# PYTHON : Listes complément


<br>


* parcourir une liste

```
for lettre in lettres:
  print(lettre)
```

<br>


* plus de précision

```
for index, valeur in enumerate(lettres):
  print(index, valeur)
```

<br>


* ou plus

```
for index, valeur in enumerate(lettres, start=2):
  print(index, valeur)
```

--------------------------------------------------------

# PYTHON : Listes complément


<br>


* jointure

```
jointure = ", ".join(lettres)
```

<br>


* découper pour créer une list

```
liste = jointure.split(",")
```


