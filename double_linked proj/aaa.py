class Node:
    def __init__(self, item, next_node=None, previous_node=None) -> None:
        self.data = item
        self.previous = previous_node
        self.next = next_node

        if next_node != None:
            self.next.previous = self
        if previous_node != None:
            self.previous.next = self

    def getNext(self):
        return self.next

    def getPrevious(self):
        return self.previous

    def getData(self):
        return self.data

    def setData(self, data):
        self.data = data

    def setNext(self, node):
        self.next = node

    def setPrevious(self, node):
        self.previous = node


class CircularDoublyLinkedList:
    def __init__(self, capacity) -> None:
        assert type(capacity) == int, "Capacity of CDLL should be int"
        assert capacity > 0, "Capacity of CDLL should be > 0"
        self.__head = None
        self.__tail = None
        self.__capacity = capacity
        self.__size = 0

    def size(self):
        return self.__size
    
    def getHead(self):
        return self.__head
    
    def getTail(self):
        return self.__tail

    def isEmpty(self):
        return self.__size == 0

    def isFull(self):
        return self.__size == self.__capacity

    def __str__(self):
        output = "["
        if self.isEmpty():
            return "CDLL is empty"
        current = self.__head
        loop = True
        while loop:
            output += str(current.getData()) + ", "
            current = current.getNext()
            if current == self.__head:
                loop = False
        return output + "]"

    
    def get(self,index):
        current = self.__head
        for _ in range(index):
            current = current.getNext()
        return current


    def insert(self,position: int, data ):
        """
        Insert an item into the CDLL
        """
        assert self.__size < self.__capacity, "insert(): size>capacity"
        assert position >= 0, "insert(): position<0"
        assert position <= self.__size, "insert(): postition>size"
        new_node = Node(data, None, None)
        if self.isEmpty():  # empty CDLL
            self.__head = new_node
            self.__tail = new_node
            new_node.setNext(new_node)
            new_node.setPrevious(new_node)
        else:
            if position == 0:  # the first element
                new_node.setNext(self.__head)
                new_node.setPrevious(self.__tail)
                self.__head.setPrevious(new_node)
                self.__tail.setNext(new_node)
                self.__head = new_node
            elif position == self.__size:  # the last element
                new_node.setNext(self.__head)
                new_node.setPrevious(self.__tail)
                self.__head.setPrevious(new_node)
                self.__tail.setNext(new_node)
                self.__tail = new_node
            else:
                current = self.__head
                for _ in range(position - 1):
                    current = current.getNext()
                new_node.setNext(current.getNext())
                new_node.setPrevious(current)
                current.setNext(new_node)
                current.getNext().getNext().setPrevious(new_node)
        self.__size += 1

    def pop(self,position=None):
        assert self.__size > 0, 'pop(): size of cdll <0'
        if position == None:
            position = self.__size-1
        assert position < self.__size and position >=0 , 'pop(): out of range'
        if self.__size == 1: # if only one item
            data = self.__head.getData()
            self.__head = None
            self.__tail = None
        # if multiple items in the cdll
        else:
            if position == 0: # pop the first one
                data = self.__head.getData()
                self.__head = self.__head.getNext()
                self.__head.setPrevious(self.__tail)
                self.__tail.setNext(self.__head)
            else:
                current = self.__head
                for _ in range(position):
                    current = current.getNext()
                if current == self.__tail: # pop the last one
                    data = self.__tail.getData()
                    self.__tail.getPrevious().setNext(self.__head)
                    self.__head.setPrevious(self.__tail.getPrevious())
                    self.__tail = self.__tail.getPrevious()
                else: # pop the middle one
                    data = current.getData()
                    current.getPrevious().setNext(current.getNext())
                    current.getNext().setPrevious(current.getPrevious())
        self.__size -= 1
        return data


if __name__ == '__main__':
    c = CircularDoublyLinkedList(5)
    c.insert(0,'a')
    c.insert(0,'b')
    c.insert(2,'c')
    print(c)
    c.insert(0,'e')
    c.insert(1,'f')
    print(c.get(1).getPrevious().data)
    print(c.get(1).getNext().data)
    print(c) # efbac
    print(c.get(2).getPrevious().data)
    print(c.get(2).getNext().data)
    c.pop(0)
    c.pop()
    print(c)
    c.pop(2)
    print(c)
    print(c.size())
    # //
    print(c.get(1).getNext().data)
    print(c.get(1).getPrevious().data)
    c.pop()
    print(c.size())
    print(c)
    c.pop()
    print(c)

