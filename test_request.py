import base64
import requests



response = requests.post(
    "http://localhost:8080/seldon/default/ner/api/v1.0/predictions",
    headers={"Content-Type": "application/json"},
    json={
        "data": {
            "ndarray": 
                [

                        "Hi, my name is Zachary Brown and I work at Balto Software"   
                ]
            
        }
    },
)
print(response.text)
