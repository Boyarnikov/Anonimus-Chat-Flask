from flask import Flask, render_template, request
from typing import List
import random
import string

app = Flask(__name__)


class Message:
    username = ""
    text = ""
    id = 0
    global_count = 0

    def __init__(self, username, text):
        self.text = text
        self.username = username
        self.id = self.global_count
        Message.global_count += 1

    def to_dict(self):
        return {
            "username": self.username,
            "text": self.text,
            "id": self.id
        }

    def __repr__(self):
        return str(self.to_dict())

    @classmethod
    def generate_random(cls):
        return Message(f"USER{random.randint(1, 1000)}",
                       " ".join(["".join(random.choices(string.ascii_letters, k=random.randint(1, 10))) for _ in
                                 range(random.randint(1, 30))]))


messages: List[Message] = [Message("USER1", "TEST"), Message("USER2", "TEST2")]
print(messages)


@app.route("/", methods=["GET"])
def get_chatroom():
    """Отправляет html и front script"""
    return render_template("chatroom.html")


@app.route("/post_message", methods=["POST"])
def post_message():
    pass


@app.route("/request_messages", methods=["FETCH"])
def request_messages():
    print(request.json)
    requested_messages = [m.to_dict() for m in messages if m.id > request.json['last_received_message_id']]

    if random.random() > 0.9:
        messages.append(Message.generate_random())
    return requested_messages
    """Вернуть все актуальные сообщения"""


if __name__ == "__main__":
    app.run(debug=True, port=5001)
