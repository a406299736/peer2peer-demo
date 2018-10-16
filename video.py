from flask import Flask, render_template


app = Flask(__name__)

@app.route('/video')
def video():
    return render_template('video.html')


if __name__ == '__main__':
    app.env = ''
    app.run('120.27.55.146',port=9997, debug=True)