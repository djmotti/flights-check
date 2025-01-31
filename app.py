import os
from flask import Flask, render_template, request, jsonify
from langdetect import detect
from twilio.rest import Client

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    try:
        # Debugging: Print the current working directory
        print("Current Working Directory:", os.getcwd())

        # Print the expected path to index.html
        template_path = os.path.join(os.getcwd(), "templates", "index.html")
        print("Expected index.html Path:", template_path)

        # Check if index.html exists
        if not os.path.exists(template_path):
            raise FileNotFoundError("index.html not found in the templates folder.")

        return render_template("index.html")
    except Exception as e:
        app.logger.error(f"Error rendering index.html: {e}")
        return f"<h1>Error loading the home page</h1><p>{e}</p>", 500

@app.route("/sms", methods=["POST"])
def sms():
    try:
        data = request.get_json()
        message = data.get("Body", "")

        # Detect language of the message
        detected_language = detect(message)

        # Respond with the detected language
        response = {
            "message": message,
            "detected_language": detected_language
        }
        return jsonify(response)

    except Exception as e:
        app.logger.error(f"Error processing SMS: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
