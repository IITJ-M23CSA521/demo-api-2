from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify(message="This is demo-api-2.", status="success")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050)
