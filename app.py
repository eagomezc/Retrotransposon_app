#RETROtransposon

#Import Classes:
from flask import Flask, render_template, request
import sqlite3 as sql

app = Flask(__name__)

con = sql.connect("final.db")
con.row_factory = sql.Row

@app.route('/index.html')
def index():
    return render_template('index.html')
  
@app.route('/database.html')
def database():
   cur = con.cursor()
   cur.execute("select * from ERV where repClass='LINE'")
   l1s = cur.fetchmany(20)
   cur.execute("select * from ERV where repClass='LTR'")
   ltrs = cur.fetchmany(20)
   return render_template("database.html",l1s = l1s,ltrs=ltrs)

@app.route('/individual.html-<ind>-<individual>')
def individual(ind,individual):
   t = (ind,individual)
   cur = con.cursor()
   cur.execute("select * from ERV where repName=? and genoStart=?", t)
   ind = cur.fetchone()
   return render_template('individual.html', ind = ind)

@app.route('/search.html')
def search():
    return render_template('search.html')

@app.route('/results.html')
def results():
   w = request.args.get('repFamily')
   if w=="":
      
   x = request.args.get('repName')
   y = request.args.get('genoName')
   z = request.args.get('strand')
   t = (w,x,y,z)
   cur = con.cursor()
   cur.execute("select * from ERV where repFamily=? and repName=? and genoName=? and strand=?", t)
   res = cur.fetchall()
   return render_template('results.html', res = res)

@app.route('/tools.html')
def tools():
    return render_template('tools.html')


@app.route('/help.html')
def help():
    return render_template('help.html')


if __name__ == "__main__":
    app.run()
