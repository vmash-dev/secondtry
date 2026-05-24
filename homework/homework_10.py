import requests
from pprint import pprint

params = {
    "skip": 0,
    "limit": 1000
}

url = "https://dummyjson.com/recipes"

response = requests.get(url=url, params=params)

response_json = response.json()
recipes = response_json["recipes"]
italian_cuisine = 0
max_caloriesPerServing = 0
recipes_that_prepared_at_temperature_190 = []
all_reviewCount = 0

for recipe in recipes:
    cuisine = recipe["cuisine"]
    #print(cuisine)
    if cuisine == "Italian":
        italian_cuisine += 1
        #print(italian_cuisine)
    caloriesPerServing = recipe["caloriesPerServing"]
    #print(caloriesPerServing)
    if caloriesPerServing > max_caloriesPerServing:
        max_caloriesPerServing = caloriesPerServing
        #print(caloriesPerServing)
    instructions = recipe["instructions"]
    instruction = instructions[0]
    if instruction.count("190°C"):
        recipes_that_prepared_at_temperature_190.append(recipe)
        #print(instruction)
    reviewCount = recipe["reviewCount"]
    if reviewCount > 0:
        all_reviewCount += reviewCount
        #print(all_reviewCount)

#pprint(recipes_that_prepared_at_temperature_190)