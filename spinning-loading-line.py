import time


lines = [
    "|",
    "/",
    "-",
    "\\",
]

i = 0
while True:
    if i == 4:
        i = 0
    print(lines[i], end='\r')
    i += 1
    time.sleep(1/2)
