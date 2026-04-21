"""Exception handling:
    Exception means an error.
        types of error:
            1. Syntax error
            2. Logical error
    -> we had two clauses in EH.
        1. try : we provide the code to try if there is an error.
        2. except : except cluase will only be executed
                    when there is an error in try cluase

try:
    a = int(input())
except Exception as e:
    print("Invailid input!!!",e)



data = {"Name":"Yasir",
        "Balance": 1000000,
        "Pin":1001}
while(True):
    while(True):
        try:
            userpin = int(input("Please enter your pin: "))
            break
        except:
            print("invalid Pin.")
    
    if userpin == data['Pin']:
        while(True):
            print("1. Check Balance")
            print("2. Withdraw")
            print("3. Deposit")
            print("4. Exit")
            while(True):
                try:
                    userselection = int(input("Enter your selection: "))
                    break
                except:
                    print("Invalid Selection!!!")
            if userselection == 1:
                print("Your balance is:",data['Balance'])
            elif userselection == 2:
                try:
                    amount = int(input("Enter amount to withdraw"))
                    if amount < data['Balance']:
                        if amount >= 500 and amount%500 == 0:
                            data['Balance'] -= amount
                            print("Withdraw is succesful!!!")
                        else:
                            print("amountmust be a multiple of 500...")
                    else:
                        print("Insuficeint Balance!!!")
                except:
                    print("Invalid amount!!")
            elif userselection == 3:
                try:
                    amount = int(input("Enter amount to deposit"))
                    data['Balance'] += amount
                    print("Deposit is succesful!!!")
                except:
                    print("Invalid amount!!")
            elif userselection == 4:
                exit(0)
            else:
                print("Please select a number from above...")
    else:
        print("Wrong Pin..")
    
"""

"""
File Handling:
    Open
"""
'''
#read
try:
    useremail = input("Enter your Email: ")
    userpass = input("Enter your Password: ")
    file = open("data.txt",'r')
    # print(file.read())
    # print(file.readline().strip().split(','))
    for line in file.readlines():
        user = line.strip().split(',')
        if user[4] == useremail and user[5] == userpass:
            print(user)
    file.close()
except FileNotFoundError as e:
    print("Wromg File name!")
'''
'''
write'''

# name = input("Enter your Name: ")
# fname = input("Enter your FName: ")
# phone = input("Enter your Phone: ")
# email = input("Enter your Email: ")
# password = input("Enter your Password: ")
# file = open('data.csv','a')
# # data = f"{name},{fname},{phone},{email},{password}\n"
# listdata = ["ali,ahmed,892374209213,ahmed@gmail.com,ali123\n",
#             "zeeshan,ali,09797892789,zeeshan@gmail.com,zeeshan123\n"]
# file.writelines(listdata)
# file.close()


# data = [['Yasir','Nawaz','abc@gmail.com','abc123'],
#         ['Yasir1','Nawaz','abc1@gmail.com','abc123'],
#         ['Yasir2','Nawaz','abc2@gmail.com','abc123'],
#         ['Yasir3','Nawaz','abc3@gmail.com','abc123']]

# with open('data.csv','a') as file:
#     for user in data:
#         file.write(','.join(user)+'\n')

# mylist = ['Yasir','nawaz','76783478348673','abc@gmail.com']
# print(','.join(mylist))
# print(mylist)




# Task:
# Create a data.txt file for storing details for atleast 5 users.
# (uid, name, email, phone, cnic)
# create a program for updating user details by user id

# uid = input("Please enter user id to update: ")
# data = []
# with open("data.csv","r") as file:
#     # data = [ line.strip().split(',') for line in file.readlines()]
#     for line in file.readlines():
#         data.append(line.strip().split(','))


# for i in range(0,len(data)):
#     if data[i][0] == uid:
#         name = input("Enter your Name: ")
#         fname = input("Enter your FName: ")
#         email = input("Enter your Email: ")
#         password = input("Enter your Password: ")
#         data[i][1] = name
#         data[i][2] = fname
#         data[i][3] = email
#         data[i][4] = password

# with open("data.csv",'w') as file:
#     # print([",".join(user) for user in data])
#     strdata = []
#     for user in data:
#         strdata.append(",".join(user)+"\n")
#     file.writelines(strdata)
        

# r+,w+ and a+ modes

with open("data.csv","a+") as file:
    # end = len(file.read())
    # file.seek(end+1)
    # file.write("THE END")\
    file.seek(0)
    print(file.read())




















