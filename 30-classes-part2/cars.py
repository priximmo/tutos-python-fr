#!/usr/bin/python3

class Car:
  """Define a car"""

  def __init__(self,color,year):
    """Initialize the Car class"""
    self.color = color
    self.year  = year
    self.doors = 3 
    self.crash = 0

  def max_speed(self):
    """Max speed calculation"""

    if self.year < 1950:
        maxspeed = 150

    elif self.year < 1980:
        maxspeed = 200

    else:
        maxspeed = 250
  
    return maxspeed

  def getCar(self):
    """Car caracteristics"""
    summary = f"""
Color    : {self.color}
Year     : {self.year}
Doors    : {self.doors}
MaxSpeed : {self.max_speed()}
Crash    : {self.crash}
        """
    return summary

  def setCrash(self,crash):
      self.crash += crash

class ClassicCar(Car):
  """Car with classical charateristics"""

  def __init__(self,color,year,crash):            
    """Initialize a classical category of car"""
    super().__init__(color,year)
    self.crash = crash
    self.seat  = 3

  def getClassicCar(self):
      """Classical Car characteristics"""         
      summary = f"""
...
MaxSpeed : {self.max_speed()}
Doors    : {self.doors}
Crash    : {self.crash}
Seat     : {self.seat}
          """
      return summary


xavkicar = ClassicCar("Red",1930,2)
xavkicar.seat = 5
print(xavkicar.getClassicCar())
