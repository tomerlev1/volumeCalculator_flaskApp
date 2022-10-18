from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap



app = Flask(__name__)
Bootstrap(app)

@app.route('/')

def home():
  return render_template('index.html')

@app.route('/', methods = ['POST'])

def home_post():
  dim1 = request.form['first_dim']
  dim2 = request.form['second_dim']
  dim3 = request.form['third_dim']
  volume = float(dim1) * float(dim2) * float(dim3)
  return render_template('index.html', output=volume, First_value=dim1, Second_value=dim2, Third_value=dim3)

app.run(host="0.0.0.0")