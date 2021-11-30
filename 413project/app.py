from flask import Flask

app = Flask(__name__)


@app.route('/')
def main():  # put application's code here
    return '413 Project'


if __name__ == '__main__':
    app.run()
