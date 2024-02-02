import time

def dot_sleeper(sec: int):
    for _ in range(sec):
        time.sleep(1)
        print('.')
