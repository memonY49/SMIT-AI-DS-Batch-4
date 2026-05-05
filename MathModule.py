import math

# print(2**3)
# print(math.pow(2,5))
# print(math.sqrt(30))
# print(math.isqrt(30))
# print(math.cbrt(125))
# print(math.factorial(5))
# print(math.pi)
# print(math.nan)
# print(math.prod([0.25,0.10,0.75,-0.30]))
# print(math.prod([2,3,6,2]))
# print(math.sin(90))
# print(math.log10(2.34))
# print(math.floor(3.67))
# print(math.ceil(3.67))

# Create a function for area of a circle (A = πr2)
def area_of_circle(r):
    return math.pi * math.pow(r,2)

print(area_of_circle(4))

#create a function for if the number is a perfect sqrt or not (True, False) 

def is_perfect_sqrt(num: int):
    return math.sqrt(num) == math.isqrt(num)

print(is_perfect_sqrt(30))

# create a function to find distance between two points.

def distance(p1: tuple,p2: tuple):
    return math.sqrt(math.pow(p2[0]-p1[0],2)+math.pow(p2[1]-p1[1],2))

print(distance((3,4),(5,7)))

print(math.dist((3,4),(5,7)))


