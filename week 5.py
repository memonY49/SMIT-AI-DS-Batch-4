'''
Loops: to repeat a block of code for multiple times if the condition is true.
Type: for loop
    syntax:
        for counter in range(0,10):
            #body of for loop
'''

#for i in range(1,11):
    #print(9*i)


#for odd in range(11,1,-1):
#    print(odd)

#a,b,c,d,e,f,g,h
#for i in "abcdefgh":
#    print(i,end = ',')

'''
    while loop:
    syntax:
        initialize counter
        while condition:
            body of while
            inc/dec
'''
'''
counter = 1
while counter <=10:
    print(counter)
    counter = counter + 1



print(counter)

'''
"""

stars = int(input("Enter the no for stars in one line: "))
for i in range(1,stars+1):
    print("*"*i)


* 
* * 
* * * 
* * * *
* * * * * 
"""

"""
----* 
---* * 
--* * * 
-* * * *
* * * * * 

stars = 5
for i in range(1,stars+1):
    print(' '*(stars-i),end = '')
    print("* "*i)
"""

'''
    * 
   * * 
  * * * 
 * * * * 
* * * * *
 * * * *
  * * *
   * *
    *

stars = 5
for i in range(1,stars):
    print(' '*(stars-i),end = '')
    print("* "*i)
    
for i in range(stars, 0 ,-1):
    print(' '*(stars-i)+'* '*i)
'''

stars = 5
i = 1
while i < stars:
    print(' '*(stars-i)+'* '*i)
    i += 1

i = stars
while i > 0:
    print(' '*(stars-i)+'* '*i)
    i -= 1














