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
    Prompts the user to enter a command for the web browser simulator.
    Valid commands are '=', '<', '>', or 'q'.
    Raises an exception for invalid entries.

    Inputs: None
    Returns: A string representing the user's input command.
    '''
    while True:
        action = input( "Enter '=' to visit a new site, '<' to go back, '>' to go forward, or 'q' to quit: " )
        if action not in [ '=', '<', '>', 'q' ]:
            raise Exception( 'Invalid entry.' )
        return action


def goToNewSite(current, bck, fwd):
    '''
    Prompts the user for a new website address, updates the back and forward stacks accordingly,
    and returns the new site.

    Inputs:
    - current: The current website (string).
    - bck: A stack holding the back history of visited sites.
    - fwd: A stack holding the forward history of visited sites.

    Returns: The new website address (string).
    '''
    newSite = input( "URL:" )
    if current:
        bck.push( current )
    fwd.clear()  # Clear the forward stack because new navigation clears forward history.
    return newSite


def goBack(current, bck, fwd):
    '''
    Moves back to the previous website, if available, updating the stacks accordingly.

    Inputs:
    - current: The current website (string).
    - bck: A stack holding the back history of visited sites.
    - fwd: A stack holding the forward history of visited sites.

    Returns: The previous website address (string), or the current site if back is not possible.
    '''
    if bck.isEmpty():
        print( "Cannot go back." )
        return current
    else:
        fwd.push( current )
        return bck.pop()


def goForward(current, bck, fwd):
    '''
    Moves forward to the next website, if available, updating the stacks accordingly.

    Inputs:
    - current: The current website (string).
    - bck: A stack holding the back history of visited sites.
    - fwd: A stack holding the forward history of visited sites.

    Returns: The next website address (string), or the current site if forward is not possible.
    '''
    if fwd.isEmpty():
        print( "Cannot go forward." )
        return current
    else:
        bck.push( current )
        return fwd.pop()


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

    print( 'Currently viewing', current )
    while not quit:

        try:
            action = getAction()
            
        except Exception as actionException:
            print(actionException.args[0])
            
        else:
            if action == '=':
                current = goToNewSite(current, back, forward)
            elif action == '<':
                current = goBack( current, back, forward )
            elif action == '>':
                current = goForward( current, back, forward )
            elif action == 'q':
                quit = True
            if not quit:
                print( '\nCurrently viewing', current )
            #TO DO: add code for the other valid actions ('<', '>', 'q')
            #HINT: LOOK AT LAB 4
            
            
    print('Browser closing...goodbye.')    

        
if __name__ == "__main__":
    main()
    