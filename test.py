import itchat, time
import requests
from itchat.content import *

KEY = 'eb720a8970964f3f855d863d24406576'

def get_response(msg):
    apiUrl = 'http://www.tuling123.com/openapi/api'
    data = {
        'key': KEY,
        'info': msg,
        'userid': 'wechat-robot',
    }
    try:
        r = requests.post(apiUrl, data=data).json()
        return r.get('text')
    except:
        return
@itchat.msg_register([TEXT, CARD, NOTE, SHARING])
def tuling_reply(msg):
    defaultReply = 'I received: ' + msg.text
    reply = get_response(msg.text)
    return reply or defaultReply

@itchat.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO])
def download_file(msg):
    msg.download(msg.fileName)
    typeSymbol = {
        PICTURE: 'img',
        VIDEO: 'vid', }.get(msg.type, 'fil')
    return '@%s@%s' % (typeSymbol, msg.fileName)

itchat.auto_login(hotReload=True)
itchat.run()
time.sleep(30)
itchat.logout()