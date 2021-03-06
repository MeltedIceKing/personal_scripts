import pyautogui as p
import pydirectinput as pdi # Use this library as pyautogui may not support older games
from tqdm import tqdm
import time
import random
import sys


class InviteFriend:
    """
    Represents a class that reads a file.txt and automatically invites names contained within

    :param file_of_names: File that holds all of the names
    :type file_of_names: str

    :param invite_count: How many names to invite from said file
    :type invite_count: int

    :param start_delay: How long the delay is before this script runs
    :type start_delay: int or float
    """
    def __init__(self, file_of_names, invite_count, start_delay=5):
        """
        Initialization of instance attributes
        """
        self._file_of_names = file_of_names
        self._invite_count = invite_count
        self._start_delay = start_delay

        self.verify_integrity()

        self._list_of_names = self.create_list_of_names()

    def verify_integrity(self):
        """
        Behaviour: Verifies the variable types set by the constructor
        """
        if isinstance(self._file_of_names, str) == False:
            print("ERROR: Incorrect file name, it must be a .txt file. Script exiting in 5 seconds.")
            time.sleep(5)
            sys.exit()
        if isinstance(self._invite_count, int) == False:
            print("ERROR: Invite count must be a whole number. Script exiting in 5 seconds.")
            time.sleep(5)
            sys.exit()
        if isinstance(self._start_delay, int) == False and isinstance(self._start_delay, float) == False:
            print("ERROR: Start delay must be a number. Script exiting in 5 seconds.")
            time.sleep(5)
            sys.exit()

    # Getter
    @property
    def file_of_names(self):
        return self._file_of_names

    # Setter
    @file_of_names.setter
    def file_of_names(self, value):
        self._file_of_names = value

    def create_list_of_names(self):
        """
        Behaviour: Creates a list of strings of the names in user-provided file.txt
        """
        try:
            with open(self._file_of_names) as f:
                names_list = f.readlines()
                names_list = [name.strip() for name in names_list]
            return names_list
        except FileNotFoundError:   # Most common and likely exception to occur
            print(f"ERROR: File {self._file_of_names} does not exist in this script's directory. Exiting script in 5 seconds.")
            time.sleep(5)
            sys.exit()

    def invite_person(self, name):
        """
        Behaviour: Automatically invites players using the pyautogui and pydirectinput libraries

        :param name: Name of the user to be invited
        :type name: str
        """
        pdi.press("enter")
        #natural_typing_delay = random.uniform(0.00001, 0.00005)
        p.write(f"/squadinvite {name}")
        pdi.press("enter")

    def focus_game_window(self, x=1000, y=500):
        """
        Behaviour: Focuses the game window for the user. (1000, 500) is the default location to click

        :param x: x-coordinate of click location
        :type x: int

        :param y: y-coordinate of click location
        :type y: int
        """
        print(f"Get ready, the script will begin inviting in {self._start_delay} seconds.\n\n")
        time.sleep(self._start_delay)
        try:
            p.click(x,y)
        except:
            print("ERROR: Invalid coordinates, cannot focus window. Exiting script in 5 seconds.")
            time.sleep(5)
            sys.exit()

    def invite_friends(self):
        """
        Behaviour: Automatically invites users using the methods created above
        """
        for i in tqdm(range(self._invite_count)):

            # Select a random individual to invite
            random_name = random.randint(0, len(self._list_of_names) - 1)
            self.invite_person(self._list_of_names[random_name])
            print(f"\n\n{self._list_of_names[random_name]} has been invited.")

        print("\n\nThe script has finished inviting.\n\n")