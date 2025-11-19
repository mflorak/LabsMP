from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/currency", methods=["GET"])
def currency():
    content_type = request.headers.get("Content-Type")
    if content_type == "application/json":
        return jsonify({"USD": 41.5})
    elif content_type == "application/xml":
        return "<currency><USD>41.5</USD></currency>"
    else:
        return "USD - 41,5"

if __name__ == "__main__":
    app.run(port=8000)
