import requests

# old version: 
# for w in ["rain", "nostalgia", "night", "love", "energetic"]:
   # r = requests.get(f"https://poetrydb.org/lines/{w}/title,author,linecount")
   # data = r.json()
   # print(w, "->", len(data) if isinstance(data, list) else data)

import requests

r = requests.get("https://poetrydb.org/lines,poemcount/rain;3/title,author,lines,linecount")
data = r.json()
print(data[0])