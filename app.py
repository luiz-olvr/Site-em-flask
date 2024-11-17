from flask import Flask

app = Flask(__name__)

@app.route('/<nome>')
def hello(nome):
    return " <h1> Olá {}</h1>".format(nome)

if __name__ == '__main__':
    app.run(debug=True)