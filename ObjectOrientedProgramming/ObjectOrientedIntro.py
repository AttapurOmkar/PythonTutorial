# Object Oriented Programming

# Variables in class are attributes
# Function in class are methods

#class NameOfClass():
    #Attribute
    #Method

# Pascal convention must be followed while naming class name

class Dog():
    species="mamal"
    def __init__(self,breed,name,spots):
        self.breed=breed
        self.name=name
        self.spots=spots

    def bark(self,num):
        print(f'Woofff woofa,humara kutta kutta, tumhana kutaa {self.name} and mera number is {num}')

my_dog=Dog(breed="lab",name="Tommy",spots="No Spots")
print(my_dog.species)
print(my_dog.breed)
my_dog.bark(2)


class ellipses():
    # class object attribute
    pi=3.14
    def __init__(self,major_axis=1,minor_axis=1):
        self.major_axis=major_axis
        self.minor_axis=minor_axis

    # method
    def area(self):
        return self.pi*self.major_axis *self.minor_axis

my_ellipse=ellipses(2,1)

print(my_ellipse.area())