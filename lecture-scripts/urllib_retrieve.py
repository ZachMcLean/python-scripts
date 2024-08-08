import urllib.request
import urllib.parse

urllib.request.urlretrieve("http://www.cs.mtsu.edu/~rwsmith/something.jpg", 'potato.jpg')

parsed = urllib.parse.urlparse("https://www.cs.mtsu.edu/~rwsmith/search?q=python&format=json")
print(parsed )

base_url = "https://www.cs.mtsu.edu"
relative_url = "/~rwsmith/"
joined = urllib.parse.urljoin(base_url, relative_url)
print(joined)
urllib.request.urlretrieve(joined, 'something.html')