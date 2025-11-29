from flask import Flask, request, jsonify
import pickle
import pandas as pd

app = Flask(__name__)

# -----------------------------
# Load Model and Columns
# -----------------------------
model = pickle.load(open("model/predictor.pickle", "rb"))
columns = pickle.load(open("model/model_columns.pkl", "rb"))

# -----------------------------
# Prediction Endpoint
# -----------------------------
@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Read JSON input
        data = request.get_json()

        # Convert input to DataFrame
        df = pd.DataFrame([data])

        # Reorder missing columns
        df = df.reindex(columns=columns, fill_value=0)

        # Predict
        prediction = model.predict(df)[0]

        return jsonify({
            "success": True,
            "prediction": float(prediction)
        })

    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 400


@app.route("/", methods=["GET"])
def home():
    return {"service": "Laptop Price Prediction API", "status": "running"}


if __name__ == "__main__":
    app.run(port=5001, debug=True)
