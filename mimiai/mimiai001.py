import requests


r = requests.get("http://www.mimis9.com/index.php")
print(len(r.text))