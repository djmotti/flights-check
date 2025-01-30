from flask import Flask, render_template, request, jsonify
from langdetect import detect
from twilio.rest import Client
import os

app = Flask(__name__)

# Twilio Configuration (Replace with your actual credentials)
TWILIO_ACCOUNT_SID = "your_account_sid"
TWILIO_AUTH_TOKEN = "your_auth_token"
TWILIO_PHONE_NUMBER = "your_twilio_phone_number"

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

@app.route("/", methods=["GET"])
def home():
    try:
        # Debugging: Print the current working directory
        print("Current Working Directory:", os.getcwd())

        # Check if the templates folder and index.html exist
        template_path = os.path.join(os.getcwd(), "templates", "index.html")
        if not os.path.exists(template_path):
            raise FileNotFoundError("index.html not found in the templates folder.")

        return render_template("index.html")
    except Exception as e:
        app.logger.error(f"Error rendering index.html: {e}")
        return f"<h1>Error loading the home page</h1><p>{e}</p>", 500

@app.route("/send_sms", methods=["POST"])
def send_sms():
    try:
        # Extract data from the request
        data = request.get_json()
        message_body = data.get("message", "")
        recipient_number = data.get("to", "")

        # Detect language of the message
        detected_language = detect(message_body)

        # Send SMS using Twilio
        message = client.messages.create(
            body=f"[{detected_language}] {message_body}",
            from_=TWILIO_PHONE_NUMBER,
            to=recipient_number
        )

        return jsonify({"status": "success", "message_sid": message.sid})
    except Exception as e:
        app.logger.error(f"Error sending SMS: {e}")
        return jsonify({"status": "error", "error": str(e)}), 500

if __name__ == "__main__":
    # Debugging: Print a message when the server starts
    print("Starting the Flask app...")
    app.run(debug=True)
