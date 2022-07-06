import requests

print ("hello world!")
print ("testing ah nambahin baris")
print ("mau print apa nih")

res = requests.get("https://www.google.com")

print (res.text)
