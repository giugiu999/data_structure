from bqueue import BoundedQueue
from bstack import Stack
import os
import time

'''GLOBAL VARIABLE'''
CHEMICAL_UNITS = 3
FLASKS_SIZE = 4
CHEM_QUEUE_SIZE = 4
FLASK_CAPACITY = 4

ANSI = {
    'AA': "\033[41m",
    'BB': "\033[44m",
    'CC': "\033[42m",
    'DD': "\033[48;2;255;165;0m",
    'EE': "\033[43m",
    'FF': "\033[45m",
    "RESET": "\033[0m",
    "CLEARLINE": "\033[0K",
    "source": "\033[31m",
    "destination":"\033[32m",
        }

os.system("") # Enables ANSI escape codes in terminal

# Clears the terminal.
if os.name == "nt": # for Windows
    os.system("cls")
else: # for Mac/Linux
    os.system("clear")

def read_file(filename:str)->list[Stack]:
    '''
    read files
    input -- string
    output -- list[stack]
    '''
    with open(filename,'r') as file:
        flask_num, chmc_num = file.readline().strip().split(" ")
        flask_num = int(flask_num)
        chmc_num = int(chmc_num)
        flasks = []
        for _ in range(flask_num):
            flasks.append(Stack(FLASKS_SIZE))
        chemicals = BoundedQueue(CHEM_QUEUE_SIZE)
        for line in file:
            line=line.strip()
            if line[0].isdigit():
                dequeue_num = int(line[0]) # The number of dequeues
                bottle = int(line[2]) # bottle number
                if not chemicals.isEmpty() and not flasks[bottle-1].isFull():
                    for i in range(dequeue_num):
                        flasks[bottle-1].push(chemicals.dequeue())
            else:
                if not chemicals.isFull():
                    chemicals.enqueue(line)
    return flasks

def display_flasks(flasks:list[Stack],source = None, destination = None):
    '''
    print flasks in the specific format
    input -- list[Stack] 
    '''
    matrix = []
    num = len(flasks)
    for _ in range(FLASK_CAPACITY):
        row = ["|  |"] * num
        matrix.append(row)
    matrix.append(['+--+'] * num)
            
    for stack in range(num):
        if flasks[stack].is_sealed(CHEMICAL_UNITS):
            matrix[0][stack]='+--+'

    if source==None and destination==None: 
        order = []
        for i in range(num):
            order.append("  "+str(i+1)+' ')
        matrix.append(order)
    else: # source and destination have values
        order = []
        for i in range(num):
            if i == source:
                order.append(f'  {ANSI["source"]}{str(i+1)}{ANSI["RESET"]} ')
            elif i == destination:
                order.append(f'  {ANSI["destination"]}{str(i+1)}{ANSI["RESET"]} ')
            else:
                order.append("  "+str(i+1)+' ')
        matrix.append(order)

    for stack in range(num):
        for i in range(FLASK_CAPACITY):
            if flasks[stack].get(FLASK_CAPACITY-i-1) != None:
                matrix[i][stack]=f'|{ANSI[flasks[stack].get(FLASK_CAPACITY-i-1)]+flasks[stack].get(FLASK_CAPACITY-i-1)+ANSI["RESET"]}|'
    
    if len(flasks)==4: # display 4 flasks
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                print(matrix[i][j],end='  ')
            print()

    if len(flasks) == 8: # display 8 flasks
        for i in range(len(matrix)):
            for j in range(4):
                print(matrix[i][j],end='  ')
            print()
        for i in range(len(matrix)):
            for j in range(4,8):
                print(matrix[i][j],end='  ')
            print()

def move_cursor(x, y):
    '''
    Moves the cursor to the specified location on the terminal.
    Input:
        - x (int): row number
        - y (int): column number
    Returns: N/A     
    '''
    print("\033[{0};{1}H".format(x, y), end='')

def invalid(flasks:list[Stack],source,destination):
    '''
    check the invalid condition (the flasks are sealed or full)
    '''
    for stack in range(len(flasks)):
        if flasks[stack].is_sealed(CHEMICAL_UNITS) or flasks[stack].isFull():
            return False
        if source == 'exit' or destination =='exit':
            return False
        return True
    
def remove(flasks, source:int, destination:int):
    '''
    Remove chemicals from the source flask and add them to the destination flask.
    '''
    # convert into index
    if flasks[source].isEmpty() or flasks[source].is_sealed(CHEMICAL_UNITS):
        return False
    if flasks[destination].isFull() or flasks[destination].is_sealed(CHEMICAL_UNITS):
        return False
    chemical = flasks[source].pop()
    flasks[destination].push(chemical)
    return True

def invalidOutput(flasks,source:int,destination:int):
    '''
    Contains three abnormal situations
    a. source flask is empty/sealed
    b. destination flask is full/sealed
    c. source and the destination are the same
    '''
    if not remove(flasks,source,destination):
        if flasks[source].isEmpty() or flasks[source].is_sealed(CHEMICAL_UNITS):
            return 'Cannot pour from that flask. Try again.'
        if flasks[destination].isFull() or flasks[destination].is_sealed(CHEMICAL_UNITS):
            return 'Cannot pour into that flask. Try again.'
    elif source == destination:
        return 'Cannot pour into the same flask. Try again.'


def win(flasks)->bool:
    """
    check whether the user win ( empty or sealed)
    """
    for i in range(len(flasks)):
        if not flasks[i].isEmpty() and not flasks[i].is_sealed(CHEMICAL_UNITS):
            return False
    return True
            
def main():
    print("Magical Flask Game\n")
    flasks = read_file('8f6c.txt')
    move_cursor(6,0)
    display_flasks(flasks)
    
    loop = True
    source,destination = None,None

    while loop:
        print ("\033[{1};{0}H{2}".format(0, 3, 'Select source flask:'))
        move_cursor(3,22)
        print(ANSI["CLEARLINE"],end='')
        move_cursor(4,27)
        print ("\033[{1};{0}H{2}".format(0, 4, "Select destination flask: "))
        move_cursor(4,27)
        print(ANSI["CLEARLINE"],end='')
        move_cursor(6,0)
        display_flasks(flasks,source,destination)
        move_cursor(3,22)
        try:
            source = input()
            if source.lower() == 'exit':
                source = source.lower()
                raise Exception # exit the program
            source = int(source)
            move_cursor(4,27)
            destination = input()
            if destination.lower() == 'exit':
                destination = destination.lower()
                raise Exception
            destination = int(destination)
            # convert from order into index
            source -= 1
            destination -= 1

            # remove or cannot remove
            if remove(flasks, source, destination):
                print(ANSI["CLEARLINE"])
                if source == destination:
                    move_cursor(5,0)
                    print('Cannot pour into the same flask. Try again.')
                move_cursor(6,0)
                if win(flasks):
                    display_flasks(flasks,source,destination)
                    if len(flasks) == 4:
                        move_cursor(12,0)
                    elif len(flasks) == 8:
                        move_cursor(18,0)
                    print('You win!')
                    loop = False
            else:
                print(ANSI["CLEARLINE"])
                move_cursor(5,0)
                print(invalidOutput(flasks,source,destination))
                print(ANSI["CLEARLINE"])
                source = None
                destination = None
        except:
            if source != 'exit' and destination != 'exit':
                move_cursor(5,0)
                print(ANSI['CLEARLINE'],end='')
                print("Invalid input. Try again.",end='')
            else:
                move_cursor(6,0)
                display_flasks(flasks,source,destination)
                loop = False

if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    move_cursor(1,0)
    print(end-start,'s')
