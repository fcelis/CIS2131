## Instructions

#### Objective:

Create a Python program for a class registration system that supports both administrator and student modes. Administrators can manage classes (create, update, delete) and view class rosters. Students can enroll in classes, view their schedules, and un-enroll from classes.

#### Requirements:

1. **Class Management:**
    
    - Administrators can create classes with a name and a maximum size.
    - Classes are stored with their name and roster of registered students.
2. **Enrollment:**
    
    - Students can enroll in classes if there is available space in the class.
3. **Un-enrollment:**
    
    - Students can un-enroll from classes, removing their name from the roster.
4. **Modes:**
    
    - **Administrator Mode:**
        - Create, update, delete classes.
        - Print class rosters.
    - **Student Mode:**
        - Enroll in classes.
        - Print class schedule.
        - Un-enroll from classes.
5. **Error Handling:**
    
    - Handle cases such as exceeding class size limits, attempting to un-enroll from a class not enrolled in, etc.

#### Rubric:

| Criteria                                     | Points |
| -------------------------------------------- | ------ |
| **Class Creation (per class)**               | 3      |
| **Enrollment Handling**                      | 3      |
| **Un-enrollment Handling**                   | 2      |
| **Administrator Mode (CRUD)**                | 4      |
| **Student Mode (Enroll/Un-enroll/Schedule)** | 4      |
| **Error Handling and Robustness**            | 2      |
