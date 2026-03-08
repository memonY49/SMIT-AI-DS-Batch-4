'''
 Create an atm note counting program that takes a number as an input
 from the user and prints how many 5000, 1000 and 500 notes are there
 in the number. 
- Example: 9500 is a number from the user which includes 1 note from5000,
  4 notes of 1000 and 1 note for 500.
- Note: add a restriction to the user to enter a
  number that is a multiple of 500 only.


while True:
    print('*'*20)
    print('1.note counter.\n0.exit')
    user_selection = int(input("Enter your selection: "))

    if user_selection == 1:
        while True:
            amount = int(input("Please enter your number: "))
            note5000 = 0
            note1000 = 0
            note500 = 0
        
            if amount % 500 == 0:
                note5000 = int(amount/5000)
                amount = amount%5000
        
                note1000 = amount//1000
                amount = amount%1000
        
                note500 = amount/500
        
                print(f"note for 5000: {note5000}")
                print(f"note for 1000: {note1000}")
                print(f"note for 500: {note500}")
                break
            else:
                print("Invailed entry!!!")
                
    elif user_selection == 0:
        exit(0)
'''

'''
Nasted Loops:
    Loop inside a loop.
    syntax:
        for counter1 in range():
            #body of outer loop
            for counter2 in range():
                #body of inner loop


12345
12345
12345
12345
12345


1
12
123
1234
12345





for row in range(3):
    for col in range(1,6):
        print(col,end = '')
    print('')

'''



"""
step1: Add three options at start where options are:
        1.Login
        2.check user
        0.exit
step2: Create a user log in program where you need to store 5 variables
        named as(Name,Fname,Email,Cnic and pass)
step3: than takes 2 variables as an input for useremail and userpass
        if password is matched print all details of that user.
step4: if the user enters incorrect pass for 3 times you need to show a
        message
        "You had entered wrong password for 3 time and you are blocked.
        please call the helpline".
"""
while True:
    selection = int(input("1.Login\n2.Check user\n0.Exit\n\
Please enter your selection: "))
    name = 'abc'
    fname = 'efg'
    cnic = '5376782963'
    email = 'abc@gmail.com'
    password = 'abc123'
    status = 'unblocked'

    if selection == 1:
        useremail = input("Please Enter your email: ")
        if status == 'unblocked'
            if useremail == email:
                for i in range(1,4):
                    userpass = input("Please Enter your pass: ")
                    if userpass == password:
                        print(f"Name: {name}\nFname: {fname}\nCnic: {cnic}\nEmail: {email}")
                        break
                    else:
                        print(f"Incorrect Password {i}..")
                else:
                    print("You had entered wrong password for 3 time and you are blocked. \
                    please call the helpline")
                    status = 'blocked'
    elif selection == 2:
        useremail = input("Please Enter your email: ")
        if useremail == email:
            print(f"Your account is {status}")
    elif selection == 0:
        exit()
    else:
        print("Wrong selection...")






















    
