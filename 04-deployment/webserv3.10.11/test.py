import requests
# from predict import prepare_features
# from predict import predict

ride = {
    "PULocationID": 10, 
    "DOLocationID": 50,
    "trip_distance": 40
}

url = 'http://localhost:9696/predict'
response = requests.post(url, json=ride)
print(response.json())



# features = prepare_features(ride)
# pred = predict(ride)
# print(pred)
