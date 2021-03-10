from flask import Flask
import json
import mux_python


app = Flask(__name__)

MUX_TOKEN_ID='bbcb8911-562b-4b0a-bf4a-64de6bad9ffc'
MUX_TOKEN_SECRET='PGCkpvE5ZtZ/wwwKBC+YpJnGV5ibxycaIoEaDsOpyMJJmfEuFMFvXEsFLv7pD9SSU2cnfPdT6o4'

configuration = mux_python.Configuration()
configuration.username = MUX_TOKEN_ID
configuration.password = MUX_TOKEN_SECRET

uploads_api = mux_python.DirectUploadsApi(mux_python.ApiClient(configuration))


@app.route('/')
def hello_world():
   create_asset_request = mux_python.CreateAssetRequest(playback_policy=[mux_python.PlaybackPolicy.PUBLIC])
   create_upload_request = mux_python.CreateUploadRequest(timeout=3600, new_asset_settings=create_asset_request, cors_origin="*")
   create_upload_response = uploads_api.create_direct_upload(create_upload_request)  
   print(create_upload_response)
   d = {
    "url": create_upload_response.data.url,
    "id": create_upload_response.data.id
   }
   return json.dumps(d)
   