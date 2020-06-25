# -*- coding: UTF-8 -*-
import requests
import sys

r = requests.get('http://127.0.0.1')
with open("/tmp/reqstat.txt", "w") as text_file:
  if r.status_code == 200:
    text_file.write(r.text)

