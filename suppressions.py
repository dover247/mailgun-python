import requests

class Suppressions(object):
    
    def __init__(self, baseurl, creds):
        self.baseurl = baseurl
        self.creds = creds

    def bounces(self, domain, limit):
        return requests.get(self.baseurl + 'v3/' + domain + '/bounces', params={'limit': limit}, auth=self.creds)

    def bounce(self, domain, address):
        return requests.get(self.baseurl + 'v3/' + domain + '/bounces/' + address, auth=self.creds)

    def unsubscribes(self, domain, limit):
        return requests.get(self.baseurl + 'v3/' + domain + '/unsubscribes', params={'limit': limit}, auth=self.creds)

    def unsubscribe(self, domain, address):
        return requests.get(self.baseurl + 'v3/' + domain + '/unsubscribes/', + address, auth=self.creds)

    def complaints(self, domain):
        return requests.get(self.baseurl + 'v3/' + domain + '/complaints', auth=self.creds)

    def complaint(self, domain, address):
        return requests.get(self.baseurl + 'v3/' + domain + '/complaints/', + address, auth=self.creds)

    def whitelists(self, domain, limit):
        return requests.get(self.baseurl + 'v3/' + domain + '/whitelists', params={'limit': limit}, auth=self.creds)

    def whitelist(self, domain, addressordomain):
        return requests.get(self.baseurl + 'v3/' + domain + '/whitelists/' + addressordomain, auth=self.creds)  