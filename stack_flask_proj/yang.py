from bqueue import BoundedQueue
from bstack import Stack
import os

ANSI = {
    "RED": "\033[31m",
    "GREEN": "\033[32m",
    "BLUE": "\033[34m",
    "AA": "\033[41m",
    "BB": "\033[44m",
    "CC": "\033[42m",
    "DD": "\033[48;2;255;165;0m",
    "EE": "\033[43m",
    "FF": "\033[45m",
    "UNDERLINE": "\033[4m",
    "RESET": "\033[0m",
    "CLEARLINE": "\033[0K",
}

CHE_UNIT = 3
BOUNDEDQUEUE_SIZE = 4  # the chemical queue's capacity
STACK_SIZE = 4  # how many a flask can contain


class Flasks:
    def __init__(self, size) -> None:
        self.items = []
        for _ in range(size):
            self.items.append(Stack(STACK_SIZE))

    def get(self, index):
        return self.items[index]

    def getSize(self):
        return len(self.items)

    '''
    def __str__(self) -> str:
        matrix = []
        for _ in range(STACK_SIZE):
            matrix.append(["|  |"] * self.getSize())
        for h in range(STACK_SIZE):
            for s in range(self.getSize()):
                if self.items[s].size() - 1 >= h:
                    matrix[STACK_SIZE - 1 - h][s] = f"|{self.items[s].get(h)}|"
        for i in range(self.getSize()):
            if self.items[i].isSealed():
                matrix[0][i] = "+--+"
        output = ""
        if self.getSize() <= 4:
            for row in range(len(matrix)):
                output += "  ".join(matrix[row]) + "\n"
            output += "  ".join(["+--+"] * len(matrix[0])) + "\n"
            output += (
                "  " + "     ".join(str(i) for i in range(1, len(matrix[0]) + 1)) + "\n"
            )
        else:
            for row in range(len(matrix)):
                output += "  ".join(matrix[row][:4]) + "\n"
            output += "  ".join(["+--+"] * 4) + "\n"
            output += "     ".join(str(i) for i in range(1, 5)) + "\n\n"
            for row in range(len(matrix)):
                output += "  ".join(matrix[row][4:]) + "\n"
            output += "  ".join(["+--+"] * (len(matrix[0]) - 4)) + "\n"
            output += "     ".join(str(i) for i in range(5, len(matrix[0]) + 1)) + "\n"
        return output
        '''
    

    def get_show_matrix(self,source=None,destination=None):
        """
        create a matrix representing the flasks
        """
        matrix = []
        for _ in range(STACK_SIZE+2):
            matrix.append(["|  |"] * self.getSize())
        for h in range(STACK_SIZE):
            for s in range(self.getSize()):
                if self.items[s].size() - 1 >= h:
                    matrix[STACK_SIZE - 1 - h][s] = f"|{ANSI[self.items[s].get(h)]+self.items[s].get(h)+ANSI['RESET']}|"
        for i in range(self.getSize()):
            if self.items[i].isSealed():
                matrix[0][i] = "+--+"
        for i in range(self.getSize()):
            matrix[4][i] = '+--+'
        if source == None and destination == None:
            for i in range(self.getSize()):
                matrix[5][i] = "  "+str(i+1)+" "
        else:
            for i in range(self.getSize()):
                if i == destination:
                    matrix[5][i] = "  "+ANSI['GREEN']+str(i+1)+ANSI['RESET']+" "
                elif i == source:
                    matrix[5][i] = "  "+ANSI['RED']+str(i+1)+ANSI['RESET']+" "
                else:
                    matrix[5][i] = "  "+str(i+1)+" "
        return matrix
    
    
    def show_color(self,source_num = None, destination_num=None)-> None:
        """
        This function will help print the corrcet fomatted flasks
        input:
            source_num: index of the source flask + 1
            destination_num: index of the destination flask + 1
        """
        matrix = self.get_show_matrix(source_num,destination_num)
        if self.getSize() <= 4:
            for row in range(len(matrix)):
                for col in range(len(matrix[row])):
                    print(matrix[row][col], end= "  ")
                print()
        else:
            for row in range(len(matrix)):
                for col in range(4):
                    print(matrix[row][col], end= "  ")
                print("")
            print()
            for row in range(len(matrix)):
                for col in range(4,self.getSize()):
                    print(matrix[row][col],end="  ")
                print()
        print("\n")




