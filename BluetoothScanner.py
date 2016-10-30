

"""import bluetooth

nearby_devices = bluetooth.discover_devices(lookup_names=True)
print("found %d devices" % len(nearby_devices))

for addr, name in nearby_devices:
    print("  %s - %s" % (addr, name))"""

import bluetooth

nearby_devices = set()
while True:
    nearby_devices.update(bluetooth.discover_devices(lookup_names=True))
    print("found %d devices" % len(nearby_devices))
    for addr, name in nearby_devices:
        print("  %s - %s" % (addr, name))