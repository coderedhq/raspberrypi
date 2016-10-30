from firebase import firebase
import sys
import os

firebase = firebase.FirebaseApplication('https://hacktathon.firebaseio.com', None)
ROOM_ID = 'abcdef'
with open('sampleList') as f:
    lines = f.readlines().splitlines()
    for line in lines:
        identifiers = lines.split('|')
        firebase.post('/rooms/{0}/devices/{1}/'.format(ROOM_ID, identifiers[0]), identifiers[1])

#