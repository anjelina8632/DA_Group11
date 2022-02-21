import requests

url = 'https://brickset.com/sets/year-2020'
r = requests.get(url)

print(r.text)

print("Source Code:")
print("\t*", r.status_code)

h = requests.head(url)
print("Header")
print("**********")

for x in h.headers:
    print("\t", x, ".", h.headers[x])
print("**********")


header = {
    'User-Agent' : 'Mobile'
}

url2 = 'https://httpbin.org/headers'

rh = requests.get(url2, headers=header)

print(rh.text)   
