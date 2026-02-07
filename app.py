from flask import Flask, request
import requests
import os

app = Flask(__name__)

BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json or {}

    symbol = data.get("symbol", "N/A")
    price = data.get("price", "N/A")
    time = data.get("time", "N/A")

    message = f"""📊 PRICE ALERT

Sembol: {symbol}
Fiyat: {price}
Saat: {time}
"""

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(url, json={
        "chat_id": CHAT_ID,
        "text": message
    })

    return "ok", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
