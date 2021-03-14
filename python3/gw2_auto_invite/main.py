import pyautogui as p
import pydirectinput as pdi # Use this library as pyautogui may not support older games
import time
import random
import os


class InviteFriend:
    def __init__(self, file_of_names, invite_count, start_delay):
        self._file_of_names = file_of_names
        self._list_of_names = self.create_list_of_names()
        self._invite_count = invite_count
        self._start_delay = start_delay

    # Getter
    @property
    def file_of_names(self):
        return self._file_of_names

    # Setter
    @file_of_names.setter
    def file_of_names(self, value):
        self._file_of_names = value

    def create_list_of_names(self):
        with open(self._file_of_names) as f:
            names_list = f.readlines()
            names_list = [name.strip() for name in names_list]
        return names_list

    def invite_person(self, name):
        pdi.press("enter")
        natural_typing_delay = random.uniform(0.00001, 0.00005)
        p.write(f"/squadinvite {name}", interval=natural_typing_delay)
        pdi.press("enter")

    def focus_game_window(self, x=1000, y=500):
        p.click(x,y)

    def invite_friends(self):
        print(f"Get ready, the script will begin inviting in {self._start_delay} seconds.")
        time.sleep(self._start_delay)
        self.focus_game_window()
        for i in range(self._invite_count):
            random_name = random.randint(0, len(self._list_of_names) - 1)
            self.invite_person(self._list_of_names[random_name])
        print("The script has finished inviting.")


if __name__ == "__main__":
    # Change to directory where this Python script is located
    abs_path = os.path.abspath(__file__)
    dir_name = os.path.dirname(abs_path)
    os.chdir(dir_name)

    invite_people = InviteFriend("names.txt", 5, 3)
    invite_people.invite_friends()