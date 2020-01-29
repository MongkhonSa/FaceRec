#!/usr/bin/env python
from flask import Flask, render_template, Response
import cv2

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"



if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)