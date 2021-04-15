from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello world"


# 6. Define main behavior
if __name__ == "__main__":
    app.run(debug=True)
