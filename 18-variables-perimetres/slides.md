%title: PYTHON
%author: xavki
%Site : xavki.blog


# PYTHON : Globales vs locales

<br>
* la portée des variables

* variables locales vs variables globales

* importance sur de gros programmes

<br>
* locales = à une fonction et peuvent être utilisées ailleurs par d'autres fonctions (taille etc diff)

* global = sans limite, définie en dehors d'une fonction (sauf si utilisation du mot clef global)

---------------------------------------------------------------------


# PYTHON : Globales vs locales


<br>
* globale

```
var = "ma variable globale"
def mafonction():
  print(var)
fonction()
```

<br>
* locale

```
var = "ma variable globale"
def mafonction():
  var2 = "ma variable locale"
  print(var2)
mafonction()
print(var)
print(var2)
```

---------------------------------------------------------------------------


# PYTHON : Globales vs locales


<br>
* locale à une fonction

```
var = "ma variable globale"
def mafonction():
  var = "ma variable locale"
  print(var)
mafonction()
print(var)
```

<br>
* forcer une globale dans une fonction (pas top)

```
var = "ma variable globale"
def mafonction():
  global var
  var = "ma variable locale"
  print(var)
mafonction()
print(var)
```


---------------------------------------------------------------------------


# PYTHON : Globales vs locales



<br>
* et dans des nested function (imbriquées)

```
def fonction1():
  var = "var1"
  def fonction2():
    var = "var2"
    print(var)
  fonction2()
  print(var)
fonction1()
```

Rq : comment de var2

