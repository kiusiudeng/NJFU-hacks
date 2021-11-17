import requests
import sqlite3
from bs4 import BeautifulSoup
import time

conn = sqlite3.connect('Traffic.db')
c = conn.cursor()

while True:
    re = requests.get("http://202.119.210.2:85/book/view")
    tstamp = int(time.time())
    soup = BeautifulSoup(re.text, "html.parser")
    count = 3000-int(soup.find_all("div", "col-xs-6")[0].span.text)

    c.execute("INSERT INTO Traffic (TIME,COUNT) VALUES ({},{})".format(tstamp, count))
    conn.commit()

    time.sleep(10)

conn.close()