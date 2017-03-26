import requests, json
from sys import argv

script, name = argv

url = 'https://api.github.com/users/' + name + '/events/public'
r = requests.get(url)

raw_data = r.json()
if not raw_data:
    print("Not a valid user name")
    exit(0)
flag = 0
for data in raw_data:
    if data['type'] == 'PushEvent':
        email = data['payload']['commits'][0]['author']['email']
        flag = 1

if flag == 0:
    print("Unable to retrieve mail ID")
else:
    print("The email ID is : " + email)


