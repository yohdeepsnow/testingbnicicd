import requests
import os
from datetime import datetime

print ("hello world!")
print ("testing ah nambahin baris")
print ("mau print apa nih")

res = requests.get("https://www.google.com")

a=datetime.now()

with open("tempResponse/"+str(a)+".txt","w") as f:
	f.write(res.text)
