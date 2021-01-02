import requests
import json
url='https://api.telegram.org/bot1485507202:AAGc12kAKtT9glWnuGwixRZn4z6SS5i6yGc/'
def get_all_updates():
    global url
    response=requsts.get(url+'getUpdates')
    return response.json()
def last_update(data) :
    result=data['result']
    last_index_number=len(result)-1
    return result[last_index_number]
def get_chat_id(update):
    return update['message']['chat']['id']
def send_message(chat_id,text) :
    global url
    send_data={'chat_id':chat_id , 'text':text}
    response=requests.post(url+'sendMessage',send_data)
if __name__=='__main__':
    data=get_all_updates()
    last=last_update(data)
    chat_id=get_chat_id(last)
    send_message(chat_id,'Hello')
    print()