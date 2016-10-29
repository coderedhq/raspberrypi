# Calls the find_devices function and returns an array of devices found through bluetooth
while True:
    devices = open("devices.txt", "w")
    found = set(UART.find_devices())
    # Check for new devices that haven't been seen yet and print out
    # their name and ID (MAC address on Linux, GUID on OSX).
    for device in found:
        devices.write('Found UART: {0} [{1}]'.format(device.name, device.id))
    devices.close()