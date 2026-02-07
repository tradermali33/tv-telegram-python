from flask import Flask, request
import requests
import os

app = Flask(__name__)

BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json(force=True)   # 🔥 KRİTİK SATIR

    symbol = data.get("symbol", "N/A")
    price = data.get("price", "N/A")
    time = data.get("time", "N/A")

    message = f"""📊 PRICE ALERT

Symbol: {symbol}
Fiyat: {price}
Saat: {time}
"""

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(url, json={
        "chat_id": CHAT_ID,
        "text": message
    })

    return "ok", 200