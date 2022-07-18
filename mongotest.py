import pymongo
#creating connection with mongodb
client = pymongo.MongoClient("mongodb+srv://somalimishra:somali40@cluster0.3cndr.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)
#To push data into mongodb
d = {
    "name":"somali",
    "email" : "somalimishra@gmail.com",
    "surname" : "mishra"
}
d = {
    "name":"somali",
    "email" : "somalimishra@gmail.com",
    "surname" : "mishra"
}
d = {
    "name":"somali",
    "email" : "somalimishra@gmail.com",
    "surname" : "mishra"
}
db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)



