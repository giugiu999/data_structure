#----------------------------------------------------
# Stack implementation #2 
# (Top of stack corresponds to back of list)
# 
# Author: CMPUT 175 team
# Updated by:
#----------------------------------------------------

class Stack:
    def __init__(self,capacity):
        self.items = []
        self.capacity = capacity
    
    def get(self,item):
        if item >= self.size():
            return None
        return self.items[item]

    def push(self, item):
        self.items.append(item)

    # MODIFY: RAISE AN EXCEPTION IF THIS METHOD IS INVOKED ON AN EMPTY STACK
    def pop(self):      
        if len(self.items) == 0:
            raise Exception("Cannot pop from an empty stack")
        return self.items.pop()
    
    # MODIFY: RAISE AN EXCEPTION IF THIS METHOD IS INVOKED ON AN EMPTY STACK
    def peek(self):     
        if len(self.items) ==0:
            raise Exception("Cannot peek from an empty stack")

        return self.items[-1]

    
    def isEmpty(self):
        return self.items == []
    
    def size(self):
        return len(self.items)
    
    def isFull(self):
        return len(self.items) == self.capacity
    
    def show(self):
        print(self.items)

    def is_sealed(self,CHEMICAL_UNITS):
        if len(set(self.items)) == 1 and len(self.items) == CHEMICAL_UNITS:
            return True
        else:
            return False
    
    def __str__(self):
        stackAsString = ''
        for item in self.items:
            stackAsString += item + ' '
        return stackAsString
    
    def clear(self):
        #TO DO: complete method according to updated ADT
        self.items = []