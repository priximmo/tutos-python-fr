%title: PYTHON
%author: xavki
%Site : xavki.blog


# PYTHON : intro

<br>


* langage interprété  : sans étape préalable (ruby, perl)

* à la différence de langages compilés (compilation ou assemblage = C, C++, assembleur) 

* IDE Visual studio code : éditeur de code

https://code.visualstudio.com/docs/?dv=linux64_deb

extension : code runner

<br>


* retrouver le binaire python

```
which python
```

* entête de script python
```
#!/usr/bin/python
```


---------------------------------------------------------------------


# PYTHON : strings

<br>


* entre doubles ou simples quotes (échaper si nécessaire)

```
print("Hello World")
```

<br>


* sur plusieurs ligne triple quotes ou triple doubles

```
print("""
Salut
je m'appelle
Xavki !!
""")
```

-------------------------------------------------------------------

# PYTHON : variables


<br>


* variables
	* simplifier maintenance
	* meilleure compréhension
	* sans dollar

```
variable = "Xavki"
print("Bonjour " + variable + " !!!")
```

<br>


* plus lisible encore

```
mot = "Hello"
variable = "Xavki"
phrase = "{} {} !!!".format(mot,variable)
print(phrase)
```

<br>


* typage

```
print(type(variable))
```
