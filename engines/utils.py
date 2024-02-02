import os
import time


from engines.models.result import Score

def dot_sleeper(sec: int):
    if os.environ.get('DEBUG') == 'ON':
        return
    for _ in range(sec):
        time.sleep(1)
        print('.', end='')

def show_banner(score: str = None, entry: bool = False):
    base = './banners'
    if entry:
        with open(f'{base}/banner.txt') as banner:
            print(banner.read())
        return
    
    if score == Score.HOLE_IN_ONE.value:
        with open(f'{base}/hio.txt') as banner:
            print(banner.read())
    elif score == Score.ALBATROSS.value:
        with open(f'{base}/albatross.txt') as banner:
            print(banner.read())
    elif score == Score.EAGLE.value:
        with open(f'{base}/eagle.txt') as banner:
            print(banner.read())
    elif score == Score.BIRDIE.value:
        with open(f'{base}/birdie.txt') as banner:
            print(banner.read())
    else:
        print(f'\n{score}..!')
