import requests

class Messages(object):
    
    def __init__(self, baseurl, creds):

        self.baseurl = baseurl
        self.creds = creds
        self.From = None
        self.To = None
        self.Cc = None
        self.Bcc
        self.Subject = None
        self.Text = None
        self.Html = None
        self.Attachment = None
        self.Dkim = None
        self.Tag = None
        self.DeliveryTime = None
        self.Attachments = []

    def send(self, domain):

        return requests.post(self.baseurl + 'v3/' + domain + '/messages', files=[('attachment', open(file, 'rb')) for file in self.Attachments], auth=self.creds, data={
                                                                                'from': self.From,
                                                                                'to': self.To,
                                                                                'cc': self.Cc,
                                                                                'bcc': self.Bcc,
                                                                                'subject': self.Subject,
                                                                                'text': self.Text,
                                                                                'html': self.Html,
                                                                                'o:dkim': self.Dkim,
                                                                                'o:tag': self.Tag,
                                                                                'o:deliverytime': self.DeliveryTime})