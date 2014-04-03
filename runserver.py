#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" runserver.py

For dev purposes only.
"""
__author__ = 'Scott Burns <scott.s.burns@vanderbilt.edu>'


from rcqr.app import app


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)