from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Witaj w moim API!"})

@app.route('/mojastrona')
def mojastrona():
    return "To jest moja strona!"

@app.route('/hello')
def hello():
    name = request.args.get('name', 'użytkownik')
    return jsonify({"message": f"Hello, {name}!"})

@app.route('/api/v1.0/predict')
def predict():
    # Pobierz parametry num1 i num2 z URL
    num1 = request.args.get('num1')
    num2 = request.args.get('num2')

    # Sprawdź, czy num1 i num2 są liczbami
    if num1 is None or num2 is None:
        return jsonify({"error": "Brakuje parametrów num1 lub num2."}), 400

    try:
        num1 = float(num1)
        num2 = float(num2)
    except ValueError:
        return jsonify({"error": "Podaj poprawne liczby num1 i num2 jako parametry URL."}), 400

    # Zastosowanie reguły decyzyjnej
    prediction = 1 if (num1 + num2) > 5.8 else 0

    return jsonify({
        "prediction": prediction,
        "features": {
            "num1": num1,
            "num2": num2
        }
    })

if __name__ == '__main__':
    app.run(debug=True)
