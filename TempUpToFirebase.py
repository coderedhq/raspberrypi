from firebase import firebase
import json

# Reads the temperature value from the text file and stores it in value
temp = open("Temperature.txt", "r")
value = temp.read()
#print (value)

# Creates a firebase and adds the temperature value to the firebase database
f = firebase.FirebaseApplication('https://test-dc035.firebaseio.com/')
result = f.post("/temperature", value)
#print result

