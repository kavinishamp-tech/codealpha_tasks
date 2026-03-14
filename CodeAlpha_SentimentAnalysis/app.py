from flask import Flask, render_template, request
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

app = Flask(__name__)
analyzer = SentimentIntensityAnalyzer()

@app.route("/", methods=["GET", "POST"])
def home():
    sentiment = ""
    
    if request.method == "POST":
        text = request.form["text"]
        score = analyzer.polarity_scores(text)["compound"]

        if score >= 0.05:
            sentiment = "Positive 😊"
        elif score <= -0.05:
            sentiment = "Negative 😞"
        else:
            sentiment = "Neutral 😐"

    return render_template("index.html", sentiment=sentiment)

if __name__ == "__main__":
    app.run(debug=True)