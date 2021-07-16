import requests


class Routes(object):
    

    def __init__(self, baseurl, creds):

        self.baseurl = baseurl
        self.creds = creds
        self.priority = None
        self.description = None
        self.expression = None
        self.action = None
    
    def list(self, limit):
        return requests.get(self.baseurl + 'v3/routes', params={'limit': limit}, auth=self.creds)

    def route(self, id):
        return requests.get(self.baseurl + 'v3/routes/' + id, auth=self.creds)
    
    def create(self):
        return requests.post(self.baseurl + 'v3/routes', data={'priority': self.priority,
                                                                'description': self.description,
                                                                'expression': self.expression,
                                                                'action': self.action}, auth=self.creds)
    def delete(self, routeid):
        return requests.delete(self.baseurl + 'v3/routes/' + routeid, auth=self.creds)

    def edit(self, routeid):
        return requests.put(self.baseurl + 'v3/routes/' + routeid, data={'priority': self.priority,
                                                                        'description': self.description,
                                                                        'expression': self.expression,
                                                                        'action': self.action}, auth=self.creds)                                                   