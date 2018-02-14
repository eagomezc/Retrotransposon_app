#RETROtransposon

#Import Classes:
from flask import Flask, render_template, request
import sqlite3 as sql
from massapp import mzidentml, mztab
from rpy2.robjects.packages import SignatureTranslatedAnonymousPackage as STAP

app = Flask(__name__)

con = sql.connect("final.db")
con.row_factory = sql.Row

@app.route('/index.html')
def index():
    return render_template('index.html')
  
@app.route('/database.html')
def database():
   cur = con.cursor()
   cur.execute("SELECT DISTINCT repName, count(*) FROM ERV WHERE repClass='LINE' GROUP BY repName") 
   l1s = cur.fetchall()
   cur.execute("select DISTINCT repName, count(*) FROM ERV WHERE repClass='LTR' GROUP BY repName")
   ltrs = cur.fetchall()
   return render_template("database.html",l1s = l1s,ltrs=ltrs)

@app.route('/groups.html-<repName>')
def groups(repName):
   t = (repName,)
   cur = con.cursor()
   cur.execute("select * FROM ERV WHERE repName=?", t)
   group = cur.fetchall()
   return render_template('groups.html', group = group)

@app.route('/individual.html-<ind>-<individual>')
def individual(ind,individual):
   t = (ind,individual)
   cur = con.cursor()
   cur.execute("select * FROM ERV WHERE repName=? AND genoStart=?", t)
   ind = cur.fetchone()
   with open('cariofunctions.R', 'r') as f:
     string_again = f.read()
   imgs = STAP(string_again, "imgs")
   c = ind["genoName"][:5]
   c = c.replace("_", "")
   start = int(ind["genoStart"])
   end = int(ind["genoEnd"])
   pngs = ""
   zpngs = ""
   if c!="chrUn":
      pngs = "static/img/"+c+str(start)+".png"
      zpngs = "static/img/z"+c+str(start)+".png"
      cimg = imgs.localization(c,start,end,pngs)
      zimg = imgs.zoom(c,start,end,zpngs)
   else:
      zpngs = "static/img/un.png"
   return render_template('individual.html', ind = ind, pngs=pngs, zpngs=zpngs)

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
   cur.execute("SELECT * FROM ERV WHERE repFamily LIKE'"+w+"'AND repName LIKE'"+x+"'AND genoName LIKE'"+y+"%'AND strand LIKE'"+z+"'AND (ORF1 LIKE'%"+a+"%' OR ORF2 LIKE'%"+a+"%' OR ORF3 LIKE'%"+a+"%')")
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
   z = request.args.get('repFamily2')
   cur = con.cursor()
   cur.execute("SELECT * FROM ERV WHERE repClass LIKE'"+z+"'AND ORF1 LIKE'"+w+"%' AND ORF2 LIKE'"+x+"%' AND ORF3 LIKE'"+y+"%'")
   res = cur.fetchall()
   return render_template('resultsa.html', res = res)

@app.route('/tools.html')
def tools():
    cur = con.cursor()
    cur.execute("SELECT * from Fill")
    rows=cur.fetchall()
    return render_template('tools.html',rows=rows)

@app.route('/amino.html-<aa>')
def amino(aa):
   w=aa
   cur = con.cursor()
   cur.execute("SELECT * FROM ERV WHERE ORF1 LIKE'%"+w+"%' OR ORF2 LIKE'%"+w+"%' OR ORF3 LIKE'%"+w+"%'")
   group = cur.fetchall()
   return render_template('amino.html', group = group, w=w)

@app.route('/resultsb.html')
def resultsb():
    ml=request.args.get('mzidentml')
    mt=request.args.get('mzTab')
    tissue=request.args.get('tissue')
    if ml==None:
       seq=mztab(mt)
    else:
       seq=mzidentml(ml)
    amino=[]
    fills=[]
    ress=[]
    cur = con.cursor()
    for i in range(0,len(seq)):
        t=(seq[i],tissue)
	cur.execute("SELECT * FROM Fill WHERE Amino LIKE'"+seq[i]+"'AND Tissue LIKE'"+tissue+"'")
        fill=cur.fetchone()
        if fill:
           amino.append(seq[i])
           fills.append(fill)
           ress.append("")
        else:
           cur.execute("SELECT * FROM ERV WHERE ORF1 LIKE'%"+seq[i]+"%' OR ORF2 LIKE'%"+seq[i]+"%' OR ORF3 LIKE'%"+seq[i]+"%'")
           res = cur.fetchall()
           if res:
              amino.append(seq[i])
              ress.append(res)
              fills.append("")
              cur.execute("INSERT INTO Fill (Amino,Tissue) VALUES (?,?)",t)
              con.commit()
    return render_template('resultsb.html',ress=ress, fills=fills, amino=amino, tissue=tissue)

@app.route('/help.html')
def help():   
    return render_template('help.html')


if __name__ == "__main__":
    app.run()
