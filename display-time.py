from datetime import datetime as dt

while True:
    now = dt.now().strftime("%H:%M:%S")
    print(now, end='\r')
