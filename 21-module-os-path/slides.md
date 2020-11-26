%title: PYTHON
%author: xavki
%Site : xavki.blog


# PYTHON : module OS - path

<br>


* utilisation de fonctions de système d'exploitation

<br>


* chargement et informations

```
import os
print(dir(os)
print(help(os.chmod)) # ex : chmod
```

<br>


* walk : parcourir un répertoire (répertoires et fichiers)
* environ : variables d'environnement

```
import os
os.walk('/tmp/')
```

* afficher le contenu de l'objet

```
import os
for chemin,repertoires,fichiers in os.walk('/tmp/'):
    print(chemin,repertoires,fichiers)
```

--------------------------------------------------------------------------------


# PYTHON : module OS - path


<br>


* récupérer une variable d'environnement

```
print(os.environ)
print(os.environ.get('USER'))
print(os.environ.get('HOME'))
```

<br>


* jointure avec ou sans slash

```
print(os.path.join("/my/home","test.txt"))
print(os.path.join("/my/home/","test.txt"))
```

<br>


* split, splitext, dirname et basename

```
print(os.path.basename("/my/home/test.txt"))
print(os.path.dirname("/my/home/test.txt"))
print(os.path.split("/my/home/test.txt"))
print(os.path.splitext("/my/home/test.txt"))
```

<br>


* condition

```
print(os.path.exists("/my/home/test.txt"))
print(os.path.isdir("/tmp/"))
print(os.path.isfile("/my/home/test.txt"))
```

