import json
import urllib.request

url ="https://api.themoviedb.org/3/movie/76341?api_key=12c7c295d57b002fe41d9a1d82e7a0f9"

resposta = urllib.request.urlopen(url)
dados = resposta.read()
json_data = json.loads(dados)
print(json_data)