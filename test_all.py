#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" test_backend.py

Backend testing
"""
__author__ = 'Scott Burns <scott.s.burns@vanderbilt.edu>'


from rcqr import backend
from rcqr.app import app

from qrcode.image.pure import PymagingImage

def test_qr_from_data():
    comp = backend.qr_image_from_data('blah blah blah')
    assert isinstance(comp, PymagingImage)

def test_encode_data():
    name, form = 'foo', 'bar'
    assert backend.encode_data(name, form) == 'https://www.google.com/#q=foobar'

def test_app_index():
    "Make sure / returns 200 OK"
    tc = app.test_client()
    r = tc.get('/')
    assert r.status == '200 OK'

def test_app_generate():
    "Assert we get a string from /generate"
    tc = app.test_client()
    r = tc.post('/generate', data=dict(name='foo', form='bar'))
    assert isinstance(r.data, basestring)
