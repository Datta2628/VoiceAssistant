from flask import Flask, render_template, jsonify
from voice_assistant import wishMe, takeCommand

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start-assistant')
def start_assistant():
    wishMe()
    query = takeCommand().lower()

    # Add your voice assistant logic here (from voice_assistant.py)

    return jsonify({'message': 'Voice assistant started.'})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
