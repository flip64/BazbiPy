from flask import Flask, request, jsonify
from fetch_price import fetch_price

app = Flask(__name__)

@app.route('/')
def home():
    return "🟢 BazbiPy API is running"

@app.route('/get-price', methods=['GET'])
def get_price():
    url = request.args.get('url')
    if not url:
        return jsonify({'error': 'پارامتر url الزامی است'}), 400

    price = fetch_price(url)
    return jsonify({'price': price})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
