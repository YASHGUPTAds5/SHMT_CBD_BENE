from crawler import *
from datetime import datetime

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print((current_time))
j = 1
while True:
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    if current_time == "10:57:20":
        print(j)
        j += 1
        crawl()