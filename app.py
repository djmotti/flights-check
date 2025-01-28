from flask import Flask, request, jsonify
from twilio.twiml.messaging_response import MessagingResponse
from googletrans import Translator

# Initialize the Flask app
app = Flask(__name__)

# Define the /sms route with POST method
@app.route('/sms', methods=['POST'])
def sms_reply():
    # Get the message body from the request
    body = request.form.get('Body')

    if not body:
        return "Body parameter is missing.", 400  # Handle case where 'Body' is not provided

    # Initialize the Google Translator
    translator = Translator()

    # Translate the incoming message to English
    try:
        translated = translator.translate(body, src='auto', dest='en')
    except Exception as e:
        return jsonify({"error": str(e)}), 500  # Handle translation errors

    # Create a Twilio MessagingResponse
    response = MessagingResponse()
    response.message(f"Translated to English: {translated.text}")

    # Return the response as a string
    return str(response)

# Run the app if executed directly
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
