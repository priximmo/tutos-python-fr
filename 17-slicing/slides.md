%title: PYTHON
%author: xavki
%Site : xavki.blog


# PYTHON : Slicing

<br>


* manipulation de liste

* à partir des index
	* positifs : du début
	* négatifs : on part de la fin

* exemple :

```
maliste = [0, 1, 2, 3, 4, 5, 6, 7]
maliste[2]
maliste[-2]
```

-----------------------------------------------------

# PYTHON : Slicing


<br>


* principe [ START : FIN : EVOL ]

* FIN : non inclusif

* exemple :

```
maliste[0:3]
maliste[:3]
maliste[0:7:2]
```

* reverse :

```
maliste[::-1]
```

* ex url :

```
monurl = "xavki.blog"
print(monurl[:-5])
```

* si mix fr, blog...

```
point = monurl.index(".")
print(monurl[:point])
```
