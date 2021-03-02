# pip install pymongo
from pymongo import MongoClient
mongo = MongoClient('mongodb://localhost:27017/')

# create or use database in conection
db = mongo.DatabaseTester

# create or use collection in database
conection = db.Clients

# # insert a new record in json format
# conection.insert_one({"name":"Gudan"})

# # find a client with name
# conection.find()

# # insert multiple records in json format
# conection.insert_many([{"name":"Ronaldo"}, {"name":"Amaral"}])

# # update a record in json format
# conection.update_one({"name":"Ronaldo"}, {"$set":{"lastname":"de Souza"}})

# # deletes the first record found in the specifications
# conection.delete_one({'name': 'Gudan'})

# # json in python with multiple values
# json_clients = [{
#                  'name': 'William',
#                  'lastname': 'Prochnow',
#                  'age': 21,
#                  'office': 'Python Developer'
#                 },
#                 {
#                  'name': 'Luiz',
#                  'lastname': 'Silva',
#                  'age': 19,
#                  'office': 'Python Developer'
#                 }]

# # inserts the variable that contains the json
# conection.insert_many(json_clients)

# shows all records
for index in conection.find():
    print(index)
