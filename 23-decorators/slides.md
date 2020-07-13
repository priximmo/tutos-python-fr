%title: PYTHON
%author: xavki
%Site : xavki.blog


# PYTHON : Decorators


<br>
* décorer une fonction = étendre sans la modifier

* éviter les duplications de code

* une fonction de fonction... (pas tout à fait)

<br>
* exemple sans decorator (ajou de "Message :") :

```
def mafonction1():
  return "Hello Xavki"
```
--------------------------------------------------------------------

# PYTHON : Decorators


<br>
* exemple avec decorator

```
def dec(fonction):
  print("Message : ")
  return fonction
@dec
def mafonction1():
  return "Hello Xavki"
print(mafonction1())
```

--------------------------------------------------------------------

# PYTHON : Decorators


<br>
* exemple couleur - wraps

```
from functools import wraps
def vert(f):
    @wraps(f)
    def wrapped(*args, **kwargs):
        r = f(*args, **kwargs)
        phrase = "\033[32m {} \033[0m".format(r)        
        return phrase
    return wrapped
@vert
def mafonction1():
    return "Hello xavki"
def mafonction2():
    return "Au revoir xavki"
print(mafonction1())
print(mafonction2())
```

--------------------------------------------------------------------

# PYTHON : Decorators


<br>
* exemple timestamp

```
from datetime import datetime
from functools import wraps
def ts(f):
    @wraps(f)
    def wrapped(*args, **kwargs):
        r = f(*args, **kwargs)
        phrase = "{} | {}".format(datetime.now(),r)
        return phrase
    return wrapped
@ts
def mafonction1():
    return "Hello xavki"
@ts
def mafonction2():
    return "Au revoir xavki"
print(mafonction1())
print(mafonction2())
```
