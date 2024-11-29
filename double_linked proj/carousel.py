import json
from circular_dlinked_list import CircularDoublyLinkedList
import art
import time
import os
max_size = 5 # capacity

class Carousel:
    '''
    include circular_d_linked_list, and current node to point to the current slide
    '''
    def __init__(self):
        self.current = None
        self.cdll = CircularDoublyLinkedList(max_size)

    def add_left(self,item):
        '''
        add an item on the left
        '''
        self.cdll.add(item,self.current)
        
    def add_right(self,item):
        '''
        add an item on the right
        '''
        self.cdll.add(item,self.current+1)
        self.current += 1

    def add(self,item):
        '''
        add the first emoji frame
        '''
        self.current = 0
        self.cdll.add(item,self.current)
        
    def get_info(self):
        '''
        get the current data
        '''
        return self.cdll.getdata(self.current)
    
    def get_left_info(self):
        '''
        get the left one data
        '''
        if self.cdll.size() == 0:
            return None
        elif self.cdll.size() == 1:
            return self.get_info()  # The only item is the current item itself
        left_node_index = self.current - 1 if self.current > 0 else self.cdll.size() - 1
        return self.cdll.getdata(left_node_index)

    def get_right_info(self):
        '''
        get the right one data
        '''
        if self.cdll.size() == 0:
            return None  
        elif self.cdll.size() == 1:
            return self.get_info()  # The only item is the current item itself
        right_node_index = (self.current + 1) % self.cdll.size()
        return self.cdll.getdata(right_node_index)
  
    def delete(self):
        '''
        delete the current one
        '''
        self.cdll.pop(self.current)
        if self.get_size() == 0:
            self.current = None
            return
        if self.current > 0:
            self.current -= 1

    def get_size(self):
        '''
        get the size of the carousel
        '''
        return self.cdll.size()

def readfiles(filename):
    '''
    read json file and return the data
    '''
    with open(filename, 'r',encoding='utf-8') as file:
        emojis = json.load(file)
    return emojis

def print_header(carousel: Carousel):
    '''
    print the header in 3 different modes
    '''
    if carousel.get_size() == 0 :
        print('Type any of the following commands to perform the action: ')
        print('        ADD: Add a emoji frame')
        print('        Q: Quit the program')
    elif carousel.get_size() ==1 : 
        print('Type any of the following commands to perform the action: ')
        print('        ADD: Add a emoji frame')
        print('        DEL: Delete a current frame')
        print('        INFO: Retrieve info about current frame')
        print('        Q: Quit the program')
    elif carousel.get_size() >=2 :
        print('Type any of the following commands to perform the action: ')
        print('        L: Move left')
        print('        R: Move right')
        print('        ADD: Add a emoji frame')
        print('        DEL: Delete a current frame')
        print('        INFO: Retrieve info about current frame')
        print('        Q: Quit the program')

def clear_screen():
    '''
    clear screen
    '''
    os.system("cls" if os.name == "nt" else "clear")

def get_emoji(name):
    '''
    get the emoji in the json file
    '''
    for i in range(len(EMOJIS)):
        if name in EMOJIS[i]['emojis']:
            return EMOJIS[i]['emojis'][name]

def fill_art(mode,emoji,left=None,mid=None,right=None):
    '''
    Fill in the box with the corresponding emoji
    '''
    if mode == 'show1':
        output = art.show1
        output = output.replace('()',emoji)
    elif mode == 'show3':
        output = art.show3
        output = output.format(left,mid, right)
    elif mode == 'delete2':
        output = art.delete2
        output = output.format(left,right)
    elif mode == 'delete':
        output = art.delete
    elif mode == 'move_right':
        output = art.move_right
        output = output.format(left,right)
    elif mode== 'add_right2':
        output = art.add_right2
        output = output.format(left,right)
    elif mode== 'add_right':
        output = art.add_right
    elif mode == 'move_left':
        output = art.move_left
        output = output.format(left,right)
    elif mode =='add_left2':
        output = art.add_left2
        output = output.format(left,right)
    elif mode =='add_left':
        output = art.add_left
    else: # mode == add
        output = art.add
    return output
    
