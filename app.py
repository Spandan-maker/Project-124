from flask import Flask, jsonify, request

app = Flask(__name__)

contacts = [
    {
        'contact': 12345678,
        'name': 'subject 1',
        'id': 1, 
        'done': False
    },
    {
        'contact': 11234567,
        'name': 'subject 1',
        'id': 1, 
        'done': False
    }
]

@app.route("/add-data", methods = ["POST"])

def add_task():
    if not request.json:
        return jsonify({
            "status": "Error",
            "message": "Please provide data"
        }, 400)
    
    contact = [{
        "id": contacts[-1]["id"] + 1,
        "name": request.json["Name"],
        "contact": request.json.get("Contact", ""),
        "done": False
    }]

    contacts.append(contact)
    return jsonify({
        "status":"success",
        "message": "Task added succesfully!"
    })

@app.route("/get-data")
def get_task():
    return jsonify({
        "data" : contacts
    }) 

if( __name__ == "__main__"):
    app.run()