class DLinkedListNode:
    # An instance of this class represents a node in Doubly-Linked List
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


class DLinkedList:
    # An instance of this class represents the Doubly-Linked List
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__size = 0

    def search(self, item):
        current = self.__head
        found = False

        while current != None and not found:
            if current.getData() == item:
                found = True

            else:
                current = current.getNext()

        return found

    def index(self, item):
        current = self.__head
        found = False
        index = 0

        while current != None and not found:
            if current.getData() == item:
                found = True

            else:
                current = current.getNext()
                index = index + 1

        if not found:
            index = -1

        return index

    def add(self, item):
        # adds the item to the start of the list
        # TODO
        temp = DLinkedListNode(item, self.__head, None)
        if self.__head != None:
            self.__head.setPrevious(temp)
        self.__head = temp
        if self.__tail is None:
            self.__tail = temp
        self.__size += 1


    def remove(self, item):
        # removes the first element in the list that is equal to the item
        # TODO
        current = self.__head
        while current is not None:
            if current.getData() == item:
                if current == self.__head:
                    self.__head = current.getNext()
                    if self.__head is not None:
                        self.__head.setPrevious( None )
                else:
                    current.getPrevious().setNext( current.getNext() )
                    if current.getNext() is not None:
                        current.getNext().setPrevious( current.getPrevious() )
                    else:  # Removing the tail
                        self.__tail = current.getPrevious()
                self.__size -= 1
                return  # Item found and removed
            current = current.getNext()

    def append(self, item):
        # adds a new node to the tail of the list with item as its data
        # TODO
        new_node = DLinkedListNode( item, None, self.__tail )
        if self.__tail is not None:
            self.__tail.setNext( new_node )
        self.__tail = new_node
        if self.__head is None:  # List was empty
            self.__head = new_node
        self.__size += 1

    def insert(self, pos, item):
        # adds a new node at the given position with item as its data.
        # TODO position must be an integer
        assert type(pos) == int,'pos is not an integer'
        # TODO position must be non-negative
        assert pos >= 0,'pos is negative'
        # TODO implement this method
        if pos == 0:
            self.add(item)
        elif pos == self.__size:
            self.append(item)
        else:
            new_node = DLinkedListNode(item, None,None)
            current = self.__head
            for i in range(pos - 1):
                current = current.getNext()
            
            new_node.setNext(current.getNext())
            current.getNext().setPrevious(new_node)
            current.setNext(new_node)
            new_node.setPrevious(current)
            self.__size += 1

    def pop1(self):
        # removes and returns the last item in the list
        # TODO
        a = self.__tail
        self.remove(self.__tail)
        self.__size -=1
        return a

    def pop(self, pos=None):
        #  removes and returns the item in the given position.
        # TODO
        if self.__head is None:
            raise IndexError("pop from empty list")

        if pos is None:
            pos = self.__size - 1

        if pos < 0 or pos >= self.__size:
            raise IndexError("pos is out of range")

        current = self.__head
        for i in range(pos):
            current = current.getNext()

        item = current.getData()

        if current.getPrevious() is None:
            self.__head = current.getNext()
            if self.__head is not None:
                self.__head.setPrevious(None)
        else:
            current.getPrevious().setNext(current.getNext())
            if current.getNext() is not None:
                current.getNext().setPrevious(current.getPrevious())

        self.__size -= 1

        return item


    def searchLarger(self, item):
        '''
        returns the position of the first element that is larger than the item
        else: -1
        '''
        # TODO
        current = self.__head
        found = False
        index = 0
        while current != None and not found:
            if current.getData() > item:
                found = True
            else:
                current = current.getNext()
                index += 1
        if not found:
            index = -1
        return index

    def getSize(self):
        '''
        returns the number of elements in the list.
        '''
        # TODO
        size = self.__size
        return size

    def getItem(self, pos):
        '''
        returns the item at the given position. 
        An exception should be raised if the position is
        outside of the list. 
        pos must be an integer, and it can be positive OR Negative.
        '''
        # returns the item at the given position.
        # TODO
        if pos > self.getSize():
            raise Exception('the position is outside of the list.')
        if type(pos) != int:
            raise Exception('pos is not an integer')
        if pos <0:
            pos = self.__size + pos

        current = self.__head
        count = 0
        
        while count != pos:
            current = current.getNext()
            count += 1
        
        return current.getData()



    def __str__(self):
        # create the string representation of the linked list
        # TODO
        current = self.__head
        string = ''
        while current is not None:
            string += str(current.getData()) + ' '
            current = current.getNext()
        return string.strip()
        

def test():

    linked_list = DLinkedList()

    is_pass = (linked_list.getSize() == 0)
    assert is_pass == True, "fail the test"

    linked_list.add("World")
    linked_list.add("Hello")

    is_pass = (str(linked_list) == "Hello World")
    assert is_pass == True, "fail the test"

    is_pass = (linked_list.getSize() == 2)
    assert is_pass == True, "fail the test"

    is_pass = (linked_list.getItem(0) == "Hello")
    assert is_pass == True, "fail the test"

    is_pass = (linked_list.getItem(1) == "World")
    assert is_pass == True, "fail the test"

    is_pass = (linked_list.getItem(0) ==
               "Hello" and linked_list.getSize() == 2)
    assert is_pass == True, "fail the test"
    x = linked_list.pop(1)
    is_pass = (x == "World")
    assert is_pass == True, "fail the test"

    is_pass = (linked_list.pop() == "Hello")
    assert is_pass == True, "fail the test"

    is_pass = (linked_list.getSize() == 0)
    assert is_pass == True, "fail the test"

    int_list2 = DLinkedList()

    for i in range(0, 10):
        int_list2.add(i)
    int_list2.remove(1)
    int_list2.remove(3)
    int_list2.remove(2)
    int_list2.remove(0)
    is_pass = (str(int_list2) == "9 8 7 6 5 4")
    assert is_pass == True, "fail the test"

    for i in range(11, 13):
        int_list2.append(i)
    is_pass = (str(int_list2) == "9 8 7 6 5 4 11 12")
    assert is_pass == True, "fail the test"

    for i in range(21, 23):
        int_list2.insert(0, i)
    is_pass = (str(int_list2) == "22 21 9 8 7 6 5 4 11 12")
    assert is_pass == True, "fail the test"
    x = int_list2.getSize()
    is_pass = (int_list2.getSize() == 10)
    assert is_pass == True, "fail the test"

    int_list = DLinkedList()

    is_pass = (int_list.getSize() == 0)
    assert is_pass == True, "fail the test"

    for i in range(0, 1000):
        int_list.append(i)
    correctOrder = True

    is_pass = (int_list.getSize() == 1000)
    assert is_pass == True, "fail the test"

    for i in range(0, 200):
        if int_list.pop() != 999 - i:
            correctOrder = False

    is_pass = correctOrder
    assert is_pass == True, "fail the test"

    is_pass = (int_list.searchLarger(200) == 201)
    assert is_pass == True, "fail the test"

    int_list.insert(7, 801)
    x = int_list.searchLarger(800)
    is_pass = (int_list.searchLarger(800) == 7)
    assert is_pass == True, "fail the test"

    x = int_list.getItem(-1)
    is_pass = (int_list.getItem(-1) == 799)
    assert is_pass == True, "fail the test"

    is_pass = (int_list.getItem(-4) == 796)
    assert is_pass == True, "fail the test"

    if is_pass == True:
        print("=========== Congratulations! Your have finished exercise 2! ============")


if __name__ == '__main__':
    test()
