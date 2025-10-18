from flask import Flask, jsonify, url_for, redirect
import requests
from datetime import datetime, timezone
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.config["JSON_SORT_KEYS"] = False

CAT_API = "https://catfact.ninja/fact"

@app.route("/")
def home():
    return redirect(url_for("get_my_profile"))

@app.route("/me", methods=["GET"])
def get_my_profile():
    """"
    Returns my profile details and a random cat fact
    """
    try:
        response = requests.get(url=CAT_API, timeout=5)
        response.raise_for_status()
        cat_fact = response.json().get("fact", "No facts returned")

    except requests.RequestException:
        cat_fact = "Could not fetch cat fact at the moment. Try again later."

    my_data = {
        "status": "success",
        "user": {
            "email": os.environ["USER_EMAIL"],
            "name": os.environ["USER_NAME"],
            "stack":os.environ["USER_STACK"]
        },
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "fact": cat_fact
    }

    return  jsonify(my_data), 200
print("✅ Flask app loaded successfully")

if __name__ == "__main__":
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)


