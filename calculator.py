from flask import Flask, request, jsonify, send_from_directory

app = Flask(__name__)

@app.route('/')
def home():
    return open('index.html').read()

@app.route('/<path:filename>')
def serve_static(filename):
    return send_from_directory('.', filename)

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    operation = data.get('operation')
    num1 = data.get('num1')
    num2 = data.get('num2')

    # Input validation
    if num1 is None or num2 is None:
        return jsonify({'error': 'Both num1 and num2 are required.'}), 400
    try:
        num1 = float(num1)
        num2 = float(num2)
    except ValueError:
        return jsonify({'error': 'Invalid input: num1 and num2 must be numbers.'}), 400

    if operation == 'add':
        result = num1 + num2
    elif operation == 'subtract':
        result = num1 - num2
    elif operation == 'multiply':
        result = num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return jsonify({'error': 'Cannot divide by zero'}), 400
        result = num1 / num2
    else:
        return jsonify({'error': f'Invalid operation: {operation}'}), 400

    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)
