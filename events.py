import requests

class Events(object):

    def __init__(self, baseurl, creds):
        self.baseurl = baseurl
        self.creds = creds

    def list(self, domain):
        return requests.get(self.baseurl + 'v3/' + domain + '/events', auth=self.creds)