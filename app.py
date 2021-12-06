from flask import Flask, render_template

app = Flask(__name__)

@app.route('/add')
def add():  # put application's code here
    return 'Add'

@app.route('/delete')
def delete():  # put application's code here
    return 'Delete'

@app.route('/logout')
def logout():  # put application's code here
    return 'You have been logged out'

@app.route('/')
@app.route('/login')
def login():  # put application's code here
    return render_template('login.html')

@app.route('/home')
def home():  # put application's code here
    return render_template('home.html')


if __name__ == '__main__':
    app.run()
