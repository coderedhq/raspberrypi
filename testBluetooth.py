import subprocess

proc = subprocess.Popen("sudo bluetoothctl", stdout=subprocess.PIPE)
output = proc.stdout.read()
print output