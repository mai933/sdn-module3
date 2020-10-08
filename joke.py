"""

Simple API call script that returns a Chuck Norris Joke!

"""

#import requests library
import requests

#Creates a globabl variable that defines our URL string

URL = "https://icanhazdadjoke.com/"

#Creates dictionary for the payload data and header information

payload = {}
header = {'Accept': 'application/json'}

#Creates variable response and stores the HTTP GET response using the requests
#library to make the API call and passing it the URL variable value, headers, and payload information

response = requests.get(URL, headers=header, data=payload)

#creates a variable labelled joke storing our response variable in JSON format
#and filters out just the value tied to the key "joke"

statusCode = response.status_code

joke = response.json()['joke']

print("Status Code is: " + str(statusCode))
print("Here is your Chuck Norris Joke: ")
print(joke)
