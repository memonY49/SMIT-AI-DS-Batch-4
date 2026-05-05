# class animal:
#     # body of class
#     legs = 0
#     eyes = 0
#     tail = False
#     gender = ''
#     hair = False
#     color = ''
#     def __init__(self):
#         self.legs= 0
    
#     def sound(self):
#         pass
#     def runing(self):
#         print("animal is runing...")
#     def eat(self):
#         print("animal is eating")


# dog = animal()              #creating an object of animal class
# lizard = animal()           ##creating an object of animal class

# dog.legs = 4
# dog.eyes = 2
# dog.color = 'Gray'
# dog.gender = 'Male'
# dog.hair = True
# dog.tail = True

# lizard.hair = False

# print(lizard.hair)

# scope of variables and methods:
#       1.object level: Which can only be called from an object
#               -> can only be called with object name
#       2.static:       which are same for all objects
#               -> can be called by itself or by class name


# dog.runing()
# animal.runing()






class animal:
    eyes = 2                # static variable
    def __init__(self):
        self.legs = 0       # object level variable
        self.hair = False

    def running():          # static method of if not self as perameter
        print("animal is running")

dog = animal()
cat = animal()
lizard = animal()

print(animal.legs)

animal.eyes = 3
dog.legs = 4
cat.legs = 3
lizard.legs = 2


print(dog.legs)
print(cat.legs)
print(lizard.legs)

