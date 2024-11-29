class BoundedQueue: 
    # Creates a new empty queue:
    def __init__(self, capacity): 
        self.__items = [] # init the  list / queue as empty
        self.__capacity = capacity
 
    # Adds a new item to the back of the queue, and returns nothing:
    def enqueue(self, item): 
        '''
        Enqueue the element to the back of the queue
        :param item: the element to be enqueued
        :return: No returns
        '''
        if len(self.__items) < self.__capacity:
            self.__items.append(item)
        else:
            raise Exception('Error: Queue is full')
        '''
        Remember to check the conditions
        '''

        #####  END CODE HERE ######
        
    # Removes and returns the front-most item in the queue.      
    # Returns nothing if the queue is empty.    
    def dequeue(self):        
        '''
        Dequeue the element from the front of the queue and return it
        :return: The object that was dequeued
        '''

        ##### START CODE HERE #####
        '''
        1. remember to check the conditions
        2. return the appropriate value
        '''

        if len(self.__items) > 0:
            return self.__items.pop(0)
        else:
            raise Exception('Error: Queue is empty')
        #####  END CODE HERE ######
    
    # Returns the front-most item in the queue, and DOES NOT change the queue.      
    def peek(self):        
        if len(self.__items) <= 0:            
            raise Exception('Error: Queue is empty')        
        return self.__items[0]
        
    # Returns True if the queue is empty, and False otherwise:    
    def isEmpty(self):
        return len(self.__items) == 0        
    
    # Returns True if the queue is full, and False otherwise:    
    def isFull(self):
        return len(self.__items) == self.__capacity
    
    # Removes all items from the queue, and sets the size to 0    
    # clear() should not change the capacity    
    def clear(self):        
        self.__items = []

    # Returns a string representation of the queue: 
    def __str__(self):               
        str_exp = ""        
        for item in self.__items:            
            str_exp += (str(item) + " ")                    
        return str_exp
        
    # Returns a string representation of the object bounded queue: 
    def __repr__(self):               
        return  str(self) + " Max=" + str(self.__capacity)   