%title: PYTHON
%author: xavki
%Site : xavki.blog


# PYTHON : generators


<br>
* fonctions et les itérations de résultats

* la où ça coince :

```
def mafonction(maliste):
    for item in maliste:
        return "Hello number : ".format(item)
liste = [ i for i in range(10)]
print(mafonction(liste))
```

Rq : solution ? retourner une liste , append...

<br>
* mot clef "yield" > generator

```
def mafonction(maliste):
    for item in maliste:
        yield "Hello number : ".format(item)
```

Attention : aux performances (meilleures si on ne repasse pas par une liste)

* yield = coroutine

--------------------------------------------------------------------------


# PYTHON : generators

<br>
* parcourir un generator

```
result = mafonction(liste)
print(next(result))
print(next(result))
print(next(result))
print(next(result))
```

<br>
* récupérer l'intégralité sans next ?

```
result = [i for i in mafonction(liste)]
print(result)
```

<br>
* et ça tombe bien car on créer un generator...

```
result = (i for i in range(10))
print(result)
check = list(result)
print(chck)
```

```
result = ("Hello number {}".format(i) for i in range(10))
check = [i for i in result]
print(check)
```