def read_file(filename: str) -> Flasks:
    """
    This function will read text file for number of  flasks and chemicals
    Create a list of stacks to represent each flask
    Add chemicals into these flasks
    """
    with open(filename, "r") as file:
        flask_num, chmc_num = file.readline().strip().split(" ")
        flask_num = int(flask_num)
        chmc_num = int(chmc_num)
        flasks = Flasks(flask_num)
        chemicals = BoundedQueue(BOUNDEDQUEUE_SIZE)
        for line in file:
            if line[0].isnumeric():  # from one flask to another flask
                num1 = int(line.split("F")[0])
                num2 = int(line.split("F")[1])
                cnt = 0
                while (
                    not chemicals.isEmpty()
                    and cnt < num1
                    and not flasks.get(num2 - 1).isFull()
                ):
                    flasks.get(num2 - 1).push(chemicals.dequeue())
                    cnt += 1
            else:
                if not chemicals.isFull():  # add to queue while the queue is not full
                    chemicals.enqueue(line.strip())
    return flasks


def judge_win(flasks: Flasks) -> bool:
    for i in range(flasks.getSize()):
        if not flasks.get(i).isSealed() and not flasks.get(i).isEmpty():
            return False
    return True


def move_cursor(x, y):
    """
    Moves the cursor to the specified location on the terminal.
    Input:
        - x (int): row number
        - y (int): column number
    Returns: N/A
    """
    print("\033[{0};{1}H".format(x, y), end="")


def valid_type_range(source: str, length) -> bool:
    """
    This is a helper function used in main(), this will confirm
    source/destination is integer and in proper size or exit
    input:
        source: flask's index
        max_index: len of flask
    return: True when the input is valid
    """
    if source == "exit":
        return True
    if not source.isnumeric():
        return False
    if int(source) > length or int(source)<1:
        return False
    return True

def pour_from_empty(source:int,flasks:Flasks)->bool:
    """
    return wether source flask is empty
    """
    return flasks.get(source-1).isEmpty()

def valid_pour(index: int, flasks: Flasks) -> bool:
    """
    This is a helper function used in main(), this will judge whether source flask is sealed
    /destination flask is sealed
    input:
        index: flask index
        flasks: all flasks
    return:
        True if the source/destination flask is not sealed
    """
    return not flasks.get(index-1).isSealed()

def clear_rear(x,y):
    """
    move cursor to (x,y) and clear this line
    """
    move_cursor(x,y)
    print(ANSI['CLEARLINE'])


def main():
    if os.name == "nt":  # for Windows
        os.system("cls")
    else:  # for Mac/Linux
        os.system("clear")

    flasks = read_file("file2.txt")
    print("Magical Flask Game")
    move_cursor(3, 0)
    print("Select source flask:")
    print("Select destination flask:")
    move_cursor(6, 0)
    flasks.show_color()
    loop = True
    while loop:
        sourse_loop = True
        final_source = None
        final_destination = None
        while sourse_loop:
            move_cursor(3, 22)
            source = input()
            clear_rear(5,0)
            pass1 = valid_type_range(source, flasks.getSize())
            # write exit()
            if pass1:
                if source == 'exit':
                    move_cursor(6,0)
                    flasks.show_color()
                    exit()
                source = int(source)
                pass2 = not pour_from_empty(source,flasks) and valid_pour(source,flasks)
                if not pass2:
                    move_cursor(5,0)
                    print("Cannot pour from that flask. Try again.")
                sourse_loop = not (pass1 and pass2)
            else:
                move_cursor(5,0)
                print("Invalid input. Try again.")
            if sourse_loop:
                clear_rear(3,22)
        destination_loop = True
        while destination_loop:
            move_cursor(4,27)
            destination = input()
            clear_rear(5,0)
            pass3 = valid_type_range(destination,flasks.getSize())
            if pass3:
                if destination == 'exit':
                    move_cursor(6,0)
                    flasks.show_color()
                    exit()
                destination = int(destination)
                pass4 = valid_pour(destination,flasks)
                if not pass4:
                    move_cursor(5,0)
                    print("Cannot pour from that flask. Try again.")
                destination_loop = not(pass3 and pass4)
            else:
                move_cursor(5,0)
                print("Invalid input. Try again.")
            if destination_loop:
                clear_rear(4,27)
        if source == destination:
            move_cursor(5,0)
            print("Cannot pour into the same flask. Try again")
        else:
            # move from one to another
            flasks.get(destination-1).push(flasks.get(source-1).pop())
            final_source = source-1
            final_destination = destination-1
            flasks.get(destination-1).trySeal(STACK_SIZE-1)
            flasks.get(source-1).trySeal(STACK_SIZE-1)
            loop = not judge_win(flasks)
            if not loop:
                move_cursor(13,0) if flasks.getSize()<=4 else move_cursor(20,0)
                print('You win!')
        clear_rear(3,22)
        clear_rear(4,27)
        move_cursor(6,0)
        flasks.show_color(final_source,final_destination)
            
            


if __name__ == "__main__":
    main()
