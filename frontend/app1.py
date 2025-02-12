from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from googletrans import Translator

app = Flask(__name__, template_folder="templates", static_folder="static")
CORS(app)  # Enable CORS for frontend communication
translator = Translator()

@app.route('/')
def index():
    return render_template('index.html')  

@app.route('/get_response', methods=['POST'])
def translate_text():
    data = request.json
    user_text = data.get("message", "")
    source_lang = data.get("from_lang", "auto")  
    target_lang = "en" 

    if not user_text:
        return jsonify({"response": "No text provided!"})

    try:
        translated = translator.translate(user_text, src=source_lang, dest=target_lang)
        return jsonify({"response": translated.text})
    except Exception as e:
        return jsonify({"response": f"Translation error: {str(e)}"})

if __name__ == '__main__':
    app.run(debug=True)
