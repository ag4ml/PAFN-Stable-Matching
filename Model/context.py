import openpyxl
import os
from Model.advisee import Advisee
from Model.advisor import Advisor

class Context:
    def __init__(self):
        self.advisors = []
        self.advisees = []
        self.populate_advisors()
        self.populate_advisees()

    def populate_advisors(self):
        return None