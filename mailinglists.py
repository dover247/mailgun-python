import requests

class Mailinglists(object):

    def __init__(self, baseurl, creds):
        self.baseurl = baseurl
        self.creds = creds

    def list(self, limit):
        return requests.get(self.baseurl + 'v3/lists/pages', params={'limit': limit}, auth=self.creds)

    def mailinglist(self, address):
        return requests.get(self.baseurl + 'v3/lists/' + address, auth=self.creds)

    def members(self, address, limit):
        return requests.get(self.baseurl + 'v3/lists/' + address + '/members/pages', params={'limit': limit}, auth=self.creds)

    def member(self, address, member_address):
        return requests.get(self.baseurl + 'v3/lists/' + address + '/members/' + member_address, auth=self.creds)

    def jobs(self, address):
        return requests.get(self.baseurl + 'v3/lists/' + address + '/validate', auth=self.creds)