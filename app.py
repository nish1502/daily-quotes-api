from flask import Flask, jsonify, request
import random
import json

app = Flask(__name__)

with open("quotes.json") as f:
    quotes = json.load(f)

@app.route("/quote", methods=["GET"])
def get_quote():
    author = request.args.get("author")
    category = request.args.get("category")

    filtered = quotes
    if author:
        filtered = [q for q in quotes if q["author"].lower() == author.lower()]
    if category:
        filtered = [q for q in filtered if q["category"].lower() == category.lower()]

    if not filtered:
        return jsonify({"error": "No quotes found"}), 404

    return jsonify(random.choice(filtered))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050)

