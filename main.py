from flask import Flask,request
from flask_restful import Api,Resource,reqparse


app = Flask(__name__)


messages = [{
        "name": "A",
        "text": "Hi",
    }]


@app.route("/api/messages/", methods = ["GET"])
def get():
    return messages

@app.route("/api/message/", methods = ["POST"])
def post():
    data = {
        "name": request.json["name"],
        "text": request.json["text"],
        }
    messages.append(data)
    return "сообщение добавлена"

if __name__ == '__main__':
    app.run()
