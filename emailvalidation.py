import requests


class Emailvalidation(object):

    
    def __init__(self, baseurl, creds):

        self.baseurl = baseurl
        self.creds = creds

    def validate(self, address):
        return requests.get(self.baseurl + 'v4/address/validate', params={'address': address}, auth=self.creds)

    def jobs(self, limit):
        return requests.get(self.baseurl + 'v4/address/validate/bulk', params={'limit': limit}, auth=self.creds)

    def previews(self):
        return requests.get(self.baseurl + 'v4/address/validate/preview', auth=self.creds)

    def preview(self, preview_name):
        return requests.get(self.baseurl + 'v4/address/validate/preview/' + preview_name, auth=self.creds)
        