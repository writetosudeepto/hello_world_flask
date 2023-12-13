from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/api/greeting', methods=['GET'])
def get_greeting():
    return jsonify({'message': 'Hello, this is your Flask API!'})


if __name__ == '__main__':
    app.run(debug=True)
