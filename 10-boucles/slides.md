%title: PYTHON
%author: xavki
%Site : xavki.blog


# PYTHON : boucle FOR


<br>
* parcourir une liste (focntionne avec les strings) 

```
lettres = ["A", "B", "C", "D"]
for lettre in lettres:
  print(lettre)
```

<br>
* break : sortir de la boucle

```
for lettre in lettres:
  if lettre == "C":
    print("tu sors...")
    break
  print(lettre)
```

<br>
* continue : sauter une itération

```
for lettre in lettres:
  if lettre == "C":
    continue
  print(lettre)
```

----------------------------------------------------------------


# PYTHON : boucle FOR



<br>
* combinaisons de deux listes

```
lettres = ["A", "B", "C", "D"]
chiffres = ["1", "2", "3", "4"]
for lettre in lettres:
  for chiffre in chiffres:
    print(lettre, chiffre)
```

<br>
* range : plage de chiffres

```
for i in range(10):
  print(i)
```

Rq : range(1..10)

--------------------------------------------------------------


# PYTHON : boucle WHILE


<br>
* while = tant que

```
while x < 7 :
  print("Xavki !!!")
```

<br>
* itérer la variable

```
while x < 7 :
  print("Xavki !!!")
  x += 1
```

<br>
* continue/break
```
while x < 7 :
  if x == 5:
    continue
  print("Xavki !!!")
  x += 1
```
