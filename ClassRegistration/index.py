# *****************************************************
# Developer: Fernando Celis
# Date: 03/19/2025
# Class: CIS2131 / Python Programming
# Project: Class Registration System
"""
Description:
This project implements a simple class registration system that allows administrators to manage
classes and students to enroll in them. The system supports two operational modes:
Administrator and Student.
"""
# *****************************************************

# main.py - Runs the interactive menu for admin and student actions
from registration_system import RegistrationSystem

def main():
    # Main interactive loop for the class registration system.
    # Ask user whether to load existing data or start fresh
    while True:
        choice = input("Do you want to load existing registration data? (yes/no): ").strip().lower()
        if choice in ["yes", "y"]:
            system = RegistrationSystem(reset=False)
            break
        elif choice in ["no", "n"]:
            system = RegistrationSystem(reset=True)
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
        #    system = RegistrationSystem()

    while True:
        mode = input("Enter mode (admin/student/exit): ").lower()
        if mode == "exit":
            break
        elif mode == "admin":
            while True:
                action = input("Admin Actions: create/update/delete/view/exit: ").lower()
                if action == "exit":
                    break
                elif action == "create":
                    code = input("Class code: ")
                    name = input("Class name: ")
                    max_size = int(input("Max size: "))
                    print(system.create_class(code, name, max_size))
                elif action == "delete":
                    code = input("Class code: ")
                    print(system.delete_class(code))
                elif action == "update":
                    code = input("Class code: ")
                    new_max_size = int(input("New max size: "))
                    print(system.update_class(code, new_max_size))
                elif action == "view":
                    if not system.classes:
                        print("No classes registered. Please register a class first.")
                    else:
                        code = input("Class code (or press Enter to view all): ")
                        print(system.view_class_roster(code if code else None))
        elif mode == "student":
            while True:
                action = input("Student Actions: enroll/un-enroll/schedule/exit: ").lower()
                if action == "exit":
                    break
                elif action == "enroll":
                    student_name = input("Student name: ")
                    class_code = input("Class code: ")
                    print(system.enroll_student(student_name, class_code))
                elif action == "un-enroll":
                    student_name = input("Student name: ")
                    class_code = input("Class code: ")
                    print(system.un_enroll_student(student_name, class_code))
                elif action == "schedule":
                    student_name = input("Student name: ")
                    print(system.student_schedule(student_name))


if __name__ == "__main__":
    main()
