import urllib
# If you are using Python 3+, import urllib instead of urllib2

import json


data =  {

        "Inputs": {

                "input1":
                {
                    "ColumnNames": ["PassengerId", "Survived", "Pclass", "Name", "Sex", "Age", "SibSp", "Parch", "Ticket", "Fare", "Cabin", "Embarked"],
                    "Values": [ [ "0", "0", "0", "value", "value", "0", "0", "0", "value", "0", "value", "value" ], [ "0", "0", "0", "value", "value", "0", "0", "0", "value", "0", "value", "value" ], ]
                },        },
            "GlobalParameters": {
}
    }

body = str.encode(json.dumps(data))

url = 'https://ussouthcentral.services.azureml.net/workspaces/d18a0c4f9d5445d485580d68b846a784/services/106fc83811d847239ae0e3de95d3908c/execute?api-version=2.0&details=true'
api_key = 'abc123' # Replace this with the API key for the web service
headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

req = urllib2.Request(url, body, headers)

try:
    response = urllib2.urlopen(req)

    # If you are using Python 3+, replace urllib2 with urllib.request in the above code:
    # req = urllib.request.Request(url, body, headers)
    # response = urllib.request.urlopen(req)

    result = response.read()
    print(result)
except urllib2.HTTPError, error:
    print("The request failed with status code: " + str(error.code))

    # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
    print(error.info())

    print(json.loads(error.read()))