import requests

url = "https://httpbin.org/html"

response = requests.get(url)

print("Status Code:", response.status_code)
print(response.text)