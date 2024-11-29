import os
import json
from aaa import CircularDoublyLinkedList
import time
import art


class Carousel:
    def __init__(self, capacity) -> None:
        self.cdll = CircularDoublyLinkedList(capacity)
        self.curr = None

    def __str__(self):
        return str(self.curr) + ": " + str(self.cdll)

    def add(self, data, left=False, right=False) -> None:
        """
        Responsible for adding a new node to the circular doubly-linked list.
        input:
            data: name of the emoji
            left: True if insert to the left of the curr
            right: True if insert to the right of the curr
            (left and right should not be both True)
        """
        if not left and not right:
            self.cdll.insert(0, data)
            self.curr = 0
        elif left:
            self.cdll.insert(self.curr, data)
        elif right:
            self.cdll.insert(self.curr + 1, data)
            self.curr += 1

    def size(self):
        return self.cdll.size()

    def goLeft(self):
        if self.curr == 0:
            self.curr = self.cdll.size() - 1
        else:
            self.curr -= 1

    def goRight(self):
        if self.curr == self.cdll.size() - 1:
            self.curr = 0
        else:
            self.curr += 1

    def delete(self):
        if self.cdll.size() == 0:
            raise Exception("delete(): size ")
        if self.cdll.size() == 1:
            self.curr = 0
            self.cdll.pop(0)
        else:
            self.cdll.pop(self.curr)
            if self.curr == 0:
                self.curr = self.cdll.size() - 1
            else:
                self.curr -= 1

    def getInfo(self):
        return self.cdll.get(self.curr).getData()

    def get_neighbor_info(self, ne):
        """
        ne: True for getting next, False for getting previous
        """
        if ne:
            self.goRight()
            data = self.getInfo()
            self.goLeft()
        else:
            self.goLeft()
            data = self.getInfo()
            self.goRight()
        return data


def get_header(carousel: Carousel, add=False) -> str:
    """
    input: carousel
    return: a str containing corresponding message according to the next avalible operations
    """
    output = [MESSAGE["HEAD"], MESSAGE["ADD"], MESSAGE["Q"]]
    if carousel.size() > 0:
        output.insert(2, MESSAGE["DEL"])
        output.insert(3, MESSAGE["INFO"])
    if carousel.cdll.size() > 1:
        output.insert(1, MESSAGE["L"])
        output.insert(2, MESSAGE["R"])
    return "\n".join(output).strip()


def get_valid_orders(carousel: Carousel) -> list[str]:
    """
    Get a list containing valid orders according to the stage of the program
    """
    valid_orders = ["ADD", "Q"]
    if carousel.size() > 0:
        valid_orders += ["DEL", "INFO"]
    if carousel.size() > 1:
        valid_orders += ["L", "R"]
    return valid_orders


def valid_emoji(emoji_name: str) -> bool:
    """
    return whether the emoji_name is a valid emoji name
    """
    for i in range(len(EMOJIS)):
        if emoji_name in EMOJIS[i]["emojis"]:
            return True
    return False


def info_operation(carousel: Carousel):
    """
    Show the info after getting the valid order
    """
    name = carousel.getInfo()
    for i in range(len(EMOJIS)):
        if name in EMOJIS[i]["emojis"]:
            sym = EMOJIS[i]["emojis"][name]
            class_ = EMOJIS[i]["class"]
    print("Object:", name)
    print("Sym:", sym)
    print("Class:", class_)
    time.sleep(1)
    print()
    print("Click any button to continue")
    press_any_key_to_continue()


def press_any_key_to_continue():
    """
    Press any key to continue, used in info_operation()
    """
    # Searched from chatGPT
    os.system("stty raw -echo")
    key = ord(os.read(0, 1))
    os.system("stty cooked echo")


# def lev(a:str,b:str)->int:
#     """
#     Get the Levenshtein Distance between two strings
#     """
#     if len(a) == 0:
#         return len(b)
#     if len(b) == 0:
#         return len(a)
#     if a[0]==b[0]:
#         return lev(a[1:],b[1:])
#     return 1+min(lev(a[1:],b),lev(a,b[1:]),lev(a[1:],b[1:]))


def lev(a: str, b: str) -> int:
    """
    Get the Levenshtein Distance between two strings
    This is a optimized method got from chatGPT, using dynamic programming.
    Using a matrix to store the data, preventing multiple calculation.
    """
    # Create a matrix to store intermediate results
    dp = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]

    # Initialize the first row and column
    for i in range(len(a) + 1):
        dp[i][0] = i
    for j in range(len(b) + 1):
        dp[0][j] = j

    # Fill the matrix
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            cost = 0 if a[i - 1] == b[j - 1] else 1
            dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1] + cost)

    # Return the bottom-right cell of the matrix
    return dp[len(a)][len(b)]


def guess_emoji(name: str) -> str:
    """
    Match the emoji closest to the user input
    return: The closest emoji name
    """
    min_distance = len(name)
    min_name = name
    for i in range(len(EMOJIS)):
        for key in EMOJIS[i]["emojis"].keys():
            lev_distance = lev(name, key)
            if min_distance > lev_distance:
                min_distance = lev_distance
                min_name = key
    return min_name


