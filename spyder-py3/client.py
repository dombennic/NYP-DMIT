import requests

        
url = 'http://127.0.0.1:5000/users'
myobj = {'weight': 160, 'texture' : 1}

x = requests.post(url, data = myobj)

print(x.text)
