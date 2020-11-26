%title: PYTHON
%author: xavki
%Site : xavki.blog


# PYTHON : les Fonctions


<br>


* objectif ? factoriser

* éviter de refaire 2 fois la même chose

* meilleure maintenance : modifier une fois le code

<br>


* principe :

```
def mafonction():
  action
```

* exemple :

```
print("Hello Xavki !!!)
print("Hello Xavki !!!)
print("Hello Xavki !!!)
print("Hello Xavki !!!)
```


----------------------------------------------------------------------

# PYTHON : les Fonctions


<br>


* affichage ou non ? laisser le choix à l'utilisateur de la fonction

```
def mafonction():
  return "Hello Xavki !!!"
print(mafonction())
```

<br>


* return = jouer des méthodes sur la fonctions

```
def mafonction():
  return "Hello Xavki !!!"
print(mafonction().upper())
```

--------------------------------------------------------------------

# PYTHON : les Fonctions



<br>


* passer des variables :

```
def mafonction(action,nom):
  return "{} {} !!!".format(action, nom)
print(mafonction("Hello", "Xavki")
```

<br>


* variable par défaut :

```
def mafonction(action = "Bonjour", nom = "Xavki"):
  return "{} {} !!!".format(action, nom)
#print(mafonction("Hello", "Xavier")
```
