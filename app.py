#Farfalloni

from flask import Flask, render_template, url_for, redirect


app = Flask(__name__)


@app.route('/index.html')
def index():
    return render_template('index.html')
  
@app.route('/database.html')
def database():
    return render_template('database.html')

@app.route('/search.html')
def search():
    return render_template('search.html')

@app.route('/results/<query>')
def results(query):
    return render_template('results.html')

@app.route('/ind/<individual>')
def individual(individual):
    return render_template('individual.html')

@app.route('/tools.html')
def tools():
    return render_template('tools.html')

@app.route('/help.html')
def help():
    return render_template('help.html')

if __name__ == "__main__":
    app.run()
