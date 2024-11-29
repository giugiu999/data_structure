import os

ANSI = {
    "RED": "\033[31m",
    "GREEN": "\033[32m",
    "BLUE": "\033[34m",
    "HRED": "\033[41m",
    "HGREEN": "\033[42m",
    "HBLUE": "\033[44m",
    "UNDERLINE": "\033[4m",
    "RESET": "\033[0m",
    "CLEARLINE": "\033[0K"
}

os.system("") # Enables ANSI escape codes in terminal

# Clears the terminal.
if os.name == "nt": # for Windows
    os.system("cls")
else: # for Mac/Linux
    os.system("clear")

def move_cursor(x, y):
    '''
    Moves the cursor to the specified location on the terminal.
    Input:
        - x (int): row number
        - y (int): column number
    Returns: N/A     
    '''
    print("\033[{0};{1}H".format(x, y), end='')

print(ANSI["UNDERLINE"] + ANSI["BLUE"] + "VT100 SIMULATOR" + ANSI["RESET"])

jump_out = False
while not jump_out:
    print ("\033[{1};{0}H{2}".format(0, 3, 'Enter a text colour:'))
    move_cursor(3,21)
    print(ANSI["CLEARLINE"],end='')
    move_cursor(4,27)
    print(ANSI["CLEARLINE"],end='')
    move_cursor(4,27)
    print ("\033[{1};{0}H{2}".format(0, 4, 'Enter a background colour:'))
    move_cursor(3,21)
    text_color = input()

    while text_color.upper() not in ['RED', 'GREEN', 'BLUE', 'EXIT']:
        move_cursor(3,21)
        print(ANSI['CLEARLINE'])
        move_cursor(3,21)
        text_color = input()
    if text_color.upper() == 'EXIT':
        # print(ANSI["CLEARLINE"])
        jump_out = True
        move_cursor(6,0)
    
    if not jump_out:
        move_cursor(4,27)
        bgcolor = input()

        while bgcolor.upper() not in ['RED', 'GREEN', 'BLUE', 'NONE', 'EXIT']:
            move_cursor(4,27)
            print(ANSI['CLEARLINE'])
            move_cursor(4,27)
            bgcolor = input()
        if bgcolor.upper() == 'EXIT':
            print(ANSI["CLEARLINE"])
            jump_out = True
            move_cursor(6,0)
            print()
        elif bgcolor.upper() == 'NONE':
            print(ANSI["UNDERLINE"] + ANSI[text_color.upper()] + "VT100 SIMULATOR" + ANSI["RESET"])
        else:
            print(ANSI["UNDERLINE"] + ANSI[text_color.upper()] + ANSI['H'+bgcolor.upper()] + "VT100 SIMULATOR" + ANSI["RESET"])

