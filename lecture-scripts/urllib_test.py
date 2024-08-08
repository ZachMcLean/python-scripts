import urllib.request


with urllib.request.urlopen('https://www.omfgdogs.com') as response:
    data = response.read()
    for bytes_line in data.decode("utf-8").split('\n'):
        print(bytes_line)