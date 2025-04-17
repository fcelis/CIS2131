# *****************************************************
# Developer: Fernando Celis
# Date: 03/19/2025
# Class: CIS2131 / Python Programming
# Project: Class Registration System
# File: registration_system.py
# Description: Handles the class registration system
# *****************************************************

from prettytable import PrettyTable
from class_model import Class
from data_handler import load_data, save_data


class RegistrationSystem:
    def __init__(self, reset=True):
        # Initializes the registration system and optionally resets stored data.
        if reset:
            save_data({})
        self.classes = {code: Class(code, **details) for code, details in load_data().items()}

    def save(self):
        # Saves the class data to JSON.
        save_data({code: cls.to_dict() for code, cls in self.classes.items()})

    def create_class(self, code, name, max_size):
        #Creates a new class if the code is unique.
        if code not in self.classes:
            self.classes[code] = Class(code, name, max_size)
            self.save()
            return f"Class {name} ({code}) created with max size {max_size}."
        return "Class code already exists."

    def delete_class(self, code):
        # Deletes a class from the system.
        if code in self.classes:
            del self.classes[code]
            self.save()
            return f"Class {code} deleted."
        return "Class not found."

    def update_class(self, code, new_max_size):
        # Updates the maximum size of a class.
        if code in self.classes:
            self.classes[code].max_size = new_max_size
            self.save()
            return f"Class {code} updated with new max size {new_max_size}."
        return "Class not found."

    def view_class_roster(self, code=None):
        # Displays the roster of students for a single class or all classes.
        if code:
            if code in self.classes:
                class_obj = self.classes[code]
                table = PrettyTable()
                table.title = f"{class_obj.name} ({code}) - Enrolled: {len(class_obj.roster)}/{class_obj.max_size}"
                table.field_names = ["Class Code", "Class Name", "Students"]
                for student in class_obj.roster:
                    table.add_row([code, class_obj.name, student])
                if not class_obj.roster:
                    table.add_row([code, class_obj.name, "No students enrolled."])
                return table
            return "Class not found."

        output = ""
        for class_obj in self.classes.values():
            table = PrettyTable()
            table.title = f"{class_obj.name} ({class_obj.code}) - Enrolled: {len(class_obj.roster)}/{class_obj.max_size}"
            table.field_names = ["Class Code", "Class Name", "Students"]
            for student in class_obj.roster:
                table.add_row([class_obj.code, class_obj.name, student])
            if not class_obj.roster:
                table.add_row([class_obj.code, class_obj.name, "No students enrolled."])
            output += str(table) + "\n\n"
        return output.strip()

    def enroll_student(self, student_name, class_code):
        # Enrolls a student in a class.
        if class_code in self.classes:
            result = self.classes[class_code].enroll_student(student_name)
            self.save()
            return result
        return "Class not found."

    def un_enroll_student(self, student_name, class_code):
        # Un-enrolls a student from a class.
        if class_code in self.classes:
            result = self.classes[class_code].un_enroll_student(student_name)
            self.save()
            return result
        return "Class not found."

    def student_schedule(self, student_name):
        # Displays the schedule of classes a student is enrolled in.
        schedule = [c.name for c in self.classes.values() if student_name in c.roster]
        table = PrettyTable()
        table.field_names = ["Student Name", "Enrolled Classes"]
        for class_name in schedule:
            table.add_row([student_name, class_name])
        if not schedule:
            table.add_row([student_name, "No classes enrolled."])
        return table
