from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello from the DevSecOps demo app!"


if __name__ == "__main__":
    # Debug server for local testing only – not for production
    app.run(host="0.0.0.0", port=8000)
