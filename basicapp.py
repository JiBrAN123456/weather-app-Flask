from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')  # Renders the HTML file

@app.route('/calculate')
def calculate():
    operation = request.args.get('operation')
    num1 = int(request.args.get('num1'))
    num2 = int(request.args.get('num2'))

    if operation == 'add':
        result = num1 + num2
    elif operation == 'subtract':
        result = num1 - num2
    elif operation == 'multiply':
        result = num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return "Cannot divide by zero!"
        result = num1 / num2
    else:
        return "Invalid Operation!"

    return f"Result: {result}"

if __name__ == '__main__':
    app.run(debug=True)
