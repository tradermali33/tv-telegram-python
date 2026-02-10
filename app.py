from flask import Flask, request, jsonify
import telegram
import os
import asyncio  # await için gerekli

# Ortam değişkenlerini oku
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

if not TELEGRAM_TOKEN or not CHAT_ID:
    print("HATA: TELEGRAM_TOKEN veya CHAT_ID eksik!")

bot = telegram.Bot(token=TELEGRAM_TOKEN)

app = Flask(__name__)  # ← BU SATIR ÇOK ÖNEMLİ – burada tanımlanmalı!

@app.route('/webhook', methods=['POST'])
async def webhook():
    try:
        data = request.get_json() or {}
        
        alert_type = data.get('type', 'BILINMEYEN').upper()
        symbol    = data.get('symbol', '—')
        price     = data.get('price', '—')
        tf        = data.get('tf', '1m')
        time_str  = data.get('time', '—')
        emoji     = data.get('emoji', '⚠️')

        messages = {
            "BOS_BULL":     ("🟢 BOS",          "Yükseliş Yapı Kırılımı"),
            "BOS_BEAR":     ("🔴 BOS",          "Düşüş Yapı Kırılımı"),
            "CHOCH_BULL":   ("🟢 CHoCH",        "Yükseliş Karakter Değişimi"),
            "CHOCH_BEAR":   ("🔴 CHoCH",        "Düşüş Karakter Değişimi"),
            "IBOS_BULL":    ("🟢 iBOS",         "İç Yapı - Yükseliş Kırılım"),
            "IBOS_BEAR":    ("🔴 iBOS",         "İç Yapı - Düşüş Kırılım"),
            "ICHOCH_BULL":  ("🟢 iCHoCH",       "İç Yapı - Yükseliş Değişim"),
            "ICHOCH_BEAR":  ("🔴 iCHoCH",       "İç Yapı - Düşüş Değişim"),
            "OB_BULL":      ("🟩 OB",           "Yeni Yükseliş Order Block"),
            "OB_BEAR":      ("🟥 OB",           "Yeni Düşüş Order Block"),
            "EQH":          ("📌 EQH",          "Equal Highs - Üst Likidite"),
            "EQL":          ("📍 EQL",          "Equal Lows - Alt Likidite"),
            "FVG_BULL":     ("🟩 FVG",          "Bullish Fair Value Gap"),
            "FVG_BEAR":     ("🟥 FVG",          "Bearish Fair Value Gap"),
        }

        title, desc = messages.get(alert_type, ("⚠️ BİLİNMEYEN", "Tanımlanamayan sinyal"))

        message = (
            f"{emoji} <b>{title}</b>\n"
            f"────────────────────\n"
            f"• Sembol: <b>{symbol}</b>\n"
            f"• Fiyat: <b>{price}</b>\n"
            f"• Zaman: {time_str}\n"
            f"• Açıklama: {desc}\n"
            "────────────────────\n"
            f"<i>1m zaman dilimi - LuxAlgo SMC</i>"
        )

        await bot.send_message(
            chat_id=CHAT_ID,
            text=message,
            parse_mode='HTML',
            disable_notification=False
        )

        return jsonify({"status": "gönderildi"}), 200

    except Exception as e:
        print("Hata:", str(e))
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)