from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html', name='Isai Alejandro Flores', group='A')

if __name__ == '__main__':
    app.run(debug=True)

