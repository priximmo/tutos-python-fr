%title: PYTHON
%author: xavki
%Site : xavki.blog


# PYTHON : List Comprehension

<br>


* oneliners

* simplifaction de la constitution de listes

* plus difficile aux débutants

<br>


* liste simple

```
maliste = [1,2,3,4,5,6,7,8,9]
maliste = [i for i in range(10)]
```

---------------------------------------------------------------------------


# PYTHON : List Comprehension



<br>


* introduire du calcul

```
maliste = [1,2,3,4,5,6,7,8,9]
maliste10 = []
for i in maliste:
  maliste10.append(i*10)
```

<br>


* et sinon ...

```
maliste = [i for i in range(10)]
```

-------------------------------------------------------------------------


# PYTHON : List Comprehension



<br>


* conditions :

```
maliste = [1,2,3,4,5,6,7,8,9]
malistepaire = []
for i in maliste:
  if i%2 == 0:
  malistepaire.append(i)
```

<br>


* et sinon ...

```
maliste = [i for i in range(10) if i%2 == 0]
```


-------------------------------------------------------------------------


# PYTHON : List Comprehension



<br>


* les listes de listes

```
maliste1 = [1,2,3,4,5,]
malisteA = ["A", "B", "C"]
malistefinale = []
for i in maliste1:
  for j in malisteA:
    malistefinale.append("{} {}".format(i,j))
print(malistefinale)
```

<br>


* et sinon ...

```
malistefinale = [ "{} {}".format(i,y) for i in maliste1 for y in malisteA ]
malistefinale = [ "{} {}".format(i,y) for i in maliste1 if i % 2 == 0 for y in malisteA ]
```
