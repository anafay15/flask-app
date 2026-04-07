from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/health')
def health():
    return jsonify({"status": "ok"})

@app.route('/items')
def items():
    return jsonify(["item1", "item2", "item3"])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
