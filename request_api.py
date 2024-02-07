import json
import requests
import sys

if len(sys.argv) != 2:
    sys.exit()

# response =  requests.get("https://itunes.apple.com/search?entity=song&limit=10&term=" + sys.argv[1])
    
response =  requests.get("https://api.spotify.com/v1/tracks=" + sys.argv[1])


print(json.dumps(response.json(), indent=2))

# song = response.json()

# for trackname in song["results"]:
#     print(trackname["trackName"])