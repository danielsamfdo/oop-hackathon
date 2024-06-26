import requests
import json
import datetime

def send_to_ehr(text):
    url = "https://fumage-jamesleonard-oophackathon.canvasmedical.com/Task"

    headers = {
        "Authorization": "Bearer v8rGupHrkWCUUAGmBWzWsCiF9zNKlk",
        "accept": "application/json",
        "content-type": "application/json"
    }

    payload = {
        "resourceType": "Task",
        "status": "requested",
        "description": "Follow Up on Dan Doe MRI Results",
        "for": {"reference": "Patient/0aabd3daaafc4880932b917624defbfa"},
        "authoredOn": f"{datetime.datetime.now().isoformat()}Z",
        "requester": {"reference": "Practitioner/e6e90e416e0c422992aabb110fe8b1f1"},
        "owner": {"reference": "Practitioner/e766816672f34a5b866771c773e38f3c"},
        "intent": "unknown",
        "restriction": {"period": {"end": f"{datetime.datetime.now().isoformat()}Z"}},
        "note": [
            {
                "text": text,
                "time": f"{datetime.datetime.now().isoformat()}Z",
                "authorReference": {"reference": "Practitioner/e766816672f34a5b866771c773e38f3c"}
            }
        ],
        "input": [
            {
                "type": {"text": "label"},
                "valueString": "Urgent"
            }
        ]
    }

    response = requests.post(url, headers=headers, data=json.dumps(payload))

    return response.status_code, response.json()
