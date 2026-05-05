import collections as col
import queue


# myqueue = col.deque([3,6])

# myqueue.appendleft(0)
# myqueue.appendleft(4)
# myqueue.appendleft(8)
# myqueue.appendleft(0)

# print(myqueue)


# mycounterlist = col.Counter(["hen","bread","chiken","hen"])

# print(mycounterlist['hen'])

# mycounterlist2 = col.Counter({"cat":2,"dogs":4})

# print(mycounterlist2["eggs"])

# mycounterlist3 = col.Counter("allopmnnyy")

# print(mycounterlist3['y'])

# mycounterlist4 = col.Counter([["a","c","f"],["c","g","f"],["e","t","y"]])




mystack = queue.LifoQueue(maxsize=5)
mystack.put(4)
mystack.put(7)
mystack.put(9)
mystack.put(0)
mystack.put(10)

print(mystack.full())
print(mystack.get())
print(mystack.full())