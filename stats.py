import requests


class Stats(object):

    def __init__(self, baseurl, creds):
        self.baseurl = baseurl
        self.creds = creds
    
    def list(self, domain, eventType):
        return requests.get(self.baseurl + 'v3/' + domain + '/stats/total', auth=self.creds, params={'event': eventType})