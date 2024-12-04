from flask import Flask, request, render_template, jsonify
from transformers import pipeline

app = Flask(__name__)

# Load the translation model
translator = pipeline("translation_en_to_fi", model="Helsinki-NLP/opus-mt-en-fi")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/translate", methods=["POST"])
def translate():
    text_to_translate = request.form["text"]
    if not text_to_translate.strip():
        return jsonify({"error": "Text field is empty"}), 400

    # Perform translation
    translated_text = translator(text_to_translate)[0]["translation_text"]
    return jsonify({"translated_text": translated_text})

if __name__ == "__main__":
    app.run(debug=True)
