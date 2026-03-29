from flask import Flask, jsonify, request, render_template
from pymongo import MongoClient
import certifi

app = Flask(__name__)

client = MongoClient(
    "mongodb+srv://shashank:admin@todo-python.s5dnq3k.mongodb.net/todo_db",
    tlsCAFile=certifi.where()
)

db = client["todo_db"]
collection = db["items"]

# Clean index
try:
    collection.delete_many({"itemUUID": None})
    collection.create_index("itemUUID", unique=True)
except Exception as e:
    print("Index issue:", e)


@app.route('/')
def home():
    return render_template('index.html')


# CREATE
@app.route('/submittodoitem', methods=['POST'])
def submit():
    data = request.json

    item_uuid = data.get("itemUUID")
    item_name = data.get("itemName")
    item_desc = data.get("itemDescription")

    if not item_uuid or not item_name or not item_desc:
        return {"error": "Missing fields"}, 400

    collection.insert_one({
        "itemUUID": item_uuid,
        "itemName": item_name,
        "itemDescription": item_desc
    })

    return {"message": "Item added"}


# READ
@app.route('/gettodoitems')
def get_items():
    items = list(collection.find({}, {"_id": 0}))
    return {"data": items}


# DELETE
@app.route('/deleteItem', methods=['POST'])
def delete_item():
    data = request.json
    collection.delete_one({"itemUUID": data.get("itemUUID")})
    return {"message": "Deleted"}


# EDIT
@app.route('/editItem', methods=['POST'])
def edit_item():
    data = request.json

    collection.update_one(
        {"itemUUID": data.get("itemUUID")},
        {"$set": {
            "itemName": data.get("itemName"),
            "itemDescription": data.get("itemDescription")
        }}
    )

    return {"message": "Updated"}


if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)