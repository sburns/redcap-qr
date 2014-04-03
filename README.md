redcap-qr
=========

A tiny web app to generate barcodes linking to REDCap data entry pages

The idea is to take a patient's name, look them up in a REDCap database and present a QR code embedding a link to a data entry form in that database. This *should* reduce data entry errors in which data is entered into the wrong record.

Install
-------

```
$ pip install -r requirements.txt
```

Run
---

In development:

`$ make run`

In production:

`$ gunicorn -c gunicorn.py.ini rcqr:app`

Test
----

`$ make test`

