from flask import Flask, render_template, request
from googletrans import Translator

app = Flask(__name__)

# Define the dictionary mapping language codes to their full names
language_names = {
    'en': 'English',
    'fr': 'French',
    'es': 'Spanish',
    'de': 'German',
    'it': 'Italian',
    'pt': 'Portuguese',
    'nl': 'Dutch',
    'ru': 'Russian',
    'zh-CN': 'Chinese (Simplified)',
    'ja': 'Japanese',
    'hi': 'Hindi',
    'ta': 'Tamil',
    'te': 'Telugu',
    'ko': 'Korean',
    'ar': 'Arabic',
    'tr': 'Turkish',
    'pl': 'Polish',
    # Add more language codes and names as needed
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate():
    if request.method == 'POST':
        text = request.form['text']
        dest_lang = request.form['dest_lang']

        translator = Translator()
        translation = translator.translate(text, dest=dest_lang)

        return render_template('result.html', 
                               translation=translation.text,
                               original_text=text,
                               dest_lang=language_names.get(dest_lang, dest_lang))

if __name__ == '__main__':
    app.run(debug=True)
