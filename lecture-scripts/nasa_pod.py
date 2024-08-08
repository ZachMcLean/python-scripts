import urllib.request
import json

def download_nasa_pod():
    api_key = "xXwaK6iLWM7agDtiaWnMtG9iEG50XR7InHm83m37"
    apod_url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"

    
    with urllib.request.urlopen(apod_url) as response:
        apod_data = json.load(response)
        image_url = apod_data["hdurl"]
        urllib.request.urlretrieve(image_url, f'today.jpg')
        print("SUCCESS")
    
    
if __name__ == "__main__":
    download_nasa_pod()


