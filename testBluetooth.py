import subprocess

all_devices = subprocess.check_output("sudo bluetoothctl")
print(all_devices)