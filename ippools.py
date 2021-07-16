import requests

class Ippools(object):

    def __init__(self, baseurl, creds):
        self.baseurl = baseurl
        self.creds = creds

    def pool(self):
        return requests.get(self.baseurl + 'v1/ip_pools', auth=self.creds)
        