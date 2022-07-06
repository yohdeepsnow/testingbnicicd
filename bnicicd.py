import requests
import os
import datetime

print ("hello world!")
print ("testing ah nambahin baris")
print ("mau print apa nih")

res = requests.get("https://www.google.com")

os.mkdir("tempResponse")

a=datetime.now()

with open(f"tempResponse/{a}.txt","w") as f:
	f.write(res.text)
