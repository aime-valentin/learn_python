#inheritance: form classes from other classes 
#interface, abstract classes, parent class, and child classes
class Animal():
  
  def __init__(self):
    print("animal created")

  def who_am_i(self):
    print("i am an animal")

  def eat(self):
    print("am eating")

class Dog(Animal):

  def __init__(self):
    Animal.__init__(self) #same as super() in java
    print("dog created")

  def who_am_i(self): #overrides methods from super clas
    print("i am a dog")

  def eat(self):
    print("i am not eating")

  def bark(self):
    print('whoof')

#polymorphism:object classes share methods
#abstract: a template/base class for a particular object 

class Animal: #abstract class

  def __init__(self,name):
    self.name = name

  def speak(self): #abstract method
      raise NotImplemented("subclass must implement this method")



