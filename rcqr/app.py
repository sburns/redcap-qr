#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" app.py

"""
__author__ = 'Scott Burns <scott.s.burns@vanderbilt.edu>'

from StringIO import StringIO

from flask import Flask, render_template, request

app = Flask(__name__)

from .backend import qr_image_from_data, encode_data

@app.route("/", methods=["GET"])
def index():
    return render_template('index.html')


@app.route('/generate', methods=["POST"])
def generate_ajax():
    name = request.form.get('name', '')
    form = request.form.get('rcform', '')
    encoded = encode_data(name, form)
    img = qr_image_from_data(encoded)
    io = StringIO()
    img.save(io)
    io.seek(0)
    return io.getvalue().encode('base64')