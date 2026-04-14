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

"""

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

























