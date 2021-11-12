import os

cmd = "netstat -an"

os.system(cmd)

print("=" * 60)

with os.popen(cmd) as netstat_in:
    for raw_line in netstat_in:
        if "LISTEN" in raw_line:
            line = raw_line.rstrip()
            proto, local, remote, status = line.split()
            ip, port, *_ = local.split(':')
            if len(_) == 0:
                print(proto, port)
print()