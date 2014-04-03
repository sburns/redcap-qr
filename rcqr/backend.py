#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" backend.py

Main functionality for generating a QR code from input
"""

__author__ = 'Scott Burns <scott.s.burns@vanderbilt.edu>'

import qrcode
from qrcode.image.pure import PymagingImage


def qr_image_from_data(encoded):
    return qrcode.make(encoded, image_factory=PymagingImage)


def encode_data(name, form):
    """Right now, this is stupid.

    This will need to be fixed to generate a proper URL to REDcap

    Most likely we'll hit the REDCap db, filter to get a record ID
    and plunk it into the URL."""
    google_url = 'https://www.google.com/#q={}'.format(name + form)
    return  google_url
