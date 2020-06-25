# -*- coding: UTF-8 -*-
import sys

stat = []

filepath = '/tmp/reqstat.txt'
with open(filepath) as fp:
  line = fp.readline()
  while line:
    stat.append(line)
    line = fp.readline()

if len(sys.argv) > 1:
  if sys.argv[1] == 'list':
    vhost_list = []
    for str_stat in stat:
      key, _ = str_stat.split(":")
      host = '{open_br}"name": "{key}"{close_br}'.format(key=key, open_br='{', close_br='}')
      vhost_list.append(host)
    res = ", ".join(vhost_list)
    res = "[" + res + "]"

    print(res)
   
  else:
    host = sys.argv[1]
    req = 0
    found = False
    for str_stat in stat:
      key, val = str_stat.split(":")
      if key == host:
        req = int(val)
        Found = True

    print(req)

