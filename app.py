#Flask REST API 
from flask import Flask, request, jsonify
import logic, model

app = Flask(__name__)

@app.route("/")
def home():
    return "Expense Tracker API Running"

@app.route("/expenses", methods=["POST"])
def add_expense():
    data = request.json
    amount = data.get("amount")
    category = data.get("category")
    description = data.get("description")

    expense = logic.add_expense(amount,category, description)
    return jsonify(expense), 201

@app.route("/expenses", methods=["GET"])
def get_expenses():
    return jsonify(logic.get_expense())

@app.route("/expenses/summary", methods=["GET"])
def summary():
    return jsonify(logic.get_summary())

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()
        description = data.get("description")

        if not description:
            return jsonify({"error": "Description required"}), 400

        category = model.predict_category(description)

        return jsonify({
            "predicted_category": category
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__=="__main__":
    app.run(debug=True)
    print(app.url_map)