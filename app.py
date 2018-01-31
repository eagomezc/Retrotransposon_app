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
   l1s = cur.fetchmany(5000)
   cur.execute("select * from ERV where repClass='LTR'")
   ltrs = cur.fetchmany(5000)
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
      w='%'
   x = request.args.get('repName')
   if x=="":
      x='%'
   y = request.args.get('genoName')
   if y=="":
      y='%'
   z = request.args.get('strand')
   if z=="":
      z='%'
   a = request.args.get('amino')
   cur = con.cursor()
   cur.execute("select * from ERV where repFamily LIKE'"+w+"'and repName LIKE'"+x+"'and genoName LIKE'"+y+"'and strand LIKE'"+z+"'and (ORF1 LIKE'%"+a+"%' OR ORF2 LIKE'%"+a+"%' OR ORF3 LIKE'%"+a+"%')")
   res = cur.fetchall()
   return render_template('results.html', res = res)

@app.route('/resultsa.html')
def resultsa():
   w = request.args.get('ORF1')
   if w!="M":
      w='N'
   x = request.args.get('ORF2')
   if x!="M":
      x='N'
   y = request.args.get('ORF0')
   if y!="M":
      y='N'
   cur = con.cursor()
   cur.execute("select * from ERV where ORF1 LIKE'"+w+"%' and ORF2 LIKE'"+x+"%' and ORF3 LIKE'"+y+"%'")
   res = cur.fetchall()
   return render_template('resultsa.html', res = res, x=x)

@app.route('/tools.html')
def tools():
    return render_template('tools.html')


@app.route('/help.html')
def help():
    return render_template('help.html')


if __name__ == "__main__":
    app.run()
