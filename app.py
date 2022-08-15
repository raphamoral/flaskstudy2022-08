# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.

from flask import  Flask , render_template

app= Flask(__name__)

@app.route("/")
def principal():
    return render_template("index.html")






