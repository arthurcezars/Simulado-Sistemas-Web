from flask import Flask, render_template
import requests

#https://meme-api.herokuapp.com/gimme

app = Flask(__name__)

@app.route("/")
def index():
    url = "https://meme-api.herokuapp.com/gimme"
    lista_memes = []
    for i in range(9):
        meme = requests.get(url)
        lista_memes.append(meme.json())
    return render_template("index.html", dados=lista_memes)

if __name__ == "__main__":
    app.run()