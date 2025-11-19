from flask import Flask, request

app = Flask(__name__)

@app.route("/save_text", methods=["POST"])
def save_text():
    text_data = request.data.decode('utf-8')
    with open('data.txt', 'a', encoding='utf-8') as f:
        f.write(text_data + '\n')
    return "Дані збережено у файл data.txt"

if __name__ == "__main__":
    app.run(port=8000)
