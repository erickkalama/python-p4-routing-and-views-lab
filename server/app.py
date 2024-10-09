#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)


# Route for index
@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

# Route for printing a message
@app.route('/print/<string:text>')
def print_text(text):
    print(text)  # To display the message in the console
    return text  # To display the message in the browser

# Route for counting up to a given number
@app.route('/count/<int:num>')
def count(num):
    return '\n'.join(str(i) for i in range(num))+'\n'

# Route for performing math operations
@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math_operation(num1, operation, num2):
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        result = num1 / num2
    elif operation == '%':
        result = num1 % num2
    else:
        return 'Invalid operation', 400
    return str(result)

if __name__ == '__main__':
    app.run(debug=True)