def getUserInput(size):
    '''
    get user input until it's valid, including 3 modes
    '''
    loop = True
    while loop:
        user_input = input(">>").lower()
        if size == 0:
            if user_input in ['add','q']:
                return user_input
        elif size == 1:
            if user_input in ['add','q','del','info']:
                return user_input
        elif size >1 :
            if user_input in ['add','q','del','info','l','r']:
                return user_input

def valid_emoji(user_input):
    '''
    check if the emoji is in json file
    '''
    for i in range(len(EMOJIS)):
        valid_emojis = EMOJIS[i]['emojis']
        if user_input in valid_emojis: 
            return True
    return False

def click_button():
    '''
    Click any button to continue
    '''
    time.sleep(1)
    print("\nClick any button to continue")
    input() # Click any button to continue

def main():
    '''
    show the corrected frame with the corresponding situation
    '''
    carousel=Carousel()
    loop = True
    while loop:
        if carousel.get_size() ==1:
            print(fill_art('show1',get_emoji(carousel.get_info())))
        elif carousel.get_size() >1:
            print(fill_art('show3',get_emoji(carousel.get_info()),left = get_emoji(carousel.get_left_info()), mid = get_emoji(carousel.get_info()),right= get_emoji(carousel.get_right_info()) ))
        print_header(carousel)
        user_input = getUserInput(carousel.get_size())
        if user_input =='add': # add
            emoji = input('What do you want to add?\n>>')
            if valid_emoji(emoji) and carousel.get_size() > 0: # add on the left or the right side
                location = input('On which side do you want to add the emoji frame? (left/right):')
                if location.lower() =='left':
                    clear_screen()
                    if carousel.get_size() == 1:
                        print(fill_art('add_left',None))
                    else:
                        print(fill_art('add_left2',None,left=get_emoji(carousel.get_left_info()),right = get_emoji(carousel.get_right_info())))
                    carousel.add_left(emoji)
                elif location.lower() =='right':
                    clear_screen()
                    if carousel.get_size() ==1:
                        print(fill_art('add_right',None))
                    else:
                        print(fill_art('add_right2',None,left=get_emoji(carousel.get_left_info()),right = get_emoji(carousel.get_right_info())))
                    carousel.add_right(emoji)
            elif valid_emoji(emoji): # valid emoji and add on the first slide
                carousel.add(emoji)
                clear_screen()
                print(fill_art('add',None)) 
            time.sleep(1)
        elif user_input =='l': # move left
            clear_screen()
            print(fill_art('move_left',None,left=get_emoji(carousel.get_left_info()),right = get_emoji(carousel.get_right_info())))
            if carousel.current == 0:
                carousel.current = carousel.get_size()
            carousel.current -= 1
            time.sleep(1)
        elif user_input == 'r': # move right
            clear_screen()
            print(fill_art('move_right',None,left=get_emoji(carousel.get_left_info()),right = get_emoji(carousel.get_right_info())))
            if carousel.current == carousel.get_size()-1:
                carousel.current = -1
            carousel.current += 1
            time.sleep(1)
        elif user_input =='del': # delete
            clear_screen()
            carousel.delete()
            if carousel.get_size() == 0:
                print(fill_art('delete',None))
            else:
                print(fill_art('delete2',None,left=get_emoji(carousel.get_left_info()),right = get_emoji(carousel.get_right_info())))
            time.sleep(1)
        elif user_input =='info': # info
            name = carousel.get_info()
            for i in range(len(EMOJIS)):
                if name in EMOJIS[i]["emojis"]:
                    sym = EMOJIS[i]["emojis"][name]
                    emoji_class = EMOJIS[i]["class"]
            print("Object:", name)
            print("Sym:", sym)
            print("Class:", emoji_class)
            click_button()    
        elif user_input == 'q': # quit
            exit()
        clear_screen() # the header prints on the same row
        
if __name__ == '__main__':
    EMOJIS = readfiles('emojis.json')
    main()