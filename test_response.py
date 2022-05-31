import json
import requests
name = "superman"
apiurl = "http://www.omdbapi.com/?apikey=3f968d6e&s="+name
result = json.loads(requests.get(apiurl).text)
data = result['Search']
print(data)
