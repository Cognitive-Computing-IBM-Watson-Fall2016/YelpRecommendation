from flask import Flask
from flask import Flask, render_template, request, flash, session, redirect, url_for
from pymongo import MongoClient
from py_ms_cognitive import PyMsCognitiveImageSearch
from pos_wordcloud_generator import PosWordCloudGenerator
import json
import os
import nltk
import pymongo
import logging
logging.captureWarnings(True)

app = Flask(__name__, static_url_path='')
app.secret_key = 'YelpRecommendation development key'
try:
    nltk.data.find('tokenizers/punkt/english.pickle')
except LookupError:
    nltk.download('punkt')
try:
    nltk.data.find('corpora/wordnet')
except LookupError:
    nltk.download('wordnet')
try:
    nltk.data.find('taggers/averaged_perceptron_tagger')
except LookupError:
    nltk.download('averaged_perceptron_tagger')
from forms import QuestionForm
def makequery(a1,a2,a3,a4,a5):
    rqry=dict()
    subqrys=[]
    a1=int(a1)
    a2=int(a2)
    a3=int(a3)
    if a1==1 or a1==4:
        q1={"attributes.Has TV":True}
        subqrys.append(q1)
    else:
        q1={"attributes.Has TV":False}
        subqrys.append(q1)
    if a2==1 or a2==4:
        q2={"attributes.Wi-FI":"free","attributes.Outdoor Seating":True}
        subqrys.append(q2)
    else:
        q2={"attributes.Wi-FI":"no","attributes.Outdoor Seating":False}
        subqrys.append(q2)
    if a3==3 or a3==4:
        q3={"attributes.Price Range":{"$lte":2}}
        subqrys.append(q3)
    else:
        q3={"attributes.Price Range":{"$gte":3}}
        subqrys.append(q3)
    print a4
    a4=int(a4)
    if a4==1:
        q4={"attributes.Ambience.classy":True}
        subqrys.append(q4)
    elif a4==2:
        q4={"attributes.Ambience.upscale":True}
        subqrys.append(q4)
    elif a4==3:
        q4={"attributes.Ambience.trendy":True}
        subqrys.append(q4)
    elif a4==4:
        q4={"attributes.Ambience.divey":True}
        subqrys.append(q4)
    else:
        q4={"attributes.Ambience.casual":True}
        subqrys.append(q4)
    print a5
    a5=int(a5)
    if a5==1:
        q5={"attributes.Alcohol":"full_bar"}
        subqrys.append(q5)

    elif a5==4:
        q5={"attributes.Alcohol":"full_bar"}
        subqrys.append(q5)

    elif a5==2:
        q5={"attributes.Alcohol":"beer_and_wine"}
        subqrys.append(q5)
    else:
        q5={"attributes.Alcohol":"none"}
        subqrys.append(q5)
    
    rqry["$or"]=subqrys
    return rqry

@app.route("/", methods=['GET'])
def first():
    return render_template('first.html')

@app.route("/question", methods=['GET''POST'])
def question():
    form = QuestionForm()
    if request.method == 'POST':
        print 'POST'
        rqry=dict()
        answer = form.question1.data
        a1=form.question1.data
        a2=form.question2.data
        a3=form.question3.data
        a4=form.question4.data
        a5=form.question5.data
        
        print a1,a2,a3,a4,a5
        rqry=makequery(a1,a2,a3,a4,a5)
        print rqry
        return render_template('question.html', form=form)
        
    elif request.method == 'GET':
        print 'GET'
        session['question'] = 1
        return render_template('question.html', form=form)

@app.route("/result", methods=['GET','POST'])
def index():
    ##query for getting restaurant details from mongodb
    a1=request.form['q1']
    a2=request.form['q2']
    a3=request.form['q3']
    a4=request.form['q4']
    a5=request.form['q5']
    print a1
    qry=makequery(a1,a2,a3,a4,a5)
    print qry
    ##{"attributes.Ambience.trendy":True}
    res=query_restaurant(qry)
    rstrnt=res.get("names")
    stars=res.get("stars")
    reviews=res.get("reviews")
    rnge=range(len(stars))
    imgs=[]
    links=[]
    lt=[]
