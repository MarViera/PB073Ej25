import requests
url = "https://swapi.py4e.com/"
r = requests.get(url)
i = 1
while r.status_code == 200:
    r = requests.get(url+"api/people/"+str(i))
    print(i)
    i += 1
#print(i)
