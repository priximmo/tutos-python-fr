%title: PYTHON
%author: xavki
%Site : xavki.blog


# PYTHON : CLICK suite


<br>


* début

```
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

<br>


* click permet de gérer le prompt

```
@click.option("--name", prompt="A quel nom ?", help="A quel nom je dis bonjour")
```

<br>


* click permet de gérer l'affichage avec echo

```
click.echo(f"Hello, {name}")
```

--------------------------------------------------------------------

# PYTHON : CLICK suite


<br>


* la coloration de l'output avec secho

```
click.secho(f"Hello, {name}", fg="red", bold=True)
```

<br>


* le flag true/false sur argument

```
@click.option("--fr", "-f", is_flag=True, help="En français")
def cli(name,fr):
    """
      Ce script permet de faire un hello world
    """
    if fr:
        click.secho(f"Salut, {name}", fg="red", bold=True)
    else:
        click.secho(f"Hello, {name}", fg="red", bold=True)
```

--------------------------------------------------------------------

# PYTHON : CLICK suite

<br>


* choix du flag

```
@click.option("--fr/--eng", default=True, help="En français ou anglais")
```

<br>


* passer un tuple

```
@click.option('--data', required=True, type=(str, int))
def output(data):
    click.echo(f'name={data[0]} age={data[1]}')
```

<br>


* passer une liste

```
@click.option('--names', '-n', multiple=True)
```

<br>


* fichier

```
@click.argument('file_name', type=click.File('r'))
```
