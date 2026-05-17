"""
Magic Methods: These methods are used without directly calling the method name.
"""

class calculate:
    def __init__(self,numbers: list):
        self.numbers = numbers
        
    def __len__(self):
        return len(self.numbers)
    def __str__(self):
        return"This is the object of Calculator"
    def __repr__(self):
        return"This is the object of Calculator"
    def __add__(self, other):
        new_list = self.numbers
        new_list.extend(other.numbers)
        return new_list
    def __sub__(self, other):
        set1 = set(self.numbers)
        set2 = set(other.numbers)
        return list(set1.union(set2) - set1.intersection(set2))
        # newlist = []
        # for x,y in zip(self.numbers,other.numbers):
        #     if x not in other.numbers:
        #         newlist.append(x)
        #     if y not in self.numbers:
        #         newlist.append(y)
        # return newlist
    def __mul__(self, other):
        return None
    def __divmod__(self, other):
       pass 
    def __mod__(self, other):
        pass
    def __iadd__(self, other):
        self.numbers.extend(other.numbers)
        self.numbers = list(set(self.numbers))
        return self
    def __isub__(self, other):
        pass

cal = calculate([3,6])
cal1 = calculate([4,6])

# print(len(cal))
# print(cal)
cal += cal1
print(cal.numbers)
# print(cal - cal1)

"""
# 1) Smart Shopping Cart (Operator Overloading)
- A shopping cart should behave like a real object.
- You must allow adding items with +, removing using -, and printing in a readable way.
    - Requirements
        - Class Cart holds items (name, price, qty)
        - cart + item → adds item
        - cart - item → removes item (if exists)
        - str(cart) shows total items & bill
"""

class cart:
    def __init__(self):
        self.items = []
        self.total_bill = 0
    def __iadd__(self, other):
        self.items.append(other)
        self.total_bill += other["price"]*other["qty"]
        return self
    

    def __isub__(self, other):
        # if other in self.items:
            # self.items.pop(self.items.index(other))
        #     self.items.remove(other)
        # self.total_bill -= other["price"]*other["qty"]
        if other-1 < len(self.items) and other-1 > -1:
            self.total_bill -= self.items[other-1]["price"]*self.items[other-1]["qty"]
            self.items.pop(other-1)
        return self
    


    def __str__(self):
        recipt = ""
        # for index,item in enumerate(self.items):
        #     recipt += f"item no: {index+1}\n"
        #     for k,v in item.items():
        #         recipt += f"{k}: {v}\n"
        #     sub_total = item["price"]*item["qty"]
        #     recipt += f"sub total: {sub_total}\n"
        #     recipt += "*"*10+"\n"
        # recipt += f"total: {self.total_bill}"
        for index,item in enumerate(self.items):
            detail = list(item.values())
            recipt += f"{index+1} || {detail[0]} || {detail[1]} || {detail[2]}\n"
        recipt += f"total items: {len(self.items)} || total bill: {self.total_bill}"
        return recipt
    
mycart = cart()
mycart += {"name":"watch","price":1500,"qty":1}
mycart += {"name":"brush","price":30,"qty":10}

# mycart -= {"name":"brush","price":30,"qty":10}
# mycart -= 2
print(mycart)