'''
Implicit: Automatic conversion (int to float)
Explicit: Forced to be converted (float to int)
convert anything to integer use int(data/variable) function
convert anything to str use str(data/variable) function
convert anything to float use float(data/variable) function
'''
'''
a = 4.6
b = int(a)

# to check type of any value use type(value) function


#create 2 variables named as X,Y. perform (+,-,*,/ and %) on them.
x = 6
y = 4

print(x,"+",y,"=",x+y,end= ' ')
print(x,"-",y,"=",x-y, sep = ' ')
print(x,"/",y,"=",x/y)
print(x,"*",y,"=",x*y)
print(x,"%",y,"=",x%y)
print(y,"%",x,"=",y%x)

'''






'''
comparison operators:
1. less than '<'
2. greater than '>'
3. equal to '=='
4. not equal to '!='
5. less than or equal to '<='
6. greater than or equal to '>='
'''
'''
x = 7
y = 5

print(x<y)
print(x>y)
print(x<=y)
print(x>=y)
print(x==y)
print(x!=y)
'''
'''
logical operators:
    1. and
    2. or
    3. not
    => in logical operators the operands are boolean and
    the output is also boolean
'''

x = 10
y = 6

# print(x>0 and x<10)
# print(False or False)

# print(not x<y)


# Task1: convert 120F to C and Kelvin (hint: (32°F − 32) × 5/9 = 0°C,	
# 0°C + 273.15 = 273.15K)

# Task2: convert 493mm into cm, km, mile (hint: 1cm = 10mm, 1km = 100000cm and
# 1mile = 1.60934km)

# Task3: convert 38945g into mg, kg and ounce (hint: 1ounce = 28.3495g,
# 1mg = 0.001g)
'''
f = 120
c = (f - 32)*(5/9)
k = c + 273.15
print("f:",f,"c:",c,"k:",k)

mm = 493
cm = mm/10
km = cm/100000
mile = km/1.60934
print("mm:",mm,"cm:",cm,"km:",km,"mile:",mile)

g = 38945
mg = g*1000
kg = g/1000
ounce = g/28.3495
print("g:",g,"mg:",mg,"kg:",kg,"ounce:",ounce)
'''

'''
How to get value from user as input
'''

userinput = float(input("Please enter the value in f: "))

f = userinput
c = (f - 32)*(5/9)
k = c + 273.15
print("f:",f,"c:",c,"k:",k)





















