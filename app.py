import os
from flask import Flask, render_template, request, jsonify
from langdetect import detect

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    try:
        # Debugging: Print the current working directory
        print("Current Working Directory:", os.getcwd())

        # Ensure the templates folder and index.html exist
        template_folder_path = os.path.join(os.getcwd(), "templates")
        if not os.path.exists(template_folder_path):
            raise FileNotFoundError("Templates folder not found.")
        
        template_path = os.path.join(template_folder_path, "index.html")
        if not os.path.exists(template_path):
            raise FileNotFoundError("index.html not found in the templates folder.")
        
        return render_template("index.html")
    except Exception as e:
        app.logger.error(f"Error rendering index.html: {e}")
        return f"<h1>Error loading the home page</h1><p>{e}</p>", 500

@app.route("/sms", methods=["POST"])
def sms():
    try:
        # Get JSON data from the POST request
        data = request.get_json()
        if not data:
            return jsonify({"error": "No JSON payload received"}), 400

        # Extract the message body
        message = data.get("Body", "")
        if not message:
            return jsonify({"error": "No message content provided (Body is missing)"}), 400

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
    # Ensure debugging is enabled locally
    app.run(debug=True)
