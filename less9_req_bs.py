
import urllib.request

opener=urllib.request.build_opener()
response=opener.open("https://www.marvel.com/")
print(response.read())


