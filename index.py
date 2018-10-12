from flask import Flask, render_template as rt


app = Flask(__name__)

@app.route('/index')
def index():
    return rt('index.html')

@app.route('/send')
def send():
    return rt('send.html')

@app.route('/receive')
def receive():
    return rt('receive.html')


if __name__ == '__main__':
    app.env = ''
    app.run('120.27.55.146',port=9998, debug=True)