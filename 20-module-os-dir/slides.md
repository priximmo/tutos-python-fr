%title: PYTHON
%author: xavki
%Site : xavki.blog


# PYTHON : module OS - dir

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
* utilisation avec getcwd (pwd)

```
print(os.getcwd())
```

--------------------------------------------------------------


# PYTHON : module OS


<br>
* déplacement

```
os.chdir('/tmp/')
print(os.getcwd())
```

<br>
* lister les répertoires

```
print(os.listdir('/tmp/'))
```

<br>
* créer un répertoire (sur un niveau = non récursif)

```
os.mkdir('/tmp/myrep')
print(os.listdir('/tmp/'))
```

* créer des répertoires de manière récursive


```
os.makedirs('/tmp/myrep2/lvl1')
print(os.listdir('/tmp/myrep2'))
```


--------------------------------------------------------------


# PYTHON : module OS


<br>
* suppression d'un répertoire

```
os.rmdir('/tmp/myrep2/lvl1')
print(os.listdir('/tmp/myrep2'))
```

<br>
* suppression recursive (attention se placer dans le répertoire)

```
os.makedirs('/tmp/myrep2/lvl1/lvl2')
os.chdir('/tmp/myrep2/')
os.removedirs('lvl1/lvl2')
print(os.listdir('/tmp/myrep2'))
```

<br>
* modification du nom (idem fichiers)

```
os.makedirs('/tmp/myrep2/lvl1/lvl2')
os.rename('/tmp/myrep2/lvl1/lvl2','/tmp/myrep2/lvl1/lvl3')
print(os.listdir('/tmp/myrep2/lvl1'))
```

-----------------------------------------------------------------


# PYTHON : modue OS


<br>
* informations

```
print(os.stat('/tmp/myrep2/lvl1'))
print(os.stat('/tmp/myrep2/lvl1').st_size)
```

<br>
* modification time

```
import os
import datetime
mod_time = os.stat('/tmp/myrep2/lvl1').st_mtime
print(datetime.datetime.fromtimestamp(mod_time))
```
