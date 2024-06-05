from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Isai Alejandro Flores Grupo: A"

if __name__ == '__main__':
    app.run(debug=True)
