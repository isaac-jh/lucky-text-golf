import os
import json

with open("./banner.txt") as banner:
    print(banner.read())

input("\n\nHello, Welcome!!\t(Press Enter)")

golfers = list(os.scandir("./golfers"))

if golfers:
    print('\n\nOh, You back again!')
    golfer_names = ''
    cnt = 1

    for golfer in golfers:
        name, _ = golfer.name.split('.')
        golfer_names += f'{cnt}. {name}\n'
        cnt += 1

    confirm = False
    while not confirm:
        golfer_index = int(input(f'\n\nWell... Your name is...?\n\n{golfer_names}\n\nPlease type number of your name : ')) - 1
        if golfer_index < 0 or golfer_index >= len(golfers):
            print("\n\nUmm... You probably type wrong number..!")
            continue
        name, _ = golfers[golfer_index].name.split('.')
        answer = input(f'\n\nYour name is "{name}", right?\t ("y" or "yes" for yes, "n" or "no" for no) : ').lower()

        if answer == 'y' or answer == 'yes':
            print('\n\nCool!! Thanks :) I will check your last datas...')
            current_user = json.loads(open(f'./golfers/{golfers[golfer_index].name}').read())
            confirm = True

else:
    # TODO - user 없을 시 데이터 받아서 생성
    pass
