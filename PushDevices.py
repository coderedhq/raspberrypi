from firebase import firebase
import sys
import os

firebase = firebase.FirebaseApplication('https://hacktathon.firebaseio.com', None)
devices = {}
ROOM_ID = 'abcdef'
i = 0
device_list = set()
with open('sampleList') as f:
    lines = f.readlines().splitlines()
    devices[i] = lines
    identifiers = lines.split('|')
    firebase.post('/rooms/{0}/devices/{1}/'.format(ROOM_ID, identifiers[0]), identifiers[1])
    i = i + 1
    max = i


