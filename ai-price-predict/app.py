from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Load the AI model we just trained
model = joblib.load('price_model.pkl')

@app.route('/predict', methods=['GET'])
def predict():
    try:
        # Get data from the URL: ?qty=10&cat=1
        qty = request.args.get('qty', type=float)
        cat = request.args.get('cat', type=float)

        if qty is None or cat is None:
            return jsonify({"error": "Missing parameters. Use ?qty=X&cat=Y"}), 400

        # AI makes a prediction based on input
        prediction = model.predict([[qty, cat]])
        
        return jsonify({
    "status": "success",
    "recommended_price": round(float(prediction[0]), 2)
})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__': 
    # Run the server on port 5000
    app.run(host='0.0.0.0', port=5000, debug=True)