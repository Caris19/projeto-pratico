from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/contatos')
def contatos():
    return render_template('contatos.html')

@app.route('/curriculo')
def curriculo():
    return render_template('curriculo.html')
    
