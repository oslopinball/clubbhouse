#!/usr/bin/python3

# OEM RFID Keyboard Emulator

import sys
import json
import requests
from evdev import InputDevice, list_devices, ecodes, categorize
from member import Member
import config

keyMap = {
    'KEY_A': "A",
    'KEY_B': "B",
    'KEY_C': "C",
    'KEY_D': "D",
    'KEY_E': "E",
    'KEY_F': "F",
    'KEY_G': "G",
    'KEY_H': "H",
    'KEY_I': "I",
    'KEY_J': "J",
    'KEY_K': "K",
    'KEY_L': "L",
    'KEY_M': "M",
    'KEY_N': "N",
    'KEY_O': "O",
    'KEY_P': "P",
    'KEY_Q': "Q",
    'KEY_R': "R",
    'KEY_S': "S",
    'KEY_T': "T",
    'KEY_U': "U",
    'KEY_V': "V",
    'KEY_W': "W",
    'KEY_X': "X",
    'KEY_Y': "Y",
    'KEY_Z': "Z",
    'KEY_1': "1",
    'KEY_2': "2",
    'KEY_3': "3",
    'KEY_4': "4",
    'KEY_5': "5",
    'KEY_6': "6",
    'KEY_7': "7",
    'KEY_8': "8",
    'KEY_9': "9",
    'KEY_0': "0",
}

def parseKey(val):
    return keyMap[val] if val in keyMap else ""

def slack(member):
    slack_data = {'text': ":key: *" + member + "* har sjekket inn på klubben :door:"}

    response = requests.post(config.webhook_url, json=slack_data)

    if response.status_code != 200:
        raise ValueError(
            'Request to slack returned an error %s, the response is:\n%s'
            % (response.status_code, response.text)
        )
    elif response.status_code is 200:
        print("message posted")

if __name__ == "__main__":
    m = Member("opc.db")

    print("Finding RFID USB reader...")

    event_id = None
    devices = [InputDevice(fn) for fn in list_devices()]

    for device in devices:
        if "OEM RFID Keyboard Emulator" in device.name:
            event_id = device.fn
            print("Found: " + device.fn)
            break

    if event_id:
        device = InputDevice(event_id)
    else:
        print("ERROR: no reader found")
        sys.exit(1)

    print("Getting exclusive access to the device...")
    device.grab()

    id = ""

    print("Ready:")

    for event in device.read_loop():
        if event.type == ecodes.EV_KEY:
            e = categorize(event)
            if e.keystate == e.key_up:
                id += parseKey(e.keycode)
                #print(id)
            if len(id) is 14:
                #print(id)
                member = m.getID(id)
                if not member is "ERROR":
                    print(member)
                    slack(member)

                id = ""
                print("Ready:")

    device.ungrab()
