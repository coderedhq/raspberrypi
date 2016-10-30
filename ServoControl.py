import atexit
import os
import time
import sys

import Adafruit_BluefruitLE
from Adafruit_BluefruitLE.services import UART

# Get the BLE provider for the current platform.
ble = Adafruit_BluefruitLE.get_provider()

# Did I Create A lock file?
lock_file_created = False

# lock file name
LOCK_FILE = 'bluetooth.lck'


def grab_lock():
    while os.path.isfile(LOCK_FILE):
        time.sleep(1)
    lock_file = open(LOCK_FILE, 'w')
    lock_file.write('temp_reader')
    lock_file.close()
    lock_file_created = True


# Main function implements the program logic so it can run in a background
# thread.  Most platforms require the main thread to handle GUI events and other
# asyncronous events like BLE actions.  All of the threading logic is taken care
# of automatically though and you just need to provide a main function that uses
# the BLE provider.
def main():

    # Grab lock before doing anything
    grab_lock()

    # get the default adapter
    adapter = ble.get_default_adapter()
    # start the adapter
    adapter.power_on()

    # clear cached data
    ble.clear_cached_data()

    # disconnect previous connections
    UART.disconnect_devices()

    # start scanning
    adapter.start_scan()
    print("Started Scanning")

    # keep track of known_devices
    known_devices = set()
    while True:
        # get the devices found
        found = set(UART.find_devices())
        # get difference between current and known
        new = found - known_devices
        # add new to known devices
        known_devices.update(new)
        # for each new device
        for device in new:
            print("Found {0} - {1}".format(device.name, device.id))
            # check if the id is the adafruit
            if device.id == "DE:85:BD:07:6F:29":
                # if it matches stop scanning
                adapter.stop_scan()
                # connect to the device
                device.connect()
                # check if it has UART capabilities
                UART.discover(device)
                # initialize uart object to talk to the device
                uart = UART(device)
                # send the servo command
                if sys.argv[1] == 'open':
                    # if response received
                    uart.write('cmd:open')
                if sys.argv[1] == 'close':
                    # if response received
                    uart.write('cmd:close')
                # read response
                received = uart.read(timeout_sec=60)
                if received is not None:
                    # print response
                    print('Received: {0}'.format(received))
                # disconnect from device
                UART.disconnect_devices()
                # device.disconnect()
                # power down adpater
                adapter.power_off()
                # remove lock file
                os.remove(LOCK_FILE)
                # sleep
                time.sleep(60)
                return


# Initialize the BLE system.  MUST be called before other BLE calls!
ble.initialize()

# Start the mainloop to process BLE events, and run the provided function in
# a background thread.  When the provided main function stops running, returns
# an integer status code, or throws an error the program will exit.
ble.run_mainloop_with(main)
