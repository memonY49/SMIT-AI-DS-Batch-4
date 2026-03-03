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
'''

for row in range(5):
    for col in range(1,6):
        print(col,end = '')
    print()



















    
