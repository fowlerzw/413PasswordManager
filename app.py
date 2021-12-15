
from flask import Flask, render_template, request, session, redirect, url_for
import pandas as pd
import csv

from passlib.hash import pbkdf2_sha256
from cryptography.fernet import Fernet



pee = b'kh8n73vwtCY77uC7UGI6Lyqryw_1lpirSs9lqIaFHJY='
f = Fernet(pee)
key = "$pbkdf2-sha256$29000$lDKm1BrjHIOQshaidC4FYA$5XCeCdY9e0K7yzsMaVstl65KisBvotxOdNuh00zFvsc"
filename = "DataSet.csv"


app = Flask(__name__)
app.config['SECRET_KEY'] = 'c676dfde28b0b13ce00ba2455791628b'


#this renders the logout template
@app.route('/logout')
def logout():  # put application's code here
    return render_template('logout.html')

#this renders logout to starting endpoint and /login with login template
@app.route('/')
@app.route('/login')
def login():
    session.pop('logged_in', None)
    session['logged_in'] = False
    return render_template('login.html')

# This renders the main template with password data table
@app.route('/home', methods=['GET', 'POST'])
def home():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    else:
        df = pd.read_csv(filename, names=["site", "user", "pass"], encoding='unicode_escape')
        for passwords in df["pass"]:
            names = decrypt(passwords)
            df["pass"].replace({passwords: names}, inplace=True)

        result = df.to_html()
        return render_template('home.html', result=result)

# This checks if the masterkey is correct
@app.route('/getPassword', methods=['GET', 'POST'])
def getPassword():
    #fill with code to save masterkey
    if request.method == 'POST':
        password = request.form['password']

        #check if password is correct
        if (pbkdf2_sha256.verify(password, key)):
            session['logged_in'] = True
            return redirect('home')
        else:
            session['logged_in'] = False
            return redirect('login')
        #redirects to home
        

# This adds a new entry to the data table
@app.route('/addPassword', methods=['GET', 'POST'])
def addPassword():
    #fill with code to add a new password and domain
    if request.method == 'POST':
        domainname = request.form['domainname']
        user = request.form['username']
        password = request.form['password']

        # stores current user password
        
        encryptpass = encrypt(password)

        # adds to the data table
        rows = [str(domainname),str(user),str(encryptpass)]
        with open(filename, 'a') as csvfile: 
            csvwriter = csv.writer(csvfile) 
            csvwriter.writerow(rows)

        # redirects to home (unneeded)
        return redirect('home')


#encrypt
def encrypt(password):
  

    password = password.encode()
    encryptpass = f.encrypt(password)
    return encryptpass

#decrypt
def decrypt(encryptpass):

    encryptpass = encryptpass[2:-1]
    passw = encryptpass.encode()
    decryptedpass = f.decrypt(passw)
    decryptedpass = decryptedpass.decode("utf-8") 
    return decryptedpass

# This deletes the inputted entry from the data table
@app.route('/deletePassword', methods=['GET', 'POST'])
def deletePassword():
    #fill with code to delete entry
    if request.method == 'POST':
        domainname = request.form['rowNum']
        df = pd.read_csv(filename, names=["site","user","pass"])
        df.drop(int(domainname),0,inplace=True)
        
        df.to_csv(filename,header=False,index=False)
        return redirect('home')




if __name__ == '__main__':
    app.run()
