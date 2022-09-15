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

response = requests.post(
    "http://localhost:8080/seldon/default/sentiment/api/v1.0/predictions",
    headers={"Content-Type": "application/json"},
    json={
        "data": {
            "ndarray": 
                [

                        "I really hate how cloudy it is today"   
                ]
            
        }
    },
)
print(response.text)

response = requests.post(
    "http://localhost:8080/seldon/default/rpunct/api/v1.0/predictions",
    headers={"Content-Type": "application/json"},
    json={
        "data": {
            "ndarray": 
                [

                        "this is just some example text"   
                ]
            
        }
    },
)
print(response.text)



response = requests.post(
    "http://localhost:8080/seldon/default/serial-rpunct-ner/api/v1.0/predictions",
    headers={"Content-Type": "application/json"},
    json={
        "data": {
            "ndarray": 
                [

                        "hi my name is zak brown and I work at balto software"   
                ]
            
        }
    },
)
print(response.text)

response = requests.post(
    "http://localhost:8080/seldon/default/complex-rpunct-ner-sentiment/api/v1.0/predictions",
    headers={"Content-Type": "application/json"},
    json={
        "data": {
            "ndarray": 
                [

                        "hi my name is zak brown and I work at balto software"   
                ]
            
        }
    },
)
print(response.text)
