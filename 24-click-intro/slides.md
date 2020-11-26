%title: PYTHON
%author: xavki
%Site : xavki.blog


# PYTHON : CLICK


<br>


* click : module

```
pip3 install click
```

<br>


* spécifique à la CLI

* parsing des arguments et options

* passage de fichiers

* édition de l'aide

<br>


* mise en place de l'environnement

<br>


* exemple : help 

```
#!/usr/bin/python3
import click
@click.command()
@click.argument('name', default='ami')
def hello(name):
    """
        Salut la team !!
    """
    print("Hello {} !!!".format(name))
if __name__ == '__main__':
    hello()
```





