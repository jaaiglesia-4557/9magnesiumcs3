#Superclass
class Animal:
  def __init__(self, name):
    try:
      name.upper()
      self.name = name
    except AttributeError:
      print("Error! Name must be a string(text)")

  def eat(self):
    print(f"{self.name} is eating...\n")

  def make_sound(self):
    print(f"{self.name} is making a sound!\n")

#Subclass 1
class Lion(Animal):
  def __init__(self, name):
    #Use super to use the attributes of superclass
    super().__init__(name)

  def eat(self):
    print(f"{self.name} eats fresh meat...\n")

  def make_sound(self):
    print(f"{self.name} roars loudly!\n")

#Subclass 2
class Elephant(Animal):
  def __init__(self, name):
    #Use super to use the attributes of superclass
    super().__init__(name)

    def eat(self):
      print(f"{self.name} eats grass and fruits...\n")

    def make_sound(self):
      print(f"{self.name} trumpets!\n")

#Subclass 3
class Monkey(Animal):
  def __init__(self, name):
    #Use super to use the attributes of superclass
    super().__init__(name)

  def eat(self):
    print(f"{self.name} eats bananas...\n")

  def make_sound(self):
    print(f"{self.name} chatters!\n")
# --- Test Run ---
print("--- Simulating the Test Run ---")

#For the ANIMAL Superclass only
Animal1 = Animal("Fah")
Animal1.eat()
Animal1.make_sound()

#For LION Subclass only
Lion1 = Lion("Roger")
Lion1.eat()
Lion1.make_sound()

#For ELEPHANT Subclass only
Elephant1 = Elephant("Dexter")
Elephant1.eat()
Elephant1.make_sound()

#For MONKEY Subclass only
Monkey1 = Monkey("Marcus")
Monkey1.eat()
Monkey1.make_sound()


 

