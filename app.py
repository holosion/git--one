# import flask tools
from flask import Flask, render_template, request, redirect, url_for

# import stack and student classes
from stack import Stack
from student import Student

# create the flask application
app = Flask(__name__)

# create the stack
stack = Stack()


# home page
@app.route('/')
def home():
    return render_template('index.html', students=stack.display())


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

    stack.push(student)

    # redirect to home page
    return redirect(url_for("home"))


# pop student from stack
@app.route("/pop")
def pop():

    stack.pop()

    # redirect to home page
    return redirect(url_for("home"))


# start the server
if __name__ == "__main__":
    app.run(debug=True)