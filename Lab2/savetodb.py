import sqlite3
from datetime import datetime
from flask import Flask, request

app = Flask(__name__)

@app.route('/save_db', methods=['POST'])
def save_db():

    text_data = request.data.decode('utf-8')

    conn = sqlite3.connect('data.db')
    c = conn.cursor()

    c.execute('''
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            text TEXT,
            created TIMESTAMP
        )
    ''')

    c.execute('INSERT INTO messages (text, created) VALUES (?, ?)',
              (text_data, datetime.now()))

    conn.commit()
    conn.close()

    return "Дані збережено у базі data.db"

if __name__ == '__main__':
    app.run(port=8000)
