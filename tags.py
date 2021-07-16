import requests


class Tags(object):

    def __init__(self, baseurl, creds):
        self.baseurl = baseurl
        self.creds = creds

    def list(self, domain):
        return requests.get(self.baseurl + 'v3/' + domain + '/tags', auth=self.creds)

    def tag(self, domain, tag):
        return requests.get(self.baseurl + 'v3/' + domain + '/tags/' + tag, auth=self.creds)

    def tagstats(self, domain, tag, eventType):
        return requests.get(self.baseurl + 'v3/' + domain + '/tags/' + tag + '/stats', params={'event': eventType}, auth=self.creds)

    def tagstatscountries(self, domain, tag):
         return requests.get(self.baseurl + 'v3/' + domain + '/tags/' + tag + '/stats/aggregates/countries', auth=self.creds)

    def tagstatsproviders(self, domain, tag):
         return requests.get(self.baseurl + 'v3/' + domain + '/tags/' + tag + '/stats/aggregates/providers', auth=self.creds)

    def tagstatsdevices(self, domain, tag):
         return requests.get(self.baseurl + 'v3/' + domain + '/tags/' + tag + '/stats/aggregates/devices', auth=self.creds)
