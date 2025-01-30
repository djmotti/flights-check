from flask import Flask, request, render_template, jsonify
from googletrans import Translator
from langdetect import detect
from twilio.rest import Client
import os

app = Flask(__name__)

# Twilio configuration (replace with your actual credentials or set as environment variables)
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID", "your_account_sid")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN", "your_auth_token")
TWILIO_PHONE_NUMBER = os.getenv("TWILIO_PHONE_NUMBER", "your_twilio_phone_number")

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

# Translator instance
translator = Translator()

@app.route("/", methods=["GET"])
def home():
    try:
        return render_template("index.html")
    except Exception as e:
        app.logger.error(f"Error rendering index.html: {e}")
        return "Error loading the home page.", 500

@app.route("/translate", methods=["POST"])
def translate_message():
    try:
        data = request.get_json()
        message = data.get("message")
        target_language = data.get("target_language", "en")

        if not message:
            return jsonify({"error": "Message is required"}), 400

        # Detect the language of the message
        detected_language = detect(message)

        # Translate the message
        translated = translator.translate(message, src=detected_language, dest=target_language)
        return jsonify({
            "original_message": message,
            "detected_language": detected_language,
            "translated_message": translated.text,
            "target_language": target_language
        })
    except Exception as e:
        app.logger.error(f"Error translating message: {e}")
        return jsonify({"error": "An error occurred during translation"}), 500

@app.route("/send_sms", methods=["POST"])
def send_sms():
    try:
        data = request.get_json()
        to_number = data.get("to_number")
        message = data.get("message")

        if not to_number or not message:
            return jsonify({"error": "Both 'to_number' and 'message' are required"}), 400

        # Send SMS
        sms = client.messages.create(
            body=message,
            from_=TWILIO_PHONE_NUMBER,
            to=to_number
        )
        return jsonify({"message_sid": sms.sid, "status": "Message sent successfully"})
    except Exception as e:
        app.logger.error(f"Error sending SMS: {e}")
        return jsonify({"error": "An error occurred while sending SMS"}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
