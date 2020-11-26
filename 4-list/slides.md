%title: PYTHON
%author: xavki
%Site : xavki.blog


# PYTHON : Listes


<br>


* instancier une liste

```
liste = []
liste = list()
liste = ["A", "B", "C"]
```

<br>


* principe

```
print(len(liste))
liste[0]
liste[-1]
liste[0:2] # 2 non inclus
liste[0:]
liste[:2]
liste[::-1]
```

-------------------------------------------------

# PYTHON : Listes


<br>


* ajout dans une en fin de liste :

```
liste.append("F")
```

<br>


* insertion

```
liste.insert(1, "Z")
```

<br>


* ajout d'une liste à une autre

```
liste.insert(0, liste2)
liste.extend(liste2)
```

<br>


* suppression

```
liste.remove("A")
```

<br>


* extraction de liste par la fin

```
variable = liste.pop()
```

--------------------------------------------------------


# PYTHON : Listes


<br>


* inverser

```
liste.reverse()
```

<br>


* tri

```
liste.sort()
liste.sort(reverse=True)
liste2 = sorted(liste)
```

<br>


* min/max/sum

```
min = min(liste)
max = max(liste)
sum = sum(liste)
```

<br>


* trouver un index

```
liste.index("A")
```

<br>


* condition

```
print("A" in liste)
```
