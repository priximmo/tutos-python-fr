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

* Définir une valeur par défaut pour des attributs

```
    def __init__(self,color,year):
        """Initialize the Voiture class"""
        self.color = color
        self.year  = year
        self.doors = 3

```

```
    def getCar(self):
        """Car caracteristics"""
        summary = f"""
  Color    : {self.color}
  Year     : {self.year}
  Doors    : {self.doors}
            """
```

-----------------------------------------------------------------

# PYTHON : Les Classes - Part 1

<br>

* Définir une valeur par défaut pour des attributs
