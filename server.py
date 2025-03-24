"""Flask server for the Emotion Detection Web App."""

from flask import Flask, request, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route('/')
def home():
    """Render the main page of the application."""
    return render_template('index.html')

@app.route('/emotionDetector', methods=['GET', 'POST'])
def emotion_detection_api():
    """Handle emotion detection requests from the frontend."""
    if request.method == 'POST':
        text_to_analyze = request.form.get('text', '')
    else:
        text_to_analyze = request.args.get('textToAnalyze', '')

    result = emotion_detector(text_to_analyze)

    if result.get('dominant_emotion') is None:
        return "Invalid text! Please try again!"

    response_string = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )

    return response_string

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
