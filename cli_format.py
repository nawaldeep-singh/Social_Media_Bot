import time

def dot(value=3,sec=0.3):
    i=0
    while i < value:
        time.sleep(sec)
        print(".",end="")
        i += 1
    print()