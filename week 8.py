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



mylist = [1,22,34,55,67,93,55]
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
mylist.sort(reverse = True)
print(mylist)










