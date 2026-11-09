"""Serve the Emotion Detector web application."""
from flask import Flask, render_template, request
from requests import RequestException
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)


@app.route("/")
def index():
    """Display the input form."""
    return render_template("index.html")


@app.route("/emotionDetector")
def detect_emotion():
    """Analyze input and present emotion scores."""
    text = request.args.get("textToAnalyze", "")
    if not text.strip():
        return "Invalid text! Please try again!"
    try:
        result = emotion_detector(text)
    except RequestException:
        return "Emotion service unavailable. Please try again later.", 503
    if result["dominant_emotion"] is None:
        return "Invalid text! Please try again!"
    scores = ", ".join(
        f"'{name}': {result[name]}"
        for name in ("anger", "disgust", "fear", "joy", "sadness")
    )
    return (f"For the given statement, the system response is {scores}. "
            f"The dominant emotion is {result['dominant_emotion']}.")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
