from flask import Flask, request, jsonify, render_template
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
    # Get the message body from the request
    body = request.form.get('Body')
    
    # If the Body is missing, return a 400 Bad Request error
    if not body:
        app.logger.warning("Body parameter is missing.")
        return jsonify({"error": "Body parameter is required"}), 400

    try:
        # Initialize the Google Translator
        translator = Translator()

        # Detect the language of the input text
        detected = translator.detect(body)
        detected_lang = detected.lang

        # Translate the incoming message to English
        translated = translator.translate(body, src='auto', dest='en')

        # Return the detected language and translated text
        return jsonify({
            "detected_language": detected_lang,
            "translated_text": translated.text
        }), 200

    except Exception as e:
        # Log the error and return a friendly message
        app.logger.error(f"Error occurred: {str(e)}")
        return jsonify({"error": "An error occurred during translation"}), 500


# Serve the web interface
@app.route('/')
def home():
    return render_template('index.html')

# Run the app if executed directly
if __name__ == '__main__':
    app.run(debug=True)
