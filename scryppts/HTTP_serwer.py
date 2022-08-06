from os import system
from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('main.html')


@app.route('/room')
def room():
    return render_template('room.html')


@app.route('/black_wall')
def black_wall():
    return render_template('black_wall.html')


@app.route('/lamp')
def lamp():
    return render_template('lamp.html')


@app.route('/picture')
def picture():
    return render_template('picture.html')


@app.route('/green_wall')
def green_wall():
    return render_template('green_wall.html')


@app.route('/device_control', methods=['GET'])
def device_control():
    args = request.args
    name = args.get('name')
    value = args.get('value')
    if name == "NOP":
        return "UNAVAILABLE"
    if (system("/home/pi/" + name + " " + value)) == 0:
        return "OPERATION SUCCESS"
    else:
        return "FAIL"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
