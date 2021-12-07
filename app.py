from flask import Flask, render_template, request, session, redirect
import pandas as pd
import csv

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
    #decrypts password
    for passwords in df["pass"]:
        namespace = passwords

    #Makes dataframe table to html
    df = pd.read_csv(filename, names=["site","user","pass"])
    result = df.to_html()
    session['table'] = result

    return render_template('home.html')

# This checks if the masterkey is correct
@app.route('/getPassword')
def getPassword():
    #fill with code to save masterkey
    if request.method == 'POST':
        password = request.form['password']

        #stores current user password
        session['password'] = password

        #check if password is correct

        #redirects to home
        return redirect('home')


# This adds a new entry to the data table
@app.route('/addPassword')
def addPassword():
    #fill with code to add a new password and domain
    if request.method == 'POST':
        domainname = request.form['domainname']
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
    return password
#decrypt
def decrypt():
    print("hi")

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
