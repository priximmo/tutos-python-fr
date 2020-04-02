%title: PYTHON
%author: xavki
%Site : xavki.blog


# PYTHON : les Modules


<br>
* modules = organisation du code / partage

* partage de variables, fonctions

<br>
* mon_module.py :

```
#!/usr/bin/python
mavariable = "la variable du module"
print("Je suis {}".format(mavariable))
```

* ma page main.py :

```
#!/usr/bin/python
import mon_module #as mm
mavariable = "variable du main"
```

-----------------------------------------------------------------

# PYTHON : les Modules


<br>
* fonctions :

```
#!/usr/bin/python
mavariable = "la variable du module"
print("Je suis {}".format(mavariable))
def mafonction(defaut = mavariable):
    return "Fonction du module : {}".format(defaut)
```

* main.py :

```
#!/usr/bin/python
import mon_module
mavariable = "variable du main"
print(mon_module.mafonction())
```

-----------------------------------------------------------------

# PYTHON : les Modules


<br>
* fonctions :

```
#!/usr/bin/python
mavariable = "la variable du module"
print("Je suis {}".format(mavariable))
def mafonction(defaut = mavariable):
    return "Fonction du module : {}".format(defaut)
```

* main.py :

```
#!/usr/bin/python
import mon_module
mavariable = "variable du main"
print(mon_module.mafonction(mavariable))
```

-----------------------------------------------------------------

# PYTHON : les Modules


<br>
* fonctions :

```
#!/usr/bin/python
mavariable = "la variable du module"
print("Je suis {}".format(mavariable))
def mafonction(defaut = mavariable):
    return "Fonction du module : {}".format(defaut)
```

* main.py :

```
#!/usr/bin/python
from mon_module import mafonction #ajout en tant que de besoin ou toutes *
mavariable = "variable du main"
print(mon_module.mafonction())
```
