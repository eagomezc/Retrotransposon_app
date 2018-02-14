#*************************************************
#               RETROtransposon
#*************************************************

#**********
# PACKAGES
#**********

from flask import Flask, render_template, request
import sqlite3 as sql
from massapp import mzidentml, mztab
from rpy2.robjects.packages import SignatureTranslatedAnonymousPackage as STAP

#****************
# Define the app
#****************

app = Flask(__name__)

#*****************************
# Calling the SQLite Database
#*****************************

con = sql.connect("final.db") #Using sqlite3 we connect the database with the main app
con.row_factory = sql.Row #This function allows to call the database row by row

#*********************
# App Website pages
#*********************

@app.route('/index.html')
def index():
    return render_template('index.html')
  
@app.route('/database.html')
def database():
   cur = con.cursor() #Object that allows to execute commands over the database
   cur.execute("SELECT DISTINCT repName, count(*) FROM ERV WHERE repClass='LINE' GROUP BY repName") #SELECT DISTINCT only selects the different
   l1s = cur.fetchall()  #elements, avoid showing repeat elements. Count(*) counts all the elements that share a same name
   cur.execute("SELECT DISTINCT repName, count(*) FROM ERV WHERE repClass='LTR' GROUP BY repName")
   ltrs = cur.fetchall() #Fetchall harvests in a list all the elements that pass the condition established for the WHERE command
   return render_template("database.html",l1s = l1s,ltrs=ltrs) #Then you can call the list in the HTML template. 

@app.route('/groups.html-<repName>') #groups(repName) opens a new page with the table of all the retrotransposon that share "repName".
def groups(repName):
   t = (repName,) #When the condition has a variable that changes, the SQLite recomendation is to use tuple and...
   cur = con.cursor()
   cur.execute("SELECT * FROM ERV WHERE repName=?", t) #... then call the tuple into the command. 
   group = cur.fetchall()
   return render_template('groups.html', group = group)

@app.route('/individual.html-<ind>-<individual>') #individual(ind,individual) opens a new page with the specific member page. 
def individual(ind,individual):
   t = (ind,individual)
   cur = con.cursor()
   cur.execute("select * FROM ERV WHERE repName=? AND genoStart=?", t)
   ind = cur.fetchone() #Since we are only expected one result, fetchone make the search faster. 
   
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

@app.route('/results.html') #results() is the result page for the search by name, strand, chromosome, amino acid sequence, etc. 
def results():
   w = request.args.get('repFamily') #The request function allows to get information that the user uploads through the HTML template.
   if w=="": #If the user does not upload something, the variable is replace for "%", which is a signal to look for everything. 
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
   cur.execute("SELECT * FROM ERV WHERE repFamily LIKE'"+w+"'AND repName LIKE'"+x+"'AND genoName LIKE'"+y+"%'AND strand LIKE'"+z+"'AND (ORF1 LIKE'%"+a+"%' OR ORF2 LIKE'%"+a+"%' OR ORF3 LIKE'%"+a+"%')") #%<value>% means to select the elements that cointains the specific value. 
   res = cur.fetchall()
   return render_template('results.html', res = res)

@app.route('/resultsa.html') #resultsa() is the result page for the search by the presence or absence of active translated ORFs.
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

@app.route('/amino.html-<aa>') #amino(aa) opens a new page with the table of all the retrotransposon that has the "aa" amino acid sequence.
def amino(aa):
   w=aa
   cur = con.cursor()
   cur.execute("SELECT * FROM ERV WHERE ORF1 LIKE'%"+w+"%' OR ORF2 LIKE'%"+w+"%' OR ORF3 LIKE'%"+w+"%'")
   group = cur.fetchall()
   return render_template('amino.html', group = group, w=w)

@app.route('/resultsb.html') #resultsb() is the result page for the search make for the MSRetroFinder tool. 
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

#*****************
# For running App
#*****************

if __name__ == "__main__":
    app.run()
