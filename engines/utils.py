import os
import time

def dot_sleeper(sec: int):
    if os.environ.get('DEBUG') == 'ON':
        return
    for _ in range(sec):
        time.sleep(1)
        print('.', end='')
