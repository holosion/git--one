# import flask tools
from flask import Flask, render_template, request, redirect, url_for, flash

# import stack and student classes
from stack import Stack
from student import Student

# create the flask application
app = Flask(__name__)
app.secret_key = 'your_secret_key'  # for flash messages

# create the stack
stack = Stack()


# home page
@app.route('/')
def home():
    complexity_info = {
        'push_time': 'O(1)',
        'push_space': 'O(1) amortized',
        'pop_time': 'O(1)',
        'pop_space': 'O(1)',
        'overall_space': f'O({stack.size()})'
    }
    
    # Convert Student objects to dictionaries for JSON serialization
    students_data = [
        {"name": student.name, "marks": student.marks, "average": student.average}
        for student in stack.display()
    ]
    return render_template('index.html', students=students_data, complexity=complexity_info)


# push student into stack
@app.route("/push", methods=["POST"])
def push():

    name = request.form["name"]
    marks_input = request.form["marks"]

    # gracefully parse marks, ignoring invalid inputs to prevent a server crash
    marks = []
    for m in marks_input.split(","):
        if m.strip().isdigit():
            marks.append(int(m.strip()))

    student = Student(name, marks)

    time_taken = stack.push(student)

    # flash message with time taken
    flash(f"Student added successfully! Time taken: {time_taken:.6f} seconds", "success")

    # redirect to home page
    return redirect(url_for("home"))


# pop student from stack
@app.route("/pop")
def pop():

    popped, time_taken = stack.pop()
    
    if popped == "Stack is empty":
        flash("Stack is empty!", "error")
    else:
        flash(f"Student removed successfully! Time taken: {time_taken:.6f} seconds", "success")

    # redirect to home page
    return redirect(url_for("home"))


# start the server
if __name__ == "__main__":
    app.run(debug=True)