#!/bin/python3
import requests
import time
from asterisk.agi import *


def get_ack(push_id):
    URL = "http://localhost:8000/push/check"
    PARAMS = {'id': push_id}
    r = requests.get(url=URL, params=PARAMS)
    return r.text


agi = AGI()

agi.verbose("push agi started")

extension = agi.env['agi_extension']
callerID = agi.env['agi_callerid']
URL = "http://localhost:8000/push/send"
PARAMS = {'to': extension, 'from': callerID}
r = requests.get(url=URL, params=PARAMS)
pushID = r.text

ack = False
i = 1
while not ack:
    str_ack = get_ack(pushID)
    if str_ack == "True":
        ack = True
    i = i + 1
    if i > 30:
        ack = True
    time.sleep(1)
time.sleep(4)
# Get variable in dialplan
# phone_exten = agi.get_variable('PHONE_EXTEN')

# Set variable, it will be available in dialplan
# agi.set_variable('EXT_CALLERID', '1')
