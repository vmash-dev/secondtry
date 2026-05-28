import requests
from pprint import pprint

url = 'https://script.google.com/macros/s/AKfycbxNZCMuHYq7SWSEFksNVxJMzgU3_vT-rkWs5LYRmKYshYyvBGbLMgynr7SMPJrZFLmI/exec'
response = requests.get(url=url, params={})
response_json = response.json()

#pprint(response_json)

zoo = response_json['zoo']

total_care_cost = 0
african_animals_count = 0
for animal in zoo:
    if animal["is_venomous"]:
        total_care_cost += animal["care_cost"] * animal["count"]
    if animal["count"] == "Африка":
        african_animals_count += 1
print(f'Вартість догляду за отруйними тваринами: {total_care_cost}, скільки африканських тварин наразі в зоопарку: {african_animals_count}')