from flask import Flask, render_template, request
import random
import os
import threading
import json

import requests # pip install requests

r =requests.get('http://206.189.40.80')

if __name__ == '__main__':
    app.debug = True
    host = os.environ.get('IP', '206.189.40.80')
    port = int(os.environ.get('PORT', 80))
    app.run(host=host, port=port)

@app.route('/')
def index():
    return redirect(url_for('request_info'))

@app.route('/info')
def info():
    return redirect(url_for('request_info'), code=301)


@app.route('/request-info')
def request=info():
    geoip_url = 'http://freegeoip.net/json/{}'.format(request.remote_addr)
    client_location = requests.get(geoip_url).json()
    return render_template('requests/info.html',
                          client_location =client_location)


from mechanize import Browser
import bs4
from bs4 import BeautifulSoup

br = Browser()
br.set_hadle_robots(False)
br.set_handle_refresh(False)

example_url = 'http://206.189.40.80'

response = br.open(example_url)
soup = BeautifulSoup(response)
soup.find("Script", language = 'javascript')

raw = "{" + "\n".join(str(soup.find("script")).split("\n")[4:-3])

json.obj = json.loads(raw)
