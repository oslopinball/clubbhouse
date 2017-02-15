#!/usr/bin/python3

# OEM RFID Keyboard Emulator

import sys
from evdev import InputDevice, list_devices, ecodes, categorize

if __name__ == "__main__":
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
