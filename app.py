from flask import Flask


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/database')
def hello():
    return render_template('database.html')

@app.route('/ind/<individual>')
def individual(individual):
    return render_template('individual.html')

@app.route('/tools')
def tool():
    return render_template('tools.html')

@app.route('/help')
def help():
    return render_template('help.html')

if __name__ == "__main__":
    app.run()
