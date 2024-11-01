from flask import Flask, render_template

app = Flask(__name__)

@app.get("/")
def index():
    return render_template("index.html")

@app.get("/menu/")
def menu():
    return render_template("menu.html")  

@app.get("/mocarella/")
def mocarella():
    return("mocarella.html")

@app.get("/cheez/")
def cheez():
    return("cheez.html")

@app.get("/karbonara/")
def karbonara():
    return("karbonara.html")

@app.get("/pizza and awocado/")
def pizza_and_awocado():
    return("pizza and awocado.html")

@app.get("/pizza pasta/")
def pizza_pasta():
    return("pizza pasta.html")

    return render_template("")

if __name__ == "__main__":
    app.run(debug=True)