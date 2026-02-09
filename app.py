# ... (önceki flask ve telegram importları aynı kalıyor)

@app.route('/webhook', methods=['POST'])
def webhook():
    try:
        data = request.get_json() or {}
        
        alert_type = data.get('type', 'BILINMEYEN').upper()
        symbol    = data.get('symbol', '—')
        price     = data.get('price', '—')
        tf        = data.get('tf', '1m')
        time_str  = data.get('time', '—')
        emoji     = data.get('emoji', '⚠️')

        # Her sinyal türüne özel başlık ve açıklama
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

        bot.send_message(
            chat_id=CHAT_ID,
            text=message,
            parse_mode='HTML',
            disable_notification=False
        )

        return jsonify({"status": "gönderildi"}), 200

    except Exception as e:
        print("Hata:", str(e))
        return jsonify({"error": str(e)}), 500