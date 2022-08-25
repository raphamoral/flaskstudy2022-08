# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
import json
import urllib

from flask import Flask, render_template, request

app = Flask(__name__)
frutas = []
registros = []


@app.route("/", methods=["GET", "POST"])
def principal():
    nome = 'Raphael'
    idade = 31
    fruta1 = "Morango"
    fruta2 = "Uva"
    fruta3 = "Maça"
    fruta4 = "laranja"
    # frutas= ['papaia','limaaaao']
    if request.method == "POST":
        if request.form.get("frutasadd"):
            frutas.append(request.form.get("frutasadd"))

    return render_template("index.html", nome=nome, idade=idade, fruta1=fruta1, fruta2=fruta2, fruta3=fruta3,
                           fruta=fruta4, frutas=frutas)


@app.route("/sobre", methods=["POST", "GET"])
def sobre():
    # notas ={"fulano":5.0, "Beltrano":6.0, "Aluno": 7.0, "Sicrano":8.5}
    if request.method == "POST":
        if request.form.get("aluno") and request.form.get("nota"):
            registros.append({"aluno": request.form.get("aluno"), "nota": request.form.get("nota")})

    return render_template("sobre.html", registros=registros)


@app.route("/sob2")
def sobrw():
    return ("<h1> OLAAAAAAAAAAAAAAAAAAAA H1 do flask html<h1>")


@app.route("/filmes")
def filmes():
    url = "https://api.themoviedb.org/3/discover/movie?sort_by=popularity.desc&api_key=12c7c295d57b002fe41d9a1d82e7a0f9"

    resposta = urllib.request.urlopen(url)
    dados = resposta.read()
    json_data = json.loads(dados)
    print(dados)
    return render_template("filmes.html",filmes=json_data["results"])
