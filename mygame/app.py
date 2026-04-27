from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

words = ['PYTHON', 'FLASK', 'BRAIN', 'CLOUD', 'SMILE', 
         'EARTH', 'MUSIC', 'DANCE', 'LIGHT', 'STONE']

@app.route('/')
def home():
    word = random.choice(words)
    return render_template('index.html', word=word)

@app.route('/check', methods=['POST'])
def check():
    data = request.json
    guess = data['guess'].upper()
    word = data['word'].upper()
    
    result = []
    for i in range(len(word)):
        if i < len(guess):
            if guess[i] == word[i]:
                result.append('correct')
            elif guess[i] in word:
                result.append('present')
            else:
                result.append('absent')
        else:
            result.append('absent')
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)