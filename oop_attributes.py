#class object attribute: available attributes to all object of the same type. same for any instance of class 
#instance attributes: available for instances of a class 

class Dog:
  species = "Mammal" #same for all instances of dog classes
  def __init__(self,breed, name, spots):
    #these attributes are unique for each instance
    self.breed = breed
    self.name = name
    self.spots = spots 

  def bark(self): #instance methods have to start with self as the first positional argumebt
  def method2(self):
    pass 
  def method3(self): 
    pass 
    


  