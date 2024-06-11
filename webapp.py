from flask import Flask, request, url_for, render_template, redirect, session
from markupsafe import Markup

import os

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)
app.config['SECRET_KEY'] = os.environ["SECRET_KEY"]

@app.route("/")
def render_main():
    return render_template('home.html')    
    
@app.route("/p1",methods=['GET','POST'])
def render_page1():
    session.clear()
    return render_template('page1.html')
    
@app.route("/p2",methods=['GET','POST'])
def render_page2():
    if "A1" in session:
        return render_template('page2.html')
    else:
        if request.method == 'POST':
            session["A1"] = request.form['temp']
        return render_template('page2.html')
    
@app.route("/p3",methods=['GET','POST'])
def render_page3():
    if "A2" in session:
        return render_template('page3.html')
    else:
        if request.method == 'POST':
            session["A2"] = request.form['temp']
    return render_template('page3.html')
    
@app.route("/p4",methods=['GET','POST'])
def render_page4():
    if "A3" in session:
        return render_template('page4.html')
    else:
        if request.method == 'POST':
            session["A3"] = request.form['temp']
    return render_template('page4.html')
    
@app.route("/p5",methods=['GET','POST'])
def render_page5():
    if "A4" in session:
        return render_template('page5.html')
    else:
        if request.method == 'POST':
            session["A4"] = request.form['temp']
    return render_template('page5.html')
    
@app.route("/f",methods=['GET','POST'])
def render_pageFinal():
    x = 0
    y = {}
    if "A5" in session:
        return render_template('finalPage.html', numCorrect = x)
    else:
        if request.method == 'POST':
            session["A5"] = request.form['temp']
            if session["A1"] == "2":
               x += 1 
               y["Q1"] = "correct"
            else:
               y["Q1"] = "incorrect"
            if session["A2"] == "3":
               x += 1
               y["Q2"] = "correct"
            else:
               y["Q2"] = "incorrect"
            if session["A3"] == "10":
               x += 1
               y["Q3"] = "correct"
            else:
               y["Q3"] = "incorrect"
            if session["A4"] == "5":
               x += 1
               y["Q4"] = "correct"
            else:
               y["Q4"] = "incorrect"
            if session["A5"] == "256":
               x += 1
               y["Q5"] = "correct"
            else:
               y["Q5"] = "incorrect"
            return render_template('finalPage.html', numCorrect = x, qCorrect = y)
    
if __name__=="__main__":
    app.run(debug=True)
