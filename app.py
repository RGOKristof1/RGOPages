from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route("/save", methods=["POST"])
def save_text():
    data = request.get_json()
    text = data.get("text", "")
    
    with open("mentett_szoveg.txt", "a", encoding="utf-8") as f:
        f.write(text + "\n")

    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(debug=True)
