from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from googletrans import Translator
import requests

# Initialize Flask app
app = Flask(__name__)

# Define a simple route
@app.route("/")
def home():
    return "Flask app is running!"

# Route to handle incoming messages
@app.route("/sms", methods=["POST"])
def sms_reply():
    # Get the incoming message
    incoming_msg = request.form.get("Body")
    
    # Initialize response
    resp = MessagingResponse()
    msg = resp.message()
    
    if incoming_msg:
        translator = Translator()
        translated_msg = translator.translate(incoming_msg, dest="en").text
        msg.body(f"Translated to English: {translated_msg}")
    else:
        msg.body("No message received.")

    return str(resp)

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
