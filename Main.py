import json
import datetime
from PIL import Image
import fnmatch
import os

class MsgInfo():
    sender = ""
    id = 0
    text = ""
    datetime = 0
    attachment = []
    image = ""
    def __init__(self, sender, id, text, datetime, attachment):
        self.sender = sender
        self.id = id
        self.text = text
        self.datetime = datetime
        self.attachment = attachment
        self.image

if __name__ == '__main__':
    msg_list = []
    grasso_list =[]
    with open("message.json", "r") as read_file:
        data = json.load(read_file)
    for msg in data:
        msg_list.append(MsgInfo(msg["name"], msg["sender_id"], msg["text"], msg["created_at"], msg["attachments"]))

    for msg in msg_list:
        if (len(msg.attachment) > 0):
            if (msg.attachment[0].get("url")):
                file_text = str(msg.attachment[0]["url"]).split('.com/')
                search = file_text[1].split(".")
                if (len(search) > 2):
                     for file in os.listdir('gallery'):
                        if fnmatch.fnmatch(file, "*" + search[2] + "*"):
                            if (file.endswith(".png" or ".jpeg")):
                                msg.image = Image.open('gallery/' + file)
    lookup_str = ""
    while (lookup_str != "exit"):
        lookup_str = input("Text to Lookup :")
        if (lookup_str != "exit"):
            for msg in msg_list:
                if (msg.text is not None and lookup_str.lower() in msg.text.lower()):
                    print (msg.sender + '@ ' + datetime.datetime.fromtimestamp(msg.datetime).strftime('%Y-%m-%d %H:%M:%S') + ': ' \
                    + msg.text)
