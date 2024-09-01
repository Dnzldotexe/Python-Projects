import random
import time

def brute_force(s: str) -> None:
    temp = ""
    for letter in s:
        rand_letter = chr(random.randint(32, 126))
        while rand_letter != letter:
            print(temp + rand_letter)
            time.sleep(1/100)
            rand_letter = chr(random.randint(32, 126))
        temp += letter
    print(s)

brute_force("hello world")
