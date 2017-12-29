import os
import requests

SYNBIOHUB_URL = "http://localhost:8888"
AUTH_CREDENTIALS = {"email": "zach.zundel@utah.edu", "password": "1187277"}
HEADERS = {"Accept": "text/plain"}

auth_response = requests.post(SYNBIOHUB_URL + "/login", data=AUTH_CREDENTIALS, headers=HEADERS)
auth_token = auth_response.text

HEADERS["X-authorization"] = auth_token

os.chdir('archives')
for archive in range(980):
    filename = '{0:05d}'.format(archive + 1) + ".omex"

    try:
        files = {"file": (filename, open(filename, 'rb'))}
    except FileNotFoundError:
        continue

    data = {
            "id": "test" + str(archive),
            "version": "1",
            "name": filename,
            "description": "Test upload of: " + filename,
            "citations": "",
            "collectionChoices": "",
            "overwrite_merge": "0",
            "user": "zach"
            }

    result = requests.post(SYNBIOHUB_URL + "/submit", files=files, data=data, headers=HEADERS)
    print(result.text + " " + filename)
