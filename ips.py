import requests

class Ips(object):

    def __init__(self, baseurl, creds):
        self.baseurl = baseurl
        self.creds = creds

    def list(self):
        return requests.get(self.baseurl + 'v3/ips', auth=self.creds)

    def ip(self, ip):
        return requests.get(self.baseurl + 'v3/ips/' + ip, auth=self.creds)
    
    def domainip(self, domain):
        return requests.get(self.baseurl + 'v3/domains/' + domain + '/ips', auth=self.creds)

    