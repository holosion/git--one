# Stack to store students and calculate average marks




class Stack:
    def __init__(self):
        self.students = []

    def push(self, student):
        self.students.append(student)

    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        return self.students.pop()

    def peek(self):
        if self.is_empty():
            return "Stack is empty"
        return self.students[-1]

    def size(self):
        return len(self.students)

    def is_empty(self):
        return len(self.students) == 0

    def display(self):
        return self.students


# Main program with menu
'''stack = Stack()

while True:
    print("\n--- STACK MENU ---")
    print("1. Add Student (Push)")
    print("2. Remove Student (Pop)")
    print("3. View Top Student (Peek)")
    print("4. Show All Students")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        course_units = int(input("Enter number of course units: "))

        marks = []
        for i in range(course_units):
            mark = int(input(f"Enter mark for course unit {i+1}: "))
            marks.append(mark)

        student = Student(name, marks)
        stack.push(student)
        print("Student added to stack.")

    elif choice == "2":
        removed = stack.pop()
        print("Removed student:", removed if isinstance(removed, str) else removed)

    elif choice == "3":
        top_student = stack.peek()
        print("Top student:", top_student)

    elif choice == "4":
        if stack.is_empty():
            print("Stack is empty.")
        else:
            print("All students in stack:")
            for student in stack.display():
                print(student)

    elif choice == "5":
        print("Exiting program.")
        break

    else:
        print("Invalid choice. Try again.")'''
