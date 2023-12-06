from flask import Flask, render_template, request
import requests


app = Flask(__name__)
url = "http://localhost:5005/webhooks/rest/webhook"


@app.route("/", methods=("GET", "POST"))
def hello():
    if request.method == "POST":
        payload = {
            "sender": "test_user",
            "message": request.form["user_chat"]
        }
        
        headers = {"content-type": "application/json"}
        r = requests.post(url, json=payload, headers=headers)
        print(r.json())
        return render_template("index.html", bot_chat=r.json()[0]["text"])
    else:
        return render_template("index.html")
        
app.run()