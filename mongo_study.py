import os
from pymongo import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
from bson import ObjectId

load_dotenv()

MONGO_USERNAME = os.getenv('MONGO_USERNAME')
MONGO_PASSWORD = os.getenv('MONGO_PASSWORD')

uri = f"mongodb+srv://{MONGO_USERNAME}:{MONGO_PASSWORD}@myprogect.4ogd5bb.mongodb.net/?appName=myprogect"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# databases = client.list_databases()
# print(databases)
# for db in databases:
#     print(db)

# db_shop = client.shop
db_shop = client['outlet']

collection_books = db_shop.books
collection_phones = db_shop['phones']

# CREATE
# add one document
book = {'title': '10 negro', "price": 365, 'description': "English classic detective"}
collection_books.insert_one(book)

phone = {'title': 'iPhone 17', "price": 65000, 'description': "cool"}
# created_phone = collection_phones.insert_one(phone)
# print(created_phone)

# add many
phones = [
    {'title': 'iPhone 17', "price": 65000, 'description': "cool"},
    {'title': 'iPhone 16', "price": 65000, 'description': "cool"},
    {'title': 'iPhone 15', "price": 65000, 'description': "cool"},
    {'title': 'iPhone 14', "price": 65000, 'description': "cool", 'is_restored': True},
]
created_phones = collection_phones.insert_many(phones)
print(created_phones)


# READ
# first
first_phone = collection_phones.find_one()
print(first_phone)

query = {
    # '_id': ObjectId('6a21a9d65f7f195a50597ade'),
    'price': 65000
}
wanted_book = collection_phones.find_one(query)
print(wanted_book)

# find_many



# all_phones = collection_phones.find()

# AND QUERY
query = {'title': 'iPhone 17'}
query = {'price': 65111}
query = {'price': {"$gt": 65000}}
query = {'price': {"$gte": 65000}}
query = {'price': {"$gt": 65000, "$lt": 68000}}
query = {'price': {"$gte": 65000, "$lte": 68000}, 'title': 'iPhone 14'}

# OR QUERY
query = {
    '$or': [
        {'price': 65111},
        {'title': 'iPhone 14', 'is_restored': False}
    ]
}

# NOT QUERY
query = {
    'price':  {"$ne": 65111}
}

query = {
    'is_restored':  {"$ne": True}
}


# TEXT QUERY
query = {'title': 'iPhone 17 max'}
query = {'title': 'iPhone 17 Pro Max'}
query = {'title': {"$regex": "i*"}}  # * -> any sequence of letters
query = {'title': {"$regex": "I*", "$options": 'i'}}  # i -> any register
query = {'title': {"$regex": "i*max", "$options": 'i'}}
# query = {}



# all_phones = collection_phones.find(query).limit(5).skip(2)
# all_phones = collection_phones.find(query).sort('price', -1)
all_phones = collection_phones.find(query).limit(5).sort('price', -1).skip(2)
# print(list(all_phones))
print(all_phones)

for phone in all_phones:
    print(phone)


# # DELETE
# query = {'_id': ObjectId('6a21a9d65f7f195a50597ade')}
# updated_obj = collection_phones.delete_one(query)
# # updated_obj = collection_phones.delete_many(query)
# print(updated_obj)


# UPDATE
# # $set
# query = {'title': 'iPhone 17 max 123'}
# new_data = {'$set': {'price': 77777, 'weight': 250}}
# updated = collection_phones.update_many(query, new_data)
# print(updated)

# $unset
# query = {'title': 'iPhone 17 max 123'}
# new_data = {'$unset': {'weight': ""}}
# updated = collection_phones.update_many(query, new_data)
# print(updated)


# # $increase
# query = {'title': 'iPhone 17 max 123'}
# operation = {'$inc': {'price': 100}}
# updated = collection_phones.update_many(query, operation)
# print(updated)

# # multiplication
# query = {'title': 'iPhone 17 max 123'}
# operation = {'$mul': {'cost': 1.2}}
# updated = collection_phones.update_many(query, operation)
# print(updated)


# multiplication + increase + set
query = {'title': 'iPhone 17 max 123'}
operation = {'$mul': {'price': 0.9}, '$inc': {'cost': 30, 'warranty': -4}, '$set': {"discounted": True} }
updated = collection_phones.update_many(query, operation)
print(updated)