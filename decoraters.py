from datetime import datetime as dt
# def greet():
#     print("Hello")
#     def desplymessage():
#         print("This is the class from SMIT")
#     desplymessage()

# greet()


def greeting_decorator(func):
    def wrapper(*args,**kwargs):
        print("Hello!! Welcome to SMIT.")
        func(*args,**kwargs)
        print("Goodbye!! Thank you for visiting SMIT.")
    return wrapper

def confirmation_decorator(func):
    def wrapper(*args,**kwargs):
        user_in = input("Press y to confirm your transecion: ")
        if user_in.lower() == 'y':
            func(*args,**kwargs)
    return wrapper

def logs(func):
    def wrapper(*args,**kwargs):
        with open("logs.txt","a") as file:
            file.write(f"{dt.now()}:: {func.__name__} function is called.\n")
        func(*args,**kwargs)
    return wrapper

@greeting_decorator
@logs
@confirmation_decorator
def desplaymessage(message:str,message2 = ""):
    print(message,message2)

desplaymessage("This is Yasir Nawaz.",message2="From SMIT")

# Create two variables Account Title and Balance.
# Add 4 function Check Balance, view account title, withdraw and deposit.
# Add 2 decorators to all the function of an atm system Greet the user with 
# there name and ask for the confirmation to the user.