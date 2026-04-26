from flask import Flask, jsonify, render_template, request, redirect, url_for
import json
from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# MongoDB connection
client = MongoClient(os.getenv("MONGO_URI"))
db = client["assignment_db"]
collection = db["users"]

# API route
@app.route('/api', methods=['GET'])
def get_data():
    with open('data.json') as f:
        data = json.load(f)
    return jsonify(data)

# Form page
@app.route('/')
def form():
    return render_template('form.html')

# Submit form
@app.route('/submit', methods=['POST'])
def submit():
    try:
        name = request.form['name']
        email = request.form['email']

        collection.insert_one({
            "name": name,
            "email": email
        })

        return redirect(url_for('success'))

    except Exception as e:
        return render_template('form.html', error=str(e))

# Success page
@app.route('/success')
def success():
    return render_template('success.html')

@app.route('/submittodoitem', methods=['POST'])
def submit_todo():
    item_name = request.form['itemName']
    item_desc = request.form['itemDescription']

    collection.insert_one({
        "itemName": item_name,
        "itemDescription": item_desc
    })

    return "Item stored successfully"

if __name__ == '__main__':
    app.run(debug=True)