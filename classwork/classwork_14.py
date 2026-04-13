import requests
from pprint import pprint

url = 'https://dummyjson.com/posts'
response = requests.get(url=url)
# print(response.content)
# print(response.text)
pprint(response.json(), indent=4)

# print('dfgvbhjfd\nkvgdfhgvjhfdh\nkerhgjfr')
# print('"mbhg"')
