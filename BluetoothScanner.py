

"""import bluetooth

nearby_devices = bluetooth.discover_devices(lookup_names=True)
print("found %d devices" % len(nearby_devices))

for addr, name in nearby_devices:
    print("  %s - %s" % (addr, name))"""

import bluetooth

nearby_devices = bluetooth.discover_devices(lookup_names=True)
if len(nearby_devices) == 0:
    print("Nothing is there")

"""print("found %d devices" % len(nearby_devices))
for addr, name in nearby_devices:
    print("  %s - %s" % (addr, name))"""