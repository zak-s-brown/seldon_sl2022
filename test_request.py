import base64
import requests
import sys


test_name = sys.argv[1]

if test_name in ('ner','all'):

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

if test_name in ('sentiment','all'):
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

if test_name in ('rpunct','all'):
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

if test_name in ('complex','all'):
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
