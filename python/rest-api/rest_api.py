import json

class RestAPI(object):
    
    def __init__(self, database=None):
        self.database = database        #dictionary

    def get(self, url, payload=None):
        if payload == None:
            return json.dumps(self.database)    #dict to a string
        else:
            user = self.database['users'][0]['name'] == payload['users']
            json.dumps(user)

    def post(self, url, payload=None):
        user = json.loads(payload)  #string to a dictionary
        data = { 'name': user['user'], 'owes': {}, 'owed_by': {}, 'balance': 0 }
        self.database['users'].append(data)
        return json.dumps(data)

database = {'users': [{'name': 'Adam','owes': {},'owed_by': {},'balance': 0},
                    {'name': 'Bob','owes': {},'owed_by': {},'balance': 0}]}
api = RestAPI(database)
payload = json.dumps({'users': ['Bob']})
response = api.get('/users', payload)
print(api.get('/users'))
