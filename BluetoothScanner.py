

"""import bluetooth

nearby_devices = bluetooth.discover_devices(lookup_names=True)
print("found %d devices" % len(nearby_devices))

for addr, name in nearby_devices:
    print("  %s - %s" % (addr, name))"""

import bluetooth

nearby_devices = bluetooth.discover_device(lookup_names=True)
while nearby_devices is None:
    nearby_devices

print("found %d devices" % len(nearby_devices))
for addr, name in nearby_devices:
    print("  %s - %s" % (addr, name))