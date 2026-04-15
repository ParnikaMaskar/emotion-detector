import requests

def emotion_detector(text):
    url = "https://api.example.com/emotion"  # Watson endpoint
    response = requests.post(url, json={"text": text})
    return response.json()
