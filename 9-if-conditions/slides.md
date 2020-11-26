%title: PYTHON
%author: xavki
%Site : xavki.blog


# PYTHON : If conditions


<br>


* if = condition

* principe :

```
if True:
  print("Vrai")
else:
  print("False")
```
<br>


* opérateurs de comparaison :
	* == : égalité
  * >=
  * <=
  * != : différent de
  * is : comparateur d'objets mémoire

----------------------------------------------

# PYTHON : If conditions


<br>


* sinon

```
if channel == "xavki":
  print("bien")
elif channel == "youtube":
  print("pas mal")
else:
  print("pas bien")
```

<br>


* opérateurs and / or / not

```
active = True
if channel == "xavki" and active:
  print("kool"
elsif not active:
  print("lol")
else:
  print("bof")
```

------------------------------------------------


# PYTHON : If conditions


<br>


* cas du IS

```
l1 = ["A", "B", "C"]
l2 = ["A", "B", "C"]

if l1 == l2:
  print("égalité")

if l1 is l2:
	print("même objet")

print(id(l1))
print(id(l2))
```

<br>


* les booléens

```
obj = False
if obj:
    print("je suis vrai")
else:
    print("je suis faux")
```

```
0
None
[]
""
()
{}
```

