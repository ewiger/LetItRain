#!/usr/bin/env python
from __future__ import print_function
import json
import time
from sqlite3 import dbapi2 as sqlite3
from hashlib import md5
from datetime import datetime
from flask import Flask, request, session, url_for, redirect, \
     render_template, abort, g, flash, _app_ctx_stack
from werkzeug import check_password_hash, generate_password_hash


# configuration
# DATABASE = '/tmp/minitwit.db'
PER_PAGE = 30
DEBUG = True
SECRET_KEY = 'development key'

# create our little application :)
app = Flask(__name__)
app.config.from_object(__name__)
app.config.from_envvar('LETITRAIN_SETTINGS', silent=True)


@app.route('/')
def web_server():
    return render_template('layout.html')


def what_is_my_ip():
    import urllib
    ip_json = urllib.urlopen('http://wtfismyip.com/json').read()
    return json.loads(ip_json)['YourFuckingIPAddress']

if __name__ == '__main__':
    # Listen on all public IPs
    print('Your public ip is: %s' % what_is_my_ip())
    app.run(host='0.0.0.0')