def add_operation(carousel: Carousel):
    """
    Do add operation after getting user inputted order
    """
    print("What do you want to add?")
    loop1 = True
    while loop1:
        emoji_name = input(">> ").lower()
        if valid_emoji(emoji_name):
            loop1 = False
        else:
            guess_name = guess_emoji(emoji_name)
            if guess_name != emoji_name:
                guess_input = input(f"Do you mean {guess_name}? (Y/N) ").upper()
                if guess_input == "Y":
                    loop1 = False
                    emoji_name = guess_name
                else:
                    print("Invalid emoji name. Please enter a valid emoji name.")
            else:
                print("Invalid emoji name. Please enter a valid emoji name.")
    if carousel.size() == 0:  # add the first node
        show_transition(carousel, "ADD")
        carousel.add(emoji_name)
    else:
        loop2 = True
        while loop2:
            direction = input(
                "On which side do you want to add the emoji frame? (left/right): "
            ).lower()
            if direction in ["left", "right"]:
                loop2 = False
            else:
                print("Invalid side. Please enter either 'left' or 'right'.")
        if direction == "left":
            carousel.add(emoji_name, left=True)
            if carousel.size() == 2:
                show_transition(carousel, "ADD_LEFT")
            else:
                show_transition(carousel, "MULTI_ADD_LEFT")
        else:
            carousel.add(emoji_name, right=True)
            if carousel.size() == 2:
                show_transition(carousel, "ADD_RIGHT")
            else:
                show_transition(carousel, "MULTI_ADD_RIGHT")


def del_operation(carousel: Carousel):
    """
    Do delete operation after getting the valid order
    """
    if carousel.size() > 0:
        if carousel.size() == 1:
            show_transition(carousel, "DEL")
        else:
            show_transition(carousel, "MULTI_DEL")
        carousel.delete()


def get_emoji(name: str):
    """
    Search and return the emoji from the emoji list
    """
    for i in range(len(EMOJIS)):
        if name in EMOJIS[i]["emojis"]:
            return EMOJIS[i]["emojis"][name]


def fill_frames(carousel: Carousel, string: str, num):
    """
    Fill the brackets in the art.py 's strs
    """
    if num == 1:  # single frame
        emoji = get_emoji(carousel.getInfo())
        string = string.replace("()", emoji)
        return string
    elif num == 3:
        emojis = [
            get_emoji(carousel.get_neighbor_info(False)),
            get_emoji(carousel.getInfo()),
            get_emoji(carousel.get_neighbor_info(True)),
        ]
        string = string.format(emojis[0], emojis[1], emojis[2])
    elif num == 2:
        emojis = [
            get_emoji(carousel.get_neighbor_info(False)),
            get_emoji(carousel.get_neighbor_info(True)),
        ]
        string = string.format(emojis[0], emojis[1])
    return string


def show_transition(carousel: Carousel, tran_name: str):
    """
    Show the transition at the end of the operation
    """
    clear_screen()
    if tran_name == "MULTI_DEL":
        print(fill_frames(carousel, art.MULTI_DEL, 2))
    elif tran_name == "DEL":
        print(art.DEL)
    elif tran_name == "MOVE_LEFT":
        print(fill_frames(carousel, art.MOVE_LEFT, 2))
    elif tran_name == "MOVE_RIGHT":
        print(fill_frames(carousel, art.MOVE_RIGHT, 2))
    elif tran_name == "MULTI_ADD_LEFT":
        print(fill_frames(carousel, art.MULTI_ADD_LEFT, 2))
    elif tran_name == "MULTI_ADD_RIGHT":
        print(fill_frames(carousel, art.MULTI_ADD_RIGHT, 2))
    elif tran_name == "ADD":
        print(art.ADD)
    elif tran_name == "ADD_RIGHT":
        print(art.ADD_RIGHT)
    elif tran_name == "ADD_LEFT":
        print(art.ADD_LEFT)
    time.sleep(1)


def show_frame(carousel: Carousel):
    """
    Show the frame at the beginning of each loop
    """
    if carousel.size() == 1:
        print(fill_frames(carousel, art.SINGLE_FRAME, 1))
    elif carousel.size() > 1:
        print(fill_frames(carousel, art.MULTI_FRAME, 3))


def user_interface():
    """
    The user interface implementation.
    User interacts by using this method.
    """
    carousel = Carousel(max_size)
    while True:
        ###########
        ### add show picture function here to show the corresponding pictures ###
        ###########
        show_frame(carousel)
        print(get_header(carousel))
        # get valid order
        valid_orders = get_valid_orders(carousel)
        suc_input = False
        while not suc_input:
            order = input(">> ").upper()
            suc_input = order in valid_orders
            if not suc_input:
                print(
                    "Invalid menu option. Please choose a valid option from the menu."
                )
            # judge add to a full carousel
            if order == "ADD" and carousel.size() == max_size:
                print("You cannot add emojis! Carousel is Full.")
                suc_input = False

        # do operation according to order
        if order == "ADD":
            add_operation(carousel)
        elif order == "INFO":
            info_operation(carousel)
        elif order == "DEL":
            del_operation(carousel)
        elif order == "L":
            show_transition(carousel, "MOVE_LEFT")
            carousel.goLeft()
        elif order == "R":
            show_transition(carousel, "MOVE_RIGHT")
            carousel.goRight()
        elif order == "Q":
            clear_screen()
            exit()

        clear_screen()  # clear screen


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def read_json(filename):
    """
    Read json file and store the data into a dict
    """
    with open(filename, "r",encoding='utf-8') as file:
        emojis = json.load(file)
    return emojis


def main():
    user_interface()


if __name__ == "__main__":
    """
    Set global variables and call the main() function
    """
    max_size = 5  # CDLL's capacity
    MESSAGE = {
        "HEAD": "Type any of the following commands to perform the action:",
        "L": " " * 8 + "L: Move left",
        "R": " " * 8 + "R: Move right",
        "ADD": " " * 8 + "ADD: Add a emoji frame",
        "DEL": " " * 8 + "DEL: Delete current emoji frame",
        "INFO": " " * 8 + "INFO: Retrieve info about current frame",
        "Q": " " * 8 + "Q: Quit the program",
    }
    EMOJIS = read_json("emojis.json")  # list[{},{}]
    main()
