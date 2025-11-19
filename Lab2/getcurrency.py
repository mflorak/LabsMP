from flask import Flask, request
import requests
import json
from datetime import datetime, timedelta

app = Flask(__name__)

@app.route("/currency", methods=["GET"])
def currency():
    param = request.args.get("param")

    if param == "today":
        date = datetime.today().strftime("%Y%m%d")
    elif param == "yesterday":
        date = (datetime.today() - timedelta(days=1)).strftime("%Y%m%d")
    else:
        return "неприпустимий параметр"

    url = f"https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?date={date}&json"
    try:
        response = requests.get(url)
        response.raise_for_status()

        data = json.loads(response.text)
    except Exception as e:
        return f"Помилка запиту к НБУ: {e}"

    usd_rate = next((item["rate"] for item in data if item["cc"] == "USD"), None)
    if usd_rate:
        return f"USD - {usd_rate}"
    else:
        return "Курс USD не знайдено"

if __name__ == "__main__":
    app.run(port=8000)