##    freqs=[{"text":"study","size":40},{"text":"motion","size":15},{"text":"forces","size":10},{"text":"electricity","size":15},{"text":"movement","size":10},{"text":"relation","size":5},{"text":"things","size":10},{"text":"force","size":5},{"text":"ad","size":5},{"text":"energy","size":85},{"text":"living","size":5},{"text":"nonliving","size":5},{"text":"laws","size":15},{"text":"speed","size":45},{"text":"velocity","size":30},{"text":"define","size":5},{"text":"constraints","size":5},{"text":"universe","size":10},{"text":"physics","size":120},{"text":"describing","size":5},{"text":"matter","size":90},{"text":"physics-the","size":5},{"text":"world","size":10},{"text":"works","size":10},{"text":"science","size":70},{"text":"interactions","size":30},{"text":"studies","size":5},{"text":"properties","size":45},{"text":"nature","size":40},{"text":"branch","size":30},{"text":"concerned","size":25},{"text":"source","size":40},{"text":"google","size":10},{"text":"defintions","size":5},{"text":"two","size":15},{"text":"grouped","size":15},{"text":"traditional","size":15},{"text":"fields","size":15},{"text":"acoustics","size":15},{"text":"optics","size":15},{"text":"mechanics","size":20},{"text":"thermodynamics","size":15},{"text":"electromagnetism","size":15},{"text":"modern","size":15},{"text":"extensions","size":15},{"text":"thefreedictionary","size":15},{"text":"interaction","size":15},{"text":"org","size":25},{"text":"answers","size":5},{"text":"natural","size":15},{"text":"objects","size":5},{"text":"treats","size":10},{"text":"acting","size":5},{"text":"department","size":5},{"text":"gravitation","size":5},{"text":"heat","size":10},{"text":"light","size":10},{"text":"magnetism","size":10},{"text":"modify","size":5},{"text":"general","size":10},{"text":"bodies","size":5},{"text":"philosophy","size":5},{"text":"brainyquote","size":5},{"text":"words","size":5},{"text":"ph","size":5},{"text":"html","size":5},{"text":"lrl","size":5},{"text":"zgzmeylfwuy","size":5},{"text":"subject","size":5},{"text":"distinguished","size":5},{"text":"chemistry","size":5},{"text":"biology","size":5},{"text":"includes","size":5},{"text":"radiation","size":5},{"text":"sound","size":5},{"text":"structure","size":5},{"text":"atoms","size":5},{"text":"including","size":10},{"text":"atomic","size":10},{"text":"nuclear","size":10},{"text":"cryogenics","size":10},{"text":"solid-state","size":10},{"text":"particle","size":10},{"text":"plasma","size":10},{"text":"deals","size":5},{"text":"merriam-webster","size":5},{"text":"dictionary","size":10},{"text":"analysis","size":5},{"text":"conducted","size":5},{"text":"order","size":5},{"text":"understand","size":5},{"text":"behaves","size":5},{"text":"en","size":5},{"text":"wikipedia","size":5},{"text":"wiki","size":5},{"text":"physics-","size":5},{"text":"physical","size":5},{"text":"behaviour","size":5},{"text":"collinsdictionary","size":5},{"text":"english","size":5},{"text":"time","size":35},{"text":"distance","size":35},{"text":"wheels","size":5},{"text":"revelations","size":5},{"text":"minute","size":5},{"text":"acceleration","size":20},{"text":"torque","size":5},{"text":"wheel","size":5},{"text":"rotations","size":5},{"text":"resistance","size":5},{"text":"momentum","size":5},{"text":"measure","size":10},{"text":"direction","size":10},{"text":"car","size":5},{"text":"add","size":5},{"text":"traveled","size":5},{"text":"weight","size":5},{"text":"electrical","size":5},{"text":"power","size":5}]
    print '**************************************************************************'
    extractor=PosWordCloudGenerator()
    for i in rnge:
        freqs=extractor.create_wordcloud(reviews[i])
        lt.append(freqs)
    for r in rstrnt:
        query=r+''+' Restaurant,Pittsburg,'
        try:
            bimg=PyMsCognitiveImageSearch('Api Key', query)
            res=bimg.search(limit=3,format='json')
        except:
            links=['','','']
            imgs.append(links)
            continue
        links=[]
        for i in res:
            links.append(i.content_url)
        imgs.append(links)
        
            
        
    return render_template("index.html",freqs=lt,rname=rstrnt,rnge=rnge,images=imgs,stars=stars)

def query_restaurant(query):
    client=MongoClient('mongodb://yelpers:<passwd>@ds139567.mlab.com:39567/w6998')
    db=client.w6998
    restrnt=db.restaurants
    result=dict()
    names=[]
    stars=[]
    text=[]
    for r in restrnt.find(query).limit(5).sort("stars",pymongo.DESCENDING):
        names.append(r["name"])
        stars.append(r["stars"])
        try:
            text.append(r["reviews"].encode("utf-8"))
        except UnicodeEncodeError:
            text.append('EncodingErrorinYelp dataset')
    result["names"]=names
    result["stars"]=stars
    result["reviews"]=text
    client.close()
    return result

Port = os.getenv('VCAP_APP_PORT', '5000')
HOST = str(os.getenv('VCAP_APP_HOST', 'localhost'))
if __name__ == "__main__":
    app.run(debug=True,host=HOST, port=int(Port))

