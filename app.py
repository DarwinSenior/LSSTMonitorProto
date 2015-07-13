from flask import Flask, redirect, request, abort, send_file
from flask.ext.cors import CORS


app = Flask(__name__, static_url_path="")

CORS(app, resources=r'*', allow_headers='Content-Type')

@app.route('/')
def intropage():
    return redirect("/index.html")

@app.route('/images/image.fits')
def images():
    return send_file('./images/image.fits')


if __name__ == "__main__":
    app.run(host="0.0.0.0" ,port=5000, debug=True)

