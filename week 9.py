'''
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


cardata = [[['Toyota','Corolla1','GLI','2007',1300000],
            ['Toyota','Corolla2','XLI','2008',1400000],
            ['Toyota','Corolla3','GLI','2006',1250000]],
           [['Suzuki','Mehran1','VXR','2008',700000],
            ['Suzuki','Mehran2','VXR','2000',400000],
            ['Suzuki','Mehran3','VXR','2007',650000],],
           [['Kia','Sportage1','Alpha','2023',7500000],
            ['Kia','Sportage2','Alpha','2022',6800000],
            ['Kia','Sportage3','Alpha','2023',7500000]]]

print("1. Buy \n2.Sell \n0.Exit")
select = int(input("Please select your desired menu: "))
if select == 1:
    #company selection
    for company in range(len(cardata)):
        print(f'{company+1}.',cardata[company][0][0])
    scomp = int(input("Please select your desired menu: "))
    
    #car selection
    for car in range(len(cardata[scomp-1])):
        print(f'{car+1}.',cardata[scomp-1][car][1])
    scar = int(input("Please select your desired menu: "))
    
    #car details
    print(cardata[scomp-1][scar-1])
    
elif select == 2:
    pass
elif select == 0:
    exit(0)
'''

"""
example = [[30,50,60,70,20],
           [30,50,60,70,20]]
1. Student Marks System
-> Store marks of students (rows = students, columns = subjects)
Find:
    1. average per student
    2. topper student

data = [[78,78,70,72,78],
        [60,80,82,70,81],
        [70,75,85,80,90],
        [70,75,85,80,90]]

result = []
average = []
top = []
for std in data:        #row loop
    total = 0
    for marks in std:   #column loop
        total += marks
    result.append(total)
    average.append(total/5)

for i in range(len(result)):
    if result[i] >= max(result):
        top.append(i)
    
print("average:",average)
print("topers:",top)
"""
"""
2. Tic Tac Toe Board
    -> Represent board using 2D list
    -> Check winner


board = [[" "," "," "],
         [" "," "," "],
         [" "," "," "]]
moves = 1
while(moves<=9): #move count loop
    for pl in range(1,3): # two player loop
        #board print
        #--------------
        for row in board:
            for col in row:
                print(col,'|',end = '')
            print("\n--+--+--")
        #--------------
        # player selection
        #--------------
        while (True):
            sr = int(input("enter row: "))
            sc = int(input("enter column: "))
            if board[sr][sc] != " ":
                print("selection already selected...!")
            elif pl == 1:
                board[sr][sc] = "O"
                moves+=1
                break
            else:
                board[sr][sc] = "X"
                moves+=1
                break
            
        #--------------
        # winner check by 8 conditions
        #--------------
        if board[0][0] == board[0][1] == board[0][2] != " ":
            print("winner player",pl)
            exit(0)
        elif board[1][0] == board[1][1] == board[1][2] != " ":
            print("winner player",pl)
            exit(0)
        elif board[2][0] == board[2][1] == board[2][2] != " ":
            print("winner player",pl)
            exit(0)
        elif board[0][0] == board[1][0] == board[2][0] != " ":
            print("winner player",pl)
            exit(0)
        elif board[0][1] == board[1][1] == board[2][1] != " ":
            print("winner player",pl)
            exit(0)
        elif board[0][2] == board[1][2] == board[2][2] != " ":
            print("winner player",pl)
            exit()
        elif board[0][0] == board[1][1] == board[2][2] != " ":
            print("winner player",pl)
            exit(0)
        elif board[0][2] == board[1][1] == board[2][0] != " ":
            print("winner player",pl)
            exit(0)
        #--------------
print("draw.........")
"""
"""
Dictionary: A collection of key and value pairs.
 syntax:
         mydict = {"key1":"value","key2":"value"}
functions:
    1. keys()
    2. values()
    3. items()

mydict = {"name":"Yasir",
          "fname":"Nawaz",
          "phone":"03003000000",
          "pass":True,
          "marks":890}
mydict['add'] = "hvdjcgascydgvcjwvjwhdm"

sortedkeys = list(mydict.items())
#sortedkeys.sort()
#print(sortedkeys)

for k,v in mydict.items():
    print(f"{k} : {v}")


data = [{"name":"Yasir",
          "fname":"Nawaz",
          "phone":"03003000000",
          "pass":True,
         'email':"yasir123@gmail.com",
         'password':'abc123',
          "marks":890},
        {"name":"Ahmed",
          "fname":"Faraz",
          "phone":"03003000000",
          "pass":True,
         'email':"ahmed123@gmail.com",
         'password':'abc123',
          "marks":890},
        {"name":"Ali",
          "fname":"Parvez",
          "phone":"03003000000",
          "pass":True,
         'email':"ali123@gmail.com",
         'password':'abc123',
          "marks":890}]

useremail = input("Enter your email:")
userpass = input("Enter your pass:")

for user in data:
    if useremail == user['email'] and userpass == user['password']:
        print('*'*10)
        for k,v in user.items():
            print(f"{k} : {v}")
        break
else:
    print("user not found!!")
"""
'''
data = {"u1":{"name":"Yasir",
             "fname":"Nawaz",
             "phone":"03003000000",
             "pass":True,
             'email':"yasir123@gmail.com",
             'password':'abc123',
              "marks":890},
        "u2":{"name":"Ahmed",
            "fname":"Faraz",
            "phone":"03003000000",
            "pass":True,
            'email':"ahmed123@gmail.com",
            'password':'abc123',
            "marks":890},
        "u3":{"name":"Ali",
            "fname":"Parvez",
            "phone":"03003000000",
            "pass":True,
           'email':"ali123@gmail.com",
           'password':'abc123',
           "marks":890}}

#print(data['u2']['name'])

useremail = input("Enter your email:")
userpass = input("Enter your pass:")

for userid, uservalue in data.items():
    if useremail == uservalue['email'] and userpass == uservalue['password']:
        print('*'*10)
        for k,v in uservalue.items():
            print(f"{k} : {v}")
        break
else:
    print("user not found!!")

'''
data = [{"name":"Yasir",
          "fname":"Nawaz",
          "phone":"03003000000",
          "pass":True,
         'email':"yasir123@gmail.com",
         'password':'abc123',
          "marks":890},
        {"name":"Ahmed",
          "fname":"Faraz",
          "phone":"03003000000",
          "pass":True,
         'email':"ahmed123@gmail.com",
         'password':'abc123',
          "marks":890},
        {"name":"Ali",
          "fname":"Parvez",
          "phone":"03003000000",
          "pass":True,
         'email':"ali123@gmail.com",
         'password':'abc123',
          "marks":890}]

listnames = [(std['name'],std['email']) for std in data]
print(listnames)

#mylist = [x for x in range(1,101)]
#print(mylist)





