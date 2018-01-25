#RETROtransposon

#Import Classes:
from flask import Flask, render_template, g
import sqlite3 as sql

app = Flask(__name__)

@app.route('/index.html')
def index():
    return render_template('index.html')
  
@app.route('/database.html')
def database():
   con = sql.connect("final.db")
   con.row_factory = sql.Row
   
   cur = con.cursor()
   cur.execute("select * from ERV where repClass='LINE'")
   l1s = cur.fetchmany(20)
   cur.execute("select * from ERV where repClass='LTR'")
   ltrs = cur.fetchmany(20)
   
   return render_template("database.html",l1s = l1s,ltrs=ltrs)

@app.route('/search.html')
def search():
    return render_template('search.html')

@app.route('/results.html')
def results():
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
