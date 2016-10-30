from firebase import firebase
import requests

# Reads the temperature value from the text file and stores it in value
temp = open("current.temp", "r")
value = temp.read()
#print (value)

# Creates a firebase and adds the temperature value to the firebase database
f = firebase.FirebaseApplication('https://hacktathon.firebaseio.com/')
r = requests.get("http://107.170.46.161:3000/api/pi/-KVHaD86FyfI1hIZ6mRV/abcdef")
result = f.put('houses/-KVHaD86FyfI1hIZ6mRV/rooms/abcdef', 'temp', value)
#print result

