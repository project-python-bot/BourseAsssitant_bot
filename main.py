import requests
from flask import Flask
from flask import request
from flask import Response
import json
import os
url = "https://api.telegram.org/bot1485507202:AAGc12kAKtT9glWnuGwixRZn4z6SS5i6yGc/"
app = Flask(__name__)
def last_message():
    global url
    result = requests.get(url+'getUpdates')
    result = result.json()
    result = result['result']
    last_index = len(result)-1
    last_message = result[last_index]
    return last_message
def get_id(result):
    id = result['message']['chat']['id']
    return id
def get_message(result):
    message = result['message']['text']
    return message
def send_message(id,text):
    global url
    send_data = {'chat_id': id, 'text': text}
    response = requests.post(url + 'sendMessage', data = send_data)
    return response
@app.route('/webhook',methods = ['POST','GET'])
def index():
    result = last_message()
    id = get_id(result)
    text = get_message(result)
    if request.method == 'POST':
        if text == '/start':
            send_message(id,'سلام خوش آمدید!')
        return Response('ok',status=200)
    else:
        return '<h1>salam<h1>'
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=int(os.environ.get('PORT',5000)))
    #app.run(debug=True)
