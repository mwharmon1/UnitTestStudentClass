"""
Author: Michael Harmon
Last Date Modified: 10/28/2019
Description: The student class will validate and create student data
"""


class Student:
    def __init__(self, lname, fname, major, gpa=0.0):
        valid_name_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'-")
        if not (valid_name_characters.issuperset(lname) and valid_name_characters.issuperset(fname)):
            raise ValueError
        if not (valid_name_characters.issuperset(major)):
            raise ValueError
        if not isinstance(gpa, float):
            raise ValueError
        elif gpa not in range(0, 5):
            raise ValueError
        self.last_name = lname
        self.first_name = fname
        self.major = major
        self.gpa = gpa

    def __str__(self):
        return self.last_name + ", " + self.first_name + " has major " + self.major + " with gpa: " + str(self.gpa)
