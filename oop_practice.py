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
#     def runing(self,name):
#         print(f"{name} is runing...")
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

# lizard.hair = True

# print(lizard.hair)
# lizard.runing("Lizard")


# # scope of variables and methods:
# #       1.object level: Which can only be called from an object
# #               -> can only be called with object name
# #       2.static:       which are same for all objects
# #               -> can be called by itself or by class name


# # dog.runing()
# # animal.runing()


# class animal:
#     eyes = 2                # static variable
#     def __init__(self):
#         self.legs = 0       # object level variable
#         self.hair = False

#     def running(self):          # static method of if not self as perameter
#         print("animal is running")


# dog = animal()
# print(dog.legs)
# dog.running()
# cat = animal()
# lizard = animal()

# # print(animal.legs)

# # animal.eyes = 3
# # dog.legs = 4
# # cat.legs = 3
# # lizard.legs = 2


# # print(dog.legs)
# # print(cat.legs)
# # print(lizard.legs)



# class student:
#     def __init__(self,name, fname, id):
#         self.name = name
#         self.fname = fname
#         self.id = id 

#     def print_std(self):
#         print(f"Name: {self.name},Fname: {self.fname},ID: {self.id}")

# class list_of_std:
#     def __init__(self):
#         self.all_stds = []
#     def add_std(self,std) -> None:
#         self.all_stds.append(std)

#     def delete_std(self,index:int) -> student:
#         return self.all_stds.pop(index)
    
#     def print_all_stds(self) -> None:
#         for stds in self.all_stds: 
#             stds.print_std()

# std1 = student("Yasir","Nawaz","001")
# std2 = student("Ahmed","Ali","002")
# std3 = student("Zeeshan","Ali","003")



# my_std_list = list_of_std()

# my_std_list.add_std(std1)
# my_std_list.add_std(std2)
# my_std_list.add_std(std3)

# my_std_list.print_all_stds()
# print("*"*20)
# deleted = my_std_list.delete_std(1)
# deleted.print_std()
# print("*"*20)
# my_std_list.print_all_stds()


# # std1.name = "Yasir"
# # std2.name = "Ahmed"
# # std3.name = "Ali"

# # std1.print_std()
# # std2.print_std()
# # std3.print_std()





# create a library managment system.
# Create a class book and a derived class ebook with methods for borrowing and returning
# books.
# use a decorator to log all activities and save them in a file named as logs.txt.
# Implement magic methods like __str__(),__len__(),and __add__() for display and manage 
# book data.
# store all borrowing and returning records in book_record.txt.


