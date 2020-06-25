INSTALL

1. Install Openresty
2. mv reqcounter.lua to /usr/local/openresty/lualib/
3. Insert from nginx.conf to your working configuration
4. From crontab add every minute job to your crontab 
5. mv getstat.py; reqparse.py to /opt/
6. from zabbix_agentd.conf add  UserParameter's
7. Test curl http://127.0.0.1/
8. Import xml template in you zabbix dashboard
