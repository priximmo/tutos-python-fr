%title: PYTHON
%author: xavki
%Site : xavki.blog


# PYTHON : Les Classes - Part 2


<br>

POO : 

	* classes

	* attributs

	* méthode

	* instance

-----------------------------------------------------------------

# PYTHON : Les Classes - Part 2

<br>

* attributs - valeur par défaut

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
        return summary
```

Note : xavkicar.doors = 5

-----------------------------------------------------------------

# PYTHON : Les Classes - Part 2

<br>

* méthode - appeler une autre méthode

```
    def getCar(self):
        """Car caracteristics"""
        summary = f"""
  Color    : {self.color}
  Year     : {self.year}
  MaxSpeed : {self.max_speed()}
  Doors    : {self.doors}
            """
        return summary
```


-----------------------------------------------------------------

# PYTHON : Les Classes - Part 2

<br>

* méthode - redéfinir une valeur par défaut

```
    def __init__(self,color,year):
        """Initialize the Voiture class"""
        self.color = color
        self.year  = year
        self.doors = 3
        self.crash = 0
```

```
  Doors    : {self.doors}
  Crash    : {self.crash}
```

```
    def setCrash(self,crash):
        self.crash += crash
```

```
print(xavcar.getCar())
xavcar.setCrash(10)
print(xavcar.getCar())
```

-----------------------------------------------------------------

# PYTHON : Les Classes - Part 2

<br>

* héritage une classe parents/enfants

```
class ClassicCar(Car):
    """Car with classical charateristics"""
    def __init__(self,color,year,crash):
        """Initialize a classical category of car"""
        super().__init__(color,year)
        self.crash = crash
```
xavcar = ClassicCar("Yellow",2000,1)
print(xavcar.getCar())
```

-----------------------------------------------------------------

# PYTHON : Les Classes - Part 2

<br>

* méthode spécifique à la classe enfant

```
        self.seat  = 5
    def getClassicCar(self):
        """Classical Car characteristics"""
        summary = f"""
  Color    : {self.color}
  Year     : {self.year}
  MaxSpeed : {self.max_speed()}
  Doors    : {self.doors}
  Crash    : {self.crash}
  Seat     : {self.seat}
            """
        return summary
```

```
print(xavcar.getClassicCar())
```
