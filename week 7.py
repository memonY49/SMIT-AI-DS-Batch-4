'''
List: A collection of hetrogenius data type elements.
    Syntax:
            MyList = [10,30,'h',True,7.8]

mylist = [10,30,'h',True,7.8]

mylist[2] = 't'

print(mylist[2])
'''
#Task: Create a a list of user details include (Name,FNAme,CNIC,Phone,Add,
# Email and Pass)
#step 2: Email and Pass match using list

data = ["Yasir","abc@gmail.com",'abc123']
label = ['Name','Email','Pass']
useremail = input("Enter your email: ")
userpass = input("Enter your Pass: ")
if useremail == data[1] and userpass == data[2]:
    #using len function we can count all the elements of a list
    #for i in range(0,len(data)):
    #    print(label[i]+":",data[i])

    for j, i in zip(label,data):
        print(j,i)













