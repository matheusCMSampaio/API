import requests

print('*-* Python Language *-*')

url = f'https://python.org'
response = requests.get(url)

print(response.status_code)

print(b'Python is a programming language' in response.content)

def get_data(url):
    response = requests.get(url)
    return response.json()