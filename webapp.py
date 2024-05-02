from flask import Flask, request, url_for, render_template, request
from markupsafe import Markup

import os
import json

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_main():
    return render_template('home.html')    
    
@app.route("/p1")
def render_page1():
    return render_template('page1.html')
    
@app.route("/p2")
def render_page2():
    return render_template('page2.html')
    
@app.route("/p3")
def render_page3():
    return render_template('page3.html')
    
@app.route("/p4")
def render_page4():
    return render_template('page4.html')
    
@app.route("/p5")
def render_page5():
    return render_template('page5.html')
    
@app.route("/p6")
def render_page6():
    return render_template('checkPage.html')
    
@app.route("/f")
def render_pageFinal():
    return render_template('FinalPage.html')
    
if __name__=="__main__":
    app.run(debug=True)
