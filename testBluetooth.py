import subprocess

proc = subprocess.Popen("ls", stdout=subprocess.PIPE)
output = proc.stdout.read()
print output