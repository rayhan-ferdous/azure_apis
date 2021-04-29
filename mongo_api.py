from pymongo import MongoClient
from sys import argv as cmd

client = None

def connect(uri):
    """connects to db
    """
    global client
    client = MongoClient(uri)

def db_exists(name):
    """checks db existance
    """
    if name in client.list_database_names():
        return True
    return False

def add_db(name):
    """add new db
    """
    return client[name]

def add_collection(db_name, collection_name):
    """add collection to db
    """
    db = client[db_name]
    collection = db[collection_name]
    return collection

def insert(db_name, collection_name, docs):
    """insert multiple docs to collection
    """
    db = client[db_name]
    collection = db[collection_name]
    return collection.insert_many(docs)

def read_all(db_name, collection_name):
    """read all docs
    """
    db = client[db_name]
    collection = db[collection_name]
    return collection.find()


if __name__ == '__main__':
    #getting connectin uri as arg
    uri = cmd[1]
    connect(uri)

    print( db_exists('simple_db11') )

    print( add_db('api_db1') )

    print( add_collection('api_db1', 'collect111'))
    #sample docs
    docs = [
      { "name": "Amy", "address": "Apple st 652"},
      { "name": "Hannah", "address": "Mountain 21"},
      { "name": "Michael", "address": "Valley 345"},
      { "name": "Sandy", "address": "Ocean blvd 2"},
      { "name": "Betty", "address": "Green Grass 1"},
      { "name": "Richard", "address": "Sky st 331"},
      { "name": "Susan", "address": "One way 98"},
      { "name": "Vicky", "address": "Yellow Garden 2"},
      { "name": "Ben", "address": "Park Lane 38"},
      { "name": "William", "address": "Central st 954"},
      { "name": "Chuck", "address": "Main Road 989"},
      { "name": "Viola", "address": "Sideway 1633"}
    ]
    
    #add docs
    print( insert('api_db1', 'collect111', docs) )
     
    #read docs
    elems = read_all('api_db1', 'collect111')

    for e in elems:
        print(e)

