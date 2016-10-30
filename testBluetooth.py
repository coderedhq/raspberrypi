import subprocess as sp
p = sp.Popen(["bt-device", "--list"], stdin=sp.PIPE, stdout=sp.PIPE, close_fds=True)
(stdout, stdin) = (p.stdout, p.stdin)
data = stdout.readlines()