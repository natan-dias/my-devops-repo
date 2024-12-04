import requests
import json

BASE = "http://127.0.0.1:5000/"

# Small GET request

#response = requests.get(BASE + "users/user1")

#print(response.json())

#--------------------------------------------#

# Small Hello World
#responseHello = requests.get(BASE + "helloworld")
#responsePOST = requests.post(BASE + "helloworld")

#print(responseHello.json())
#print(responsePOST.json())

#--------------------------------------------#

# Small Video
headers = {"Content-Type": "application/json"}
data = [
    {"likes": 10, "name": "Video01", "views": 100},
    {"likes": 20, "name": "Video02", "views": 200},
    {"likes": 30, "name": "Video03", "views": 300}
    ]
for i in range(len(data)):

    #responseVideo = requests.put(BASE + "video/1", json.dumps({"likes": 10, "name": "Video01", "views": 100}), headers=headers)
    responseVideo = requests.put(BASE + "video/" + str(i+1), json.dumps(data[i]), headers=headers)
    print(responseVideo.json())

#input()
#responseVideo = requests.delete(BASE + "video/2")
#print(responseVideo)
input()
responseVideo = requests.get(BASE + "video/1")
print(responseVideo.json())
responseVideo = requests.get(BASE + "video/2")
print(responseVideo.json())
responseVideo = requests.patch(BASE + "video/2", json.dumps({"likes": 900}), headers=headers)
print(responseVideo.json())
responseVideo = requests.get(BASE + "video/2")
print(responseVideo.json())