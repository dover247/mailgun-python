import requests


class Templates(object):

    
    def __init__(self, baseurl, creds):

        self.baseurl = baseurl
        self.creds = creds

    def list(self, domain):
        return requests.get(self.baseurl + 'v3/' + domain + '/templates', auth=self.creds)

    def template(self, domain, template_name):
        return requests.get(self.baseurl + 'v3/' + domain + '/templates/' + template_name, auth=self.creds)

    def versions(self, domain, template_name):
        return requests.get(self.baseurl + 'v3/' + domain + '/templates/' + template_name + '/versions', auth=self.creds)

    def version(self, domain, template_name, tag):
        return requests.get(self.baseurl + 'v3/' + domain + '/templates/' + template_name + '/versions/' + tag, auth=self.creds)
