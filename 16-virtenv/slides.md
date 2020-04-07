%title: PYTHON
%author: xavki
%Site : xavki.blog


# PYTHON : VirtualEnv

<br>
* isolation

* installation

```
pip install virtualenv
```

* mise en place d'un projet

```
virtualenv mydev1
```

* utiliser

```
source mydev1/bin/activate
deactivate
```

--------------------------------------------------


# PYTHON : VirtualEnv


<br>
* version de python 

```
virtualenv --python usr/bin/python3 mydev2
source mydev2/bin/activate
python
```

* idem versions/librairies

```
pip list
```

* utilisation du requirements/freeze

```
pip freeze --local > requirements.tx
pip install -r requirements.txt
```
