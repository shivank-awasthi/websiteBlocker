# this app is used to block certain websites during a fixed time
# of the day to prevent access to sites.

import os
import time
from datetime import datetime as dt
# check the operating system of machine.

opers = os.environ['OS']
if opers == 'Windows_NT':
    path = r"C:\Windows\System32\drivers\etc\hosts"
else:
    path = "/etc/hosts"

# take list of sites which are to be blocked.

sites = ["www.facebook.com","facebook.com"]

# open hosts file according to the given path
while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,16) :
        with open(path,'r+') as file:
            content = file.read()
            for website in sites:
                if website in content:
                    pass
                else:
                    hosts = open(path,'a')
                    hosts.write("\n 127.0.0.1 "+website)
                    hosts.close()
                print("Task complete as in working hours")
    else:
        with open(path,'r+') as file:
            content = file.readlines()
            file.seek(0)
            for lines in content:
                if not any(website in lines for website in sites):
                    file.write(lines)
            file.truncate()
        print("fun hours")
    time.sleep(5)
