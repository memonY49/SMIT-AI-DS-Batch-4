#std1 = ['yasir','D',58,True]
#std1[3] = 'abc'
#print(std1[3])
'''
    Tuple: It is an Imutable collection of hetrogeneus elements.
    syntax:
            mytuple = (1,2,3,4,5,6)
'''    
#mytuple  = ('Yasir','A',98,True)
#mytuple[0] = 88
#print(mytuple[0])
'''
    Set: A well defined unordered collection of unique elements.
    syntax:
            myset = {1,2,3,4,5}
'''
#myset = {1,3,4,5,6,0,7,1,False,'A','A','B'}
#print(myset)

'''
List Functions:
	append( Element to add)	Adds an element at the end of the list
	clear()			Removes all the elements from the list
	copy()			Returns a copy of the list
	count(Element)		Returns the number of elements with the specified value
	extend()		Add the elements of a list (or any iterable), to the end of the current list
	index(Element)		Returns the index of the first element with the specified value
	insert(Index, Element)	Adds an element at the specified position
	pop()			Removes the element at the last element
	remove(Element)		Removes the item with the specified value
	reverse()		Reverses the order of the list
	sort()			Sorts the list


syntax:
    object.func()
'''



#mylist = [1,22,34,55,67,93,55]
#mylist.append(56)
#mylist.insert(7,'abc')
#mylist.extend([22,66,78,28,39])
#mylist.pop(0)
#mylist.remove(55)
#mylist.clear()
#print(mylist.count(55))
#print(len(mylist))
#print(mylist.index(55))

'''
elements = []
element_to_find = 100
for i in range(len(mylist)):
    if mylist[i] == element_to_find:
        elements.append(i)
print(elements)
'''

#mylist.reverse()
#mylist.sort(reverse = True)
#print(mylist)



'''
Multi Dimensional List: List of Lists
syntax:
    mylist = [[1,2,3],
              ['a','b','c'],
              [2.6,4.7,5.5],
              [Ture,False,True]]
    print(mylist[2][1])


data = [['Yasir','abc@gmail.com','abc123'],
        ['Yasir1','abc1@gmail.com','abc123'],
        ['Yasir2','abc2@gmail.com','abc123'],
        ['Yasir3','abc3@gmail.com','abc123']]

for i in range(len(data)):
    user = data[i]
    for j in range(len(user)):
        print(user[j])
    print("*"*10)
'''

''' Class Task:-
step1: Store atleast 5 user data (Name,Fname, Phone, Email and Pass) in a
       single multi dimensional list.
step2: Ask user for useremail and userpass.
step3: Match if useremail and userpass matches to any of the stored user.
step4: Print user matched along with the details of that user otherwise print
       user not found.

data = [['Yasir','Nawaz','abc@gmail.com','abc123'],
        ['Yasir1','Nawaz','abc1@gmail.com','abc123'],
        ['Yasir2','Nawaz','abc2@gmail.com','abc123'],
        ['Yasir3','Nawaz','abc3@gmail.com','abc123']]

useremail = input("Enter your email: ")
userpass = input("Enter your pass: ")

for i in range(len(data)):
    
    if useremail == data[i][2] and userpass == data[i][3]:
        print("User Matched")
        print("Name:",user[0])
        print("FName:",user[1])
        print("Email:",user[2])
        break
else:
    print("User not found!!")
'''
# a = [[[11,12,13],
#       ['a1','a2','a3'],
#       ['b1','b2','b3']],
#      [[21,22,23],
#       ['c1','c2','c3'],
#       ['d1','d2','d3']],
#      [[31,32,33],
#       ['e1','e2','e3'],
#       ['f1','f2','f3']]]

# print(a[0][1][2])

'''
data = [[['Company','Car name','Model','Year',Price],
          ['Company','Car name','Model','Year',Price],
          ['Company','Car name','Model','Year',Price],
          ['Company','Car name','Model','Year',Price],
          ['Company','Car name','Model','Year',Price]],
        [['Company','Car name','Model','Year',Price],
          ['Company','Car name','Model','Year',Price],
          ['Company','Car name','Model','Year',Price],
          ['Company','Car name','Model','Year',Price],
          ['Company','Car name','Model','Year',Price]],
        [['Company','Car name','Model','Year',Price],
          ['Company','Car name','Model','Year',Price],
          ['Company','Car name','Model','Year',Price],
          ['Company','Car name','Model','Year',Price],
          ['Company','Car name','Model','Year',Price]]]
Task for week 8: showroom managment system.
    step1: Store details of atleast five cars for atleast 3 companies in a
           multi dimesional list.
    step2: Create a menu for the user and ask for sell or buy the car.
        menu:
            1.Buy
            2.Sell
            0.Exit
            Enter your selection:
    step3: For Buy option show user another menu for the car companies.
        menu:
            1.Toyota
            2.Suzuki
            3.Kia
            Enter your selection:
    step4: if the user selects the company than show them all cars that are
           available for sell on your showroom.
        menu:
            1.Corolla
            2.Yaris
            3.Grande
            Enter your selection:
    step5: if the user selects any car show tham all details about that car and
           thanks for shopping message.

'''



mylist = ["a1","a2","a3"]

for index,item in enumerate(mylist):
    print(f"{index+1}. {item}")

















