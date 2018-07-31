import json
import datetime

if __name__ == '__main__':
    with open("message.json", "r") as read_file:
        data = json.load(read_file)
    for msg in data:
        print(msg["text"])

class MsgInfo():
    sender = ""
    id = 0
    text = ""
    datetime = 0
    attachment = ""
    def __init__(self, sender, id, text, datetime, attachment):
        self.sender = sender
        self.id = id
        self.text = text
        self.datetime = datetime
        self.attachment = attachment