from flask import Flask, request, jsonify
from twilio.twiml.messaging_response import MessagingResponse
from googletrans import Translator
import logging

# Initialize the Flask app
app = Flask(__name__)

# Set up logging for debugging
logging.basicConfig(level=logging.DEBUG)

# Define the /sms route with POST method
@app.route('/sms', methods=['POST'])
def sms_reply():
    # Log the incoming request data for debugging
    app.logger.debug(f"Request data: {request.form}")

    # Get the message body from the request
    body = request.form.get('Body')

    # If the Body is missing, return a 400 Bad Request error
    if not body:
        app.logger.warning("Body parameter is missing.")
        return jsonify({"error": "Body parameter is required"}), 400

    try:
        # Initialize the Google Translator
        translator = Translator()

        # Translate the incoming message to English
        translated = translator.translate(body, src='auto', dest='en')

        # Create a Twilio MessagingResponse
        response = MessagingResponse()
        response.message(f"Translated to English: {translated.text}")

        # Return the response as a string
        return str(response), 200

    except Exception as e:
        # Log the error and return a friendly message
        app.logger.error(f"Error occurred: {str(e)}")
        return jsonify({"error": "An error occurred during translation"}), 500


# Run the app if executed directly
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
