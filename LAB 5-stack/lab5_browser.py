#----------------------------------------------------
# Lab 5, Exercise 2: Web browser simulator
# Purpose of program:
#
# Author: 
# Collaborators/references:
#----------------------------------------------------

from stack import Stack

def getAction():
    '''
    Write docstring to describe function
    Inputs: ?
    Returns: ?
    '''
    action = input("Enter = to enter a URL, < to go back, > to go forward, q to quit:")
    if action in ['=', '<', '>', 'q']:
        return action
    else:
        raise Exception('Invalid entry.')


def goToNewSite(current, bck, fwd):
    '''
    Write docstring to describe function
    Inputs: ?
    Returns: ?
    '''   
    new_website = input("Enter the URL: ")
    
    # Update the stacks
    bck.push(current)
    fwd.clear()

    # Append the new website to the list
    current = new_website
    return current
    
def goBack(current, bck, fwd):
    '''
    Write docstring to describe function
    Inputs: ?
    Returns: ?
    '''    
    try:
        prev_website = bck.pop()
        fwd.push(current)
        current = prev_website

    except: 
        print("Cannot go back.")

    return current

def goForward(current, bck, fwd):
    '''
    Write docstring to describe function
    Inputs: ?
    Returns: ?
    '''    
    try:
        next_website = fwd.pop()
        bck.push(current)
        current = next_website
    except:
        print("Cannot go forward.")
    
    return current

def main():
    '''
    Controls main flow of web browser simulator
    Inputs: N/A
    Returns: None
    '''    
    HOME = 'www.cs.ualberta.ca'
    back = Stack()
    forward = Stack()
    
    current = HOME
    quit = False
    
    while not quit:
        print('\nCurrently viewing', current)
        try:
            action = getAction()
            
        except Exception as actionException:
            print(actionException.args[0])
            
        else:
            if action == '=':
                current = goToNewSite(current, back, forward)
            elif action == '<':
                current = goBack(current,back,forward)
            elif action == '>':
                current = goForward(current,back,forward)
            elif action == 'q':
                quit = True
            
            
    print('Browser closing...goodbye.')    

        
if __name__ == "__main__":
    main()    