import urllib.request
import json

def download_nasa_pod():
    api_key = ""
    apod_url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"
    
    with urllib.request.urlopen(apod_url) as response:
        # take json and turn it into a dictionary!
        apod_data = json.load(response)
        for line in apod_data.split("\n"):
            print(line)

