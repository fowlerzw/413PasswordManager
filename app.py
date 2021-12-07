from flask import Flask, render_template, request, session, redirect
import pandas as pd
import csv
from passlib.hash import pbkdf2_sha256
from cryptography.fernet import Fernet

key = "$pbkdf2-sha256$29000$lDKm1BrjHIOQshaidC4FYA$5XCeCdY9e0K7yzsMaVstl65KisBvotxOdNuh00zFvsc"
filename = "DataSet.csv"
app = Flask(__name__)

#this renders the logout template
@app.route('/logout')
def logout():  # put application's code here
    return render_template('logout.html')

#this renders logout to starting endpoint and /login with login template
@app.route('/')
@app.route('/login')
def login():  # put application's code here
    return render_template('login.html')

# This renders the main template with password data table
@app.route('/home')
def home():
    df = pd.read_csv(filename, names=["site","user","pass"])
    for passwords in df["pass"]:
        names = decrypt(passwords)
    result = df.to_html()
    return render_template('home.html',result = result)

# This checks if the masterkey is correct
@app.route('/getPassword', methods=['POST'])
def getPassword():
    #fill with code to save masterkey
    if request.method == 'POST':
        password = request.form['password']

        #stores current user password

        #check if password is correct
        if (pbkdf2_sha256.verify(password, key)):
            return redirect('home')
        else:
            return "nice try asshole"
        #redirects to home
        

# This adds a new entry to the data table
@app.route('/addPassword')
def addPassword():
    #fill with code to add a new password and domain
    if request.method == 'POST':
        domainname = request.form['domainname']
        domainname = request.form['username']
        password = request.form['password']

        # stores current user password
        session['domainname'] = domainname
        session['username'] = user
        session['password'] = password
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
    fernet = Fernet(key)
    encryptpass = fernet.encrypt(password.encode())
    return encryptpass

#decrypt
def decrypt(encryptpass):
    fernet = Fernet(key)
    decryptedpass = fernet.decrypt(encryptpass).decode()

    return decryptedpass

# This deletes the inputted entry from the data table
@app.route('/deletePassword')
def deletePassword():
    #fill with code to delete entry
    if request.method == 'POST':
        domainname = request.form['domainname']
        password = request.form['password']

        # stores current user password
        session['domainname'] = domainname
        session['password'] = password

        # Deletes from the data table

        # redirects to home (unneeded)
        return redirect('home')


if __name__ == '__main__':
    app.run()
