"""Functionality to run the app"""
from clock_system.clock import Clock
import time
import os

class DigitalClock:
    #Constructor with one attribute - one object created with class Clock.
    def __init__(self):
        self.clock = Clock()

    def clear_windows(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    #Method to run apps
    def run(self):
        while True:
            self.clock.get_current_hour()
            format_hour = self.clock.format_hour()
            self.clock.display_hour(format_hour)
            time.sleep(1)




