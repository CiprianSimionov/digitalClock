"""Functionality for current hour and format the output data"""
import time

class Clock:
    #Constructor for "current hour" variable
    def __init__(self):
        self.current_hour = None

    #Method to get current hour
    def get_current_hour(self):
        self.current_hour = time.localtime()

    #Method to format data
    def format_hour(self):
        format_hour = (f"{self.current_hour.tm_hour:02d} : {self.current_hour.tm_min:02d} : "
                         f"{self.current_hour.tm_sec:02d}")
        return format_hour


    #Method to display data in requested format
    def display_hour(self, char_hour):
        dict_hour ={

            '0': [
                " _ ",
                "| |",
                "|_|"
            ],
            '1': [
                "   ",
                "  |",
                "  |"
            ],
            '2': [
                " _ ",
                " _|",
                "|_ "
            ],
            '3': [
                " _ ",
                " _|",
                " _|"
            ],
            '4': [
                "   ",
                "|_|",
                "  |"
            ],
            '5': [
                " _ ",
                "|_ ",
                " _|"
            ],
            '6': [
                " _ ",
                "|_ ",
                "|_|"
            ],
            '7': [
                " _ ",
                "  |",
                "  |"
            ],
            '8': [
                " _ ",
                "|_|",
                "|_|"
            ],
            '9': [
                " _ ",
                "|_|",
                " _|"
            ],
            ':': [
                "   ",
                " . ",
                " . "
            ]
        }
        display_lines = ["", "", ""]
        for char in char_hour:
            if char in dict_hour:
                numar = dict_hour[char]
                for i in range(3):
                    display_lines[i] += numar[i] + "   "
        for line in display_lines:
            print(line)



