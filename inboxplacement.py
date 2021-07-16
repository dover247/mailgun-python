import requests


class Inboxplacement(object):

    def __init__(self, baseurl, creds):

        self.baseurl = baseurl
        self.creds = creds

    def list(self):
        return requests.get(self.baseurl + 'v3/inbox/tests', auth=self.creds)

    def inboxplacement(self, test_id):
        return requests.get(self.baseurl + 'v3/inbox/tests/' + test_id, auth=self.creds)

    def counters(self, test_id):
        return requests.get(self.baseurl + 'v3/inbox/tests/' + test_id + '/counters', auth=self.creds)

    def checks(self, test_id):
        return requests.get(self.baseurl + 'v3/inbox/tests/' + test_id + '/checks', auth=self.creds)

    def check(self, test_id, seed_address):
        return requests.get(self.baseurl + '/v3/inbox/tests/' + test_id + '/checks/' + seed_address, auth=self.creds)