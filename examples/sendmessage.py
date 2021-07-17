#!/usr/bin/python3

from mailgun import messages

creds = ('api', 'supersecretkey')
baseurl = 'https://api.mailgun.net/'
domain = 'test.com'

message = messages.Messages(baseurl, creds)

message.To = 'test@example.com'
message.From = 'Foo Bar <foobar@test.com>'
message.Subject = 'Foo Test!'
message.Attachments = ['testfile.txt', 'testfile2.txt']
message.Text = '''

Hello,

Just a reminder that all employees must read the "Rules Of Engagement" by EOD today.

Best,
Foo Bar

'''

print(message.send().json())