%title: PYTHON
%author: xavki
%Site : xavki.blog


# PYTHON : closure


<br>
* notion de closures = fonction dans une fonction et retourne la fonction

* réserver un espace mémoire pour cette fonction

* cela est assimilable à instancier une classe

<br>
* exemple sans closure

```
def fonction1():
  var1 = "Salut"
  def fonction2():
    print("{} Xavki !!!".format(var1))
  return fonction2()
fonction1()
```

--------------------------------------------------------------------

# PYTHON : clojure


<br>
* avec closure on retourne la fonction 

```
def fonction1():  	# on peut parler de générateur de closure
  var1 = "Salut"
  def fonction2():	# closure
    print("{} Xavki !!!".format(var1))
  return fonction2
resultat = fonction1()
print(resultat)
```

<br>
* exemple :

```
def fonction1(nom):
  def closure2(mot):
    print("{} {} !!!".format(mot,nom))
  return closure2
resultat = fonction1("Xavki")
print(resultat("Bonjour"))
print(resultat("Salut"))
```

Rq :on a gardé en mémoire le nom instancié dans la fonction1

---------------------------------------------------------------------

# PYTHON : clojure


<br>
* et un peu plus...


```
def fonction1(nom):
  def closure2(mot):
    print("{} {} !!!".format(mot,nom))
  return closure2
resultat = fonction1("Xavki")
resultat2 = fonction1("Xavier")
print(resultat("Bonjour"))
print(resultat2("Salut"))
print(resultat("Bye"))
```

* finalement on est proche du comportement d'une classe
