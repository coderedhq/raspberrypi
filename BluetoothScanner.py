from subprocess import Popen, PIPE, STDOUT
import time
import sys
import os

LOCK_FILE = 'bluetooth.lck'

# wait for bluetooth.lck to be released
while os.path.isfile(LOCK_FILE):
    time.sleep(1)
    
created_lck = False
try:
    # create lock file
    lck_file = open(LOCK_FILE, 'w')
    lck_file.write('scanner')
    lck_file.close()
    created_lck = True
    
    # Default Timeout
    TIMEOUT_SCAN = 60
    # If timeout passed in as argument, use it
    if len(sys.argv) >= 2:
        TIMEOUT_SCAN = int(sys.argv[1])

    # Start subprocess with stdout and stdin as Pipes
    p = Popen(['sudo bluetoothctl', 'f'], shell=True, stdout=PIPE, stdin=PIPE, stderr=STDOUT)    
    # Wait for bluetoothctl to initialize the controller
    time.sleep(5);
    # Start scanning
    print('Starting Scan...')
    p.stdin.write(b'scan on\n')
    # Wait for scan to capture devices
    time.sleep(TIMEOUT_SCAN)
    # Stop Scanning
    print('Scan done')
    p.stdin.write(b'scan off\n')
    p.stdout.flush()
    # Print out devices
    p.stdin.write(b'devices\n')
    # Grab the output from process
    bluetooth_output = p.communicate()[0]


    # Split output by lines
    bluetooth_list = bluetooth_output.decode().splitlines()
    # Create list of devices
    device_list = set()
    # Parse the output for lines that start with Device
    for line in bluetooth_list:
        if line.startswith('Device'):
            identifiers = line.split(' ')
            device_list.add('{0}|{1}'.format(identifiers[1], " ".join(identifiers[2:])))


    output = open('devices.list', 'w');
    # Print the devices to file
    for device in device_list:
        output.write("{0}\n".format(device))
    output.close()
except Exception:
    print('Errored Out')
finally:
    if created_lck:
        os.remove(LOCK_FILE)
