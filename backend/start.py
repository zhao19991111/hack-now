from flask import Flask, request, Response, jsonify
app = Flask(__name__,
            static_url_path='',
            static_folder='./frontend/build')


@app.route("/", methods=["get"])
def __init__():
    return "Hello World!"


if __name__ == "__main__":
    app.run(port=9000)
