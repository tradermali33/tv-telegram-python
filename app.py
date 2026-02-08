from flask import Flask, request
import requests
import os

app = Flask(__name__)

BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")

@app.route("/", methods=["GET"])
def home():
    return "Bot is running", 200


@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json(force=True)

    symbol = data.get("symbol", "N/A")
    price = data.get("price", "N/A")
    time = data.get("time", "N/A")

    message = f"""
━━━━━━━━━━━━━━━━━━━━━━━
⚡️ TRADERMALI33 ⚡️
━━━━━━━━━━━━━━━━━━━━━━━

🪙 Enstrüman : {symbol}
📊 Market    : SPOT / FUTURES
📈 Yön       : 🔵 AL (AMBEM CONFIRMED)

💰 Fiyat     : {price}
⏱️ Zaman     : {time}

━━━━━━━━━━━━━━━━━━━━━━━
🎯 STRATEJİ
━━━━━━━━━━━━━━━━━━━━━━━
ATTIĞIN ADIMA DİKKAT ET
YOKSA BORUYU SOKARLAR 
HABERİN OLMAZ
━━━━━━━━━━━━━━━━━━━━━━━
📍 SEVİYELER
━━━━━━━━━━━━━━━━━━━━━━━
🎯 TP1 : KAR CEBE YAKIŞIR
🎯 TP2 : ÇORBA PARASI TAMAMSA KAÇ
🎯 TP3 : KAÇTIN KAÇTIN YOKSA SIÇTIN

━━━━━━━━━━━━━━━━━━━━━━━
📊 GRAFİK
━━━━━━━━━━━━━━━━━━━━━━━
https://www.tradingview.com/chart/?symbol={symbol}

━━━━━━━━━━━━━━━━━━━━━━━
⚠️ RİSK UYARISI
━━━━━━━━━━━━━━━━━━━━━━━
Bu bir yatırım tavsiyesi değildir.
Risk yönetimi kullanıcıya aittir.

━━━━━━━━━━━━━━━━━━━━━━━
© TRADERMALI33 ANALİZ SISTEMI BAŞARILAR DİLER
━━━━━━━━━━━━━━━━━━━━━━━
"""

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message
    }

    requests.post(url, json=payload)
    return "ok", 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)