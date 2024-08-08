import urllib.request
import urllib.parse
# import json

# with urllib.request.urlopen('https://www.omfgdogs.com/') as response:
#     data = response.read()
#     for bytes_line in data.decode("utf-8").split("/n"):
#         line = bytes_line
#         print(line)

urllib.request.urlretrieve("https://www.cs.mtsu.edu/~rwsmith/", 'something.html')
parsed = urllib.parse.urlparse('https://www.cs.mtsu.edu/~rwsmith/search?q=python&format=json')
print(parsed)

base_url = "https://www.cs.mtsu.edu"
relative_url = "/~rwsmith/"
joined = urllib.parse.urljoin(base_url, relative_url)
print(joined)


