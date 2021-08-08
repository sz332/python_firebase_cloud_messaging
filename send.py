import http.client
import json

server_key = '<server key>';
client_token = '<token received by client>'; 

notification = {
	  'title': 'Hello world',
	  'body': 'This is a very long message',
	  'icon': 'firebase-logo.png',
	  'click_action': 'http://localhost:8081'
}

headers = {
    'Authorization': 'key=' + server_key,
    'Content-Type': 'application/json' 
}

body = {
    'notification': notification,
    'to': client_token 
}

conn = http.client.HTTPSConnection('fcm.googleapis.com')
conn.request('POST', '/fcm/send', json.dumps(body), headers)

response = conn.getresponse()

print(response.status, response.reason)
print(response.read().decode())
