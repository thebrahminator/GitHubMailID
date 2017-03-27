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
email1 = []
email = "filler"
for data in raw_data:
    if data['actor']['login'] != name:
        print("It's an organisation's name")
        exit(0)

    if "org" in data.keys():
        if data['type'] == 'PushEvent':
            for commit in data['payload']['commits']:
               email1.append(commit['author']['email'])
               flag = 1

    if "org" not in data.keys():
        if data['type'] == 'PushEvent':
            email = data['payload']['commits'][0]['author']['email']
            flag = 1

if flag == 0:
    print("Unable to retrieve Mail ID")
else:
    if email != "filler":
        print("The email ID is : " + email)

    else:
        print("Conflicting mail IDs, the list of mail IDs are\n")
        for mail in email1:
            print(mail)

