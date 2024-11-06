from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
app.config.from_object(__name__)

CORS(app, resources={r"/*": {"origins": "*"}})


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/ping")
def ping_pong():
    return jsonify("pong!")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5555, debug=True)
