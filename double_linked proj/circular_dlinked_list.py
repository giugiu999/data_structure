class DLinkedListNode:
    '''
    node operation
    '''
    def __init__(self, initData, initNext, initPrevious):
        self.data = initData
        self.next = initNext
        self.previous = initPrevious

        if initNext != None:
            self.next.previous = self
        if initPrevious != None:
            self.previous.next = self

    def getData(self):
        return self.data

    def setData(self, newData):
        self.data = newData

    def getNext(self):
        return self.next

    def getPrevious(self):
        return self.previous

    def setNext(self, newNext):
        self.next = newNext

    def setPrevious(self, newPrevious):
        self.previous = newPrevious

class CircularDoublyLinkedList:
    '''
    circular d_linked list operation
    '''
    def __init__(self,capacity) -> None:
        assert type(capacity) == int, 'CDLL __init__: capacity is not an int'
        assert capacity > 0, 'CDLL __init__: capacity is not positive'
        self.__head = None
        self.__tail = None
        self.__size = 0
        self.__capacity = capacity

    def isEmpty(self) -> bool:
        return self.__size == 0
    
    def isFull(self) -> bool:
        return self.__size == self.__capacity
    
    def size(self) ->int:
        return self.__size
    
    def getdata(self,pos):
        current = self.__head
        for _ in range(pos):
            current = current.getNext() 
        return current.getData()
    
    def add(self,item,pos) -> None:
        """
        add an item in proper postion
        input:
            item: 
            pos: integer
        """
        assert self.__size +1 <= self.__capacity, 'CDLL is full'
        assert type(pos) == int, 'CDLL add(): position is not an int'
        assert pos>=0, 'CDLL add(): position is not positive'
        assert pos <= self.__size, 'position is out of range'
        new_node = DLinkedListNode(item,None,None)
        if self.__size == 0: # empty
            self.__head = new_node
            self.__tail = new_node
            new_node.setNext(new_node)
            new_node.setPrevious(new_node)
        elif pos == 0: # not empty, pos = 0
            self.__head.setPrevious(new_node)
            new_node.setNext(self.__head)
            new_node.setPrevious(self.__tail)
            self.__tail.setNext(new_node)
            self.__head = new_node
        elif pos == self.__size: # pos = the last one
            self.__tail.setNext(new_node)
            new_node.setNext(self.__head)
            new_node.setPrevious(self.__tail)
            self.__head.setPrevious(new_node)
            self.__tail = new_node
        else: # insert
            current = self.__head
            cnt=0
            while cnt != pos -1:
                current = current.getNext()
                cnt += 1
            new_node.setNext(current.getNext())
            current.getNext().setPrevious(new_node)
            current.setNext(new_node)
            new_node.setPrevious(current)
        self.__size += 1

    def pop(self, pos) -> None:
        """
        delete an item in proper position
        input:
            pos: integer
        """
        assert self.__size > 0, 'CDLL is empty'
        assert type(pos) == int, 'CDLL pop(): position is not an int'
        assert pos >= 0, 'CDLL pop(): position is not positive'
        assert pos < self.__size, 'position is out of range'  # Corrected boundary check

        if self.__size == 1:
            self.__head = None
            self.__tail = None
        else:
            if pos == 0:  # pop the head
                self.__head = self.__head.getNext()
                self.__head.setPrevious(self.__tail)
                self.__tail.setNext(self.__head)
            elif pos == self.__size - 1:  # Corrected condition for popping the tail
                self.__tail = self.__tail.getPrevious()
                self.__tail.setNext(self.__head)
                self.__head.setPrevious(self.__tail)
            else:  # pop in the middle of the list
                current = self.__head
                for _ in range(pos):
                    current = current.getNext()
                current.getPrevious().setNext(current.getNext())
                current.getNext().setPrevious(current.getPrevious())
        self.__size -= 1

    def __str__(self):
        '''
        show in the format of string
        '''
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

if __name__ == '__main__':
    '''
    test
    '''
    c = CircularDoublyLinkedList(5)
    c.add('o',0)
    c.add('l',0)
    print(c)
    c.pop(0)
    print(c)
    

