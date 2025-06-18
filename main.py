from flask import Flask
import os

app = Flask(__name__)
version = os.environ.get("VERSION", "dev")

@app.route("/")
def hello():
    return f"Hello from Cloud Run Welcomes you! Version: {version}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
