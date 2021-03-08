from flask import Flask
import json
import requests

app = Flask(__name__)
url = "https://ws.api.video/auth/api-key"

headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}

d = {
    "apiKey": 'ZdSBGXrlXi5FrJYoYlg0uSAe7q4L8LpQC3mSRrwDtBF'
}

@app.route('/')
def hello_world():
   r = requests.post(url, data=json.dumps(d), headers=headers)
   return json.loads(r.text)['access_token']

