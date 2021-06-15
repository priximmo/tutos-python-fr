%title: PYTHON
%author: xavki
%Site : xavki.blog


# PYTHON : Les Classes - Part 1


<br>

Programmation Orientée Objet (POO)

* approche moins algo de la programmation

* représentation des choses sous forme d'objets

* tout est objet : voiture, maison, dés, requête...

* forme de représentation des choses

* facilités > maintenir, organiser et réutiliser le code 

-----------------------------------------------------------------

# PYTHON : Les Classes - Part 1


<br>

POO : 

	* classes

	* attributs

	* méthode

	* instance

-----------------------------------------------------------------

# PYTHON : Les Classes - Part 1

<br>

Classes :

		* approche réelle des objets

		* décrire les caractéristiques d'un objet

		* description des comportements de l'objet

		* mot clef "class"

		* créer un objet d'une classe > répondre à ses caractéristiques

		* constructeur init()  méthode de construction de la classe

-----------------------------------------------------------------

# PYTHON : Les Classes - Part 1

<br>

Instance :

		* instanciation de la classe

		* définition des principales caractéristiques de cette instance

		* 1 classe > de multiples instances avec les mêmes caractéristiques

		* instance contenue dans une variable

-----------------------------------------------------------------

# PYTHON : Les Classes - Part 1

<br>

Attributs :

		* variables spécifiques à une classe

		* données spécifiques à une instance de cette classe

<br>

Méthode : 

		* fonction spécifique à une classe

		* peu prendre des variables en entrées

		* variables > attributs de la classe

-----------------------------------------------------------------

# PYTHON : Les Classes - Part 1

<br>

Mise en pratique - création d'une classe

<br>

	* création d'une classe

```
class Voiture:
```

Notes : majuscule par convention

<br>

	* commentaire de la classe

```
class Voiture:
    """Define a car"""
```

-----------------------------------------------------------------

# PYTHON : Les Classes - Part 1

<br>

	* méthode init > contructeur de la classe

```
class Car:
    """Define a car"""
    def __init__(self,color):
        """Initialize the Voiture class"""
```

Notes: self nécessaire pour créer la classe, en première position

-----------------------------------------------------------------

# PYTHON : Les Classes - Part 1

<br>

	* définir un attribut de la classe

```
class Car:
    """Define a car"""
    def __init__(self,color):
        """Initialize the Voiture class"""
        self.color = color
```

Notes : les attributs définie par self sont utilisables 
	par les méthodes de la classe


-----------------------------------------------------------------

# PYTHON : Les Classes - Part 1

<br>

Mise en pratique - instanciation et utilisation

<br>

* création d'une instance de cette classe

```
xavcar = Car("red")
```

<br>

* utilisation d'inattribut de cette classe

```
print(xavcar.color)
```


-----------------------------------------------------------------

# PYTHON : Les Classes - Part 1


<br>

Mise en pratique - définition et utilisation d'une méthode

```
class Car:
    """Define a car"""
    def __init__(self,color,year):
        """Initialize the Voiture class"""
        self.color = color
        self.year = year
    def max_speed(self):
        """Max speed calculation"""
        if self.year < 1950:
            maxspeed = 150
        elif self.year < 1980:
            maxspeed = 200
        else:
            maxspeed = 250
        return maxspeed
```

```
xavcar = Car("red",1960)
print(xavcar.max_speed())
```

-----------------------------------------------------------------

# PYTHON : Les Classes - Part 1


<br>

Mise en pratique - créer une autre instance

```
paulcar = Car("grey", 1930)
print(paulcar.max_speed())
```
