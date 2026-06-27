from flask import Flask, render_template, request
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient(
    "mongodb+srv://tirthvaidh2796_db_user:tirth%402796@cluster0.qhgqwov.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
)
db = client["studentdb"]
collection = db["students"]


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/submit", methods=["POST"])
def submit():

    name = request.form["name"]
    email = request.form["email"]

    data = {
        "name": name,
        "email": email
    }

    try:
        collection.insert_one(data)
        return render_template("success.html")
    except Exception as e:
        return f"Error : {e}"


if __name__ == "__main__":
    app.run(debug=True)