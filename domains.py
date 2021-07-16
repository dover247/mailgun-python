import requests


class Domains(object):

    def __init__(self, baseurl, creds):
        self.baseurl = baseurl
        self.creds = creds

    def list(self):
        return requests.get(self.baseurl + 'v3/domains', auth=self.creds)

    def domain(self, domain):
        return requests.get(self.baseurl + 'v3/domains/' + domain, auth=self.creds)