from flask import Flask

app = Flask(__name__)

@app.route("/")
def welcome():
    return "Bem-vindo ao meu aplicativo Flask!"

if __name__ == "__main__":
    app.run(host='0.0.0.0')

    