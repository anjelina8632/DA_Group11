# Making a request to a web browser
import requests

url = 'https://brickset.com/sets/year-2020'
r = requests.get(url)

# Getting the full page of the web browser/site
print(r.text)

# Getting status code > * 200 - which means OK
print("Source Code:")
print("\t*", r.status_code)

# Header response from the web server
h = requests.head(url)
print("Header")
print("**********")

for x in h.headers:
    print("\t", x, ".", h.headers[x])
print("**********")

# Modifying the header's user agent
header = {
    'User-Agent' : 'Mobile'
}

url2 = 'https://httpbin.org/headers'

rh = requests.get(url2, headers=header)

print(rh.text)   
