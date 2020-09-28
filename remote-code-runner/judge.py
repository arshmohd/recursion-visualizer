import os
import requests
import json 

API_KEY = os.environ.get('API_KEY')
 
def sendCodeToJudge(code): 
    print(code)
    print('________________________________________\n\n')
    url = "https://judge0.p.rapidapi.com/submissions"
    payload = { "language_id": 71, "source_code": code}
    headers = { 
        'x-rapidapi-host': "judge0.p.rapidapi.com",
        'x-rapidapi-key': API_KEY,
        'content-type': "application/json",
        'accept': "application/json"
    }
    response = requests.request("POST", url, data=json.dumps(payload), headers=headers)
    responseObj = json.loads(response.text)
    if 'error' in responseObj: 
        return 'error'
    token = responseObj['token']
    URL = "https://judge0.p.rapidapi.com/submissions/" + token
    HEADERS = {
        'x-rapidapi-host': "judge0.p.rapidapi.com",
        'x-rapidapi-key': API_KEY
    }
    subResponse = requests.request("GET", URL, headers=HEADERS)
    codeSubmissionResponse = json.loads(subResponse.text) 
    print(codeSubmissionResponse)
    output = codeSubmissionResponse['stdout']
    return output