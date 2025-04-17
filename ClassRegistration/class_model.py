# *****************************************************
# Developer: Fernando Celis
# Date: 03/19/2025
# Class: CIS2131 / Python Programming
# Project: Class Registration System
# File: class_model.py
# Description: Handles the student enrollment and un-enrollment to a class
# *****************************************************
class Class:
    def __init__(self, code, name, max_size, roster=None):
        # Initializes a class with a code, name, maximum size, and roster of students.
        self.code = code
        self.name = name
        self.max_size = max_size
        self.roster = roster if roster else []

    def enroll_student(self, student_name):
        # Enrolls a student in the class if there is space.
        if len(self.roster) < self.max_size:
            if student_name not in self.roster:
                self.roster.append(student_name)
                return f"{student_name} enrolled in {self.name}."
            return f"{student_name} is already enrolled in {self.name}."
        return "Class is full. Enrollment failed."

    def un_enroll_student(self, student_name):
        # Removes a student from the class if they are enrolled.
        if student_name in self.roster:
            self.roster.remove(student_name)
            return f"{student_name} un-enrolled from {self.name}."
        return f"{student_name} is not enrolled in {self.code} - {self.name}."

    def to_dict(self):
        # Returns the class data as a dictionary.
        return {"name": self.name, "max_size": self.max_size, "roster": self.roster}
