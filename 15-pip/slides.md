%title: PYTHON
%author: xavki
%Site : xavki.blog


# PYTHON : PIP

<br>
* gestionnaire de librairies/paquets


```
apt install python3-pip
```

<br>
* aide :

```
pip help
pip install help
```

<br>
* chercher une librairie

```
pip search pandas
```

<br>
* lister les lib installées

```
pip list
```

--------------------------------------------------------


# PYTHON : PIP


<br>
* installation/désintallation

```
pip install pandas
pip uninstall pandas
```

<br>
* lib et leurs versions

```
pip list -o
```

<br>
* liste de lib pour réinstaller à l'identique

```
pip freeze > requirements.txt
```

<br>
* restauration 

```
pip install -r requirements.txt
```

<br>
* upgrade de tou les paquets à mettre à jour

```
pip list --format=legacy --outdated | cut -d' ' -f1 | xargs pip install --upgrade 
```
