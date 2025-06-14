from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)
model = joblib.load('absa_model.pkl')

def predict_sentiment(review, aspect):
    # Dummy function – replace with real prediction
    if "bad" in review.lower():
        return "negative"
    elif "good" in review.lower():
        return "positive"
    return "neutral"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    review = data.get('review')
    aspects = data.get('aspects')
    
    results = {}
    for aspect in aspects:
        results[aspect] = predict_sentiment(review, aspect)
    
    return jsonify(results)

if __name__ == '__main__':
    app.run()
