#----------------------------------------------------
# Lab 4: Web browser simulator
# Purpose of program:
#
# Author: rosie wang
# Collaborators/references:
#----------------------------------------------------

def getAction():
    '''
    Write docstring to describe function
    Inputs: none
    Returns: str
    '''
    while True:
        action = input("Enter = to enter a URL, < to go back, > to go forward, q to quit:")
        if action in ['=', '<', '>', 'q']:
            return action
        else:
            print("Invalid input.")

def goToNewSite(current, pages):
    '''
    This function prompts the user to enter a new website address, and returns
    the index to the current site (int).It also updates the list (pages) and current index
    (current)
    Inputs: int,list
    Returns: int
    '''       

    new_website = input("Enter the URL: ")
    while current < len(pages) - 1:
        pages.pop()  # delete n websites after current web page

    # Append the new website to the list
    pages.append(new_website)
    current = len(pages) - 1
    return current

def goBack(current, pages):
    '''
    no websites stored -- > error and return current index
    otherwise --> return the previous webpage index    
    Inputs: int,list
    Returns: int
    '''   
    if current > 0:
        current = current - 1
    else:
        print("Cannot go back.")

    return current

def goForward(current, pages):
    '''
    Write docstring to describe function
    Inputs: ?
    Returns: ?
    '''    
    if current < len(pages) - 1:
        # Increment the index to go forward
        current = current + 1
    else:
        print("Cannot go forward.")
    return current


def main():
    '''
    Controls main flow of web browser simulator
    Inputs: N/A
    Returns: None
    '''    
    HOME = 'www.cs.ualberta.ca'
    websites = [HOME]
    currentIndex = 0
    quit = False
    
    while not quit:
        print('\nCurrently viewing', websites[currentIndex])
        action = getAction()
        
        if action == '=':
            currentIndex = goToNewSite(currentIndex, websites)
        elif action == '<':
            currentIndex = goBack(currentIndex, websites)
        elif action == '>':
            currentIndex = goForward(currentIndex, websites)
        elif action == 'q':
            quit = True
    
    print('Browser closing...goodbye.')    

        
if __name__ == "__main__":
    main()
    