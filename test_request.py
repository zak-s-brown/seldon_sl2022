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

                            "hi my name is zak brown and i work at balto software"   
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

                            "hi my name is zak brown and i work at balto software" 
                    ]
                
            }
        },
    )
    print(response.text)

if test_name in ('serial','all'):
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
