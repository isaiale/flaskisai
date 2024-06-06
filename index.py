from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
<<<<<<< HEAD
    return render_template('index.html', name='Isai Alejandro Flores', group='A')
=======
    return "Isai Alejandro Flores Grupo: A"
>>>>>>> 13cbb9b856cf3a42aef596a4c91cff63f4dfaf8a

if __name__ == '__main__':
    app.run(debug=True)
