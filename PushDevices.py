from firebase import firebase

fi = firebase.FirebaseApplication('https://hacktathon.firebaseio.com', None)
devices = {}
i = 0
with open('sample.txt') as f:
    lines = f.readlines()
    devices[i] = lines
    i = i + 1
    max = i
# push list to firebase
for j in range(0, max):
    print(devices[j])
    j = j+1

fi.post('/devices', devices)
