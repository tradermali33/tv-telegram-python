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
🚨  AMBEM • ELITE SIGNAL
━━━━━━━━━━━━━━━━━━━━━━━

🪙 Enstrüman : {symbol}
📊 Market    : SPOT / FUTURES
📈 Yön       : 🔵 AL (AMBEM CONFIRMED)

💰 Fiyat     : {price}
⏱️ Zaman     : {time}

━━━━━━━━━━━━━━━━━━━━━━━
🎯 STRATEJİ
━━━━━━━━━━━━━━━━━━━━━━━
• Likidite süpürülmesi tamamlandı
• Yapısal kırılım (BOS) onaylandı
• Momentum pozitif

━━━━━━━━━━━━━━━━━━━━━━━
📍 SEVİYELER
━━━━━━━━━━━━━━━━━━━━━━━
🎯 TP1 : %1.5
🎯 TP2 : %3.0
🎯 TP3 : %5.0

🛑 SL  : Son likidite altı

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
© AMBEM ANALYTICS • ELITE DESK
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