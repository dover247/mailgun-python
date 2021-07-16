import requests


class Webhooks(object):

    
    def __init__(self, baseurl, creds):
        self.baseurl = baseurl
        self.creds = creds

    def list(self, domain):
        return requests.get(self.baseurl + 'v3/domains/' + domain + '/webhooks', auth=self.creds)

    def webhook(self, domain, webhookname):
        return requests.get(self.baseurl + 'v3/domains/' + domain + '/webhooks/' + webhookname, auth=self.creds)