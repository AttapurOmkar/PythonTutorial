# Inheritance

class Animal():
    def __init__(self):
        print('Animal created')
    def carnivore(self):
        print('I eat meat, I have claws')
    def herbivore(self):
        print('I eat grass, i am bunny')

#my_animal=Animal()
#my_animal.carnivore()
#my_animal.herbivore()

# Child class inherting Parent Animal class
class hunter(Animal):
    def __init__(self):
        Animal.__init__(self)
        print('Tiger Created')
    def herbivore(self):
        print('I am tiger, I do not eat grass but i eat bunty')

#my_tiger=hunter()
#my_tiger.carnivore()
#my_tiger.herbivore()
#end

# Polymorphism
# Poly means more than one
class Dog():
    def __init__(self,name):
        self.name=name

    def speak(self):
        return  self.name +'says woof'


class Cat():
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + 'says meowwww'

my_tommy=Dog('tommy')
my_sally=Cat('Sally')
print(my_tommy.speak())
print(my_sally.speak())

for pet in [my_sally,my_tommy]:
    print(pet.speak())