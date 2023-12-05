from flask import Flask, render_template, request
from audio import speech_to_text
from character_responce import ai_palm_response
import sys
from audio import generate_audio
from character_responce import open_ai
from character import charcter_select

app = Flask(__name__)
l = charcter_select.select_character()
ai_palm_response = ai_palm_response.AIResponse("AIzaSyDiqEPDpI47Qd4Je3I3chb5-z2ZQyKu3gk", background=l[0])

@app.route('/')
def index():
    return render_template('index.html', character=l[3])

@app.route('/response', methods=['POST'])
def get_response():
    speech = request.form['speech']
    if speech.lower() == "disconnect call":
        sys.exit(0)
    elif speech.lower() == "what is your name":
        response = "I am " + l[3]
    else:
        prompt = "Stay in your character. Answer the question as a human as per your character {0}. Question: ".format(l[3])
        response = ai_palm_response.generate_res(prompt + speech)
        # You can also generate audio or handle the response in other ways as needed
    return render_template('index.html', character=l[3], speech=speech, response=response)

if __name__ == '__main__':
    app.run(debug=True)
