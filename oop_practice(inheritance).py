# class A:
#     def __init__(self):
#         self.value1 = "hello"
#         self.value2 = "world"
#     def foo(self):
#         print("foo...!")

# class B(A):
#     pass

# myclass = B()

# myclass.foo()

# print(myclass.value1)



class animal:
    def __init__(self):
        self.legs = 0
        self.eyes = 2
        self.tail = False
    def sound(self):
        print("animal sound")
    
    def eat(self):
        print("animal is eating")

class dog(animal):
    def __init__(self):
        pass
    def sound(self):
        print("Dog is barking....")

class cat(animal):
    def __init__(self):
        pass

my_dog1 = dog()

my_dog1.sound()


# class person:
#     def __init__(self):
#         self.name = ""
#         self.age = 0
#         self.fname = ""
#         self.gender = ""
#     def set_name(self,v:str):
#         self.name = v
#     def set_age(self,v:int):
#         self.age = v
#     def set_fname(self,v:str):
#         self.fname = v
#     def set_gender(self,v:str):
#         self.gender = v

#     def get_age(self):
#         return self.age
#     def get_name(self):
#         return self.name
#     def get_gender(self):
#         return self.gender
#     def get_fname(self):
#         return self.fname

# p1 = person()

# p1.set_name("Yasir")
# p1.set_fname("Nawaz")
# p1.set_age(27)
# p1.set_gender("Male")

# print(p1.get_name())



# class vehical:
#     def __init__(self):
#         self.wheels = 4
#         self.engine = ""
#         self.doors = 2
#         self.spark = False
#         self.gear = 0
#         self.air_val = False
#         self.fuel_injection = False

#     def ignition(self):
#         self.air_val = True
#         self.fuel_injection = True
#         self.spark = True
#     def start(self):
#         self.ignition()
#     def set_gear(self,g:int):
#         self.gear = g

#     def br(self,g:int):
#         self.set_gear(g)



# mycar = vehical()

# mycar.start()
# mycar.br(3)



# # class person:
# #     def __init__(self):
#         self.name = ""
#         self.age = 0
#         self.fname = ""
#         self.gender = ""
#     def set_all_attr(self, n, v):
#         super().__setattr__(n,v)
#     def get_all_attr(self, n):
#         return super().__getattribute__(n)
        

# p2 = person()
# p2.set_all_attr("name","Yasir")
# p2.set_all_attr("fname","Nawaz")
# p2.set_all_attr("age",27)
# p2.set_all_attr("gender","Male")


# p2.__setattr__("age",37)
# print(p2.get_all_attr("age"))


# class human:
#     def __init__(self,color,legs=2,eyes=2,hair=True,hands = 2):
#         self.color = color
#         self.legs = legs
#         self.eyes = eyes
#         self.hair = hair
#         self.hands = hands
# class person:
#     def __init__(self,name,age,fname,gender,**kwargs):
#         super().__init__(**kwargs)
#         self.name = name
#         self.age = age
#         self.fname = fname
#         self.gender = gender
    
# class student(person,human):
#     def __init__(self,id,cl,**kwargs):
#         super().__init__(**kwargs)
#         self.id = id
#         self.cl = cl
#     def setter(self,n,v):
#         super().__setattr__(n,v)
#     def getter(self,n):
#         return super().__getattribute__(n)


# std1 = student("001","1st",name="yasir",age=27,fname="nawaz",gender="male",color="brown")

# p2 = person("ahmed",30,"ali","male")


# print(std1.getter("color"))