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
    #print(data.keys())
    if data['type'] == 'PushEvent':
        #print(data)
        email = data['payload']['commits'][0]['author']['email']
        flag = 1
#        print(data['payload']['commits'][0]['author']['email'])
#        print("NEXT")

if flag == 0:
    print("Unable to retrieve mail ID")
else:
    print("The email ID is : " + email)
#print()
#print(data[0]['payload']['commits'][0]['author'])
