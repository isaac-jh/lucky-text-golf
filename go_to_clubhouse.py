import os
import json
import regex
from engines.golfer_model import Golfer

with open("./banner.txt") as banner:
    print(banner.read())

input("\n\n----------< Press Enter To Start >----------")

golfers = list(os.scandir("./golfers"))

if golfers:
    print('\n\nOh, You back again!')
    golfer_names = ''
    cnt = 1

    for golfer in golfers:
        name, _ = golfer.name.split('.')
        golfer_names += f'{cnt}. {name}\n'
        cnt += 1

    golfer_names += f'{cnt}. new\n'

    confirm = False
    while not confirm:
        golfer_index = int(input(f'\nWell... Your name is...?\n\n{golfer_names}\nPlease type number of your name : ')) - 1
        if golfer_index == len(golfers):
            print("\n\nOh! Sorry. You are a new commer!")
            while True:
                name = input("\nPlease tell me your name. Name can be only alphanumeric. (blank is convert to under bar '_') : ")

                if name in [golfer.name.split('.')[0] for golfer in golfers]:
                    print("/n/nOops, Same-Name person in here. Do you have another nickname...?")
                if not regex.match('^[a-zA-Z\s]+$', name):
                    print('\n\nOops, Something bad charactors in your name...')
                    continue

                name.replace(' ', '_')
                current_user = Golfer(name)
                current_user.save()
                print(f'\n\nWelcome, {name}!')
                break
            break

        if golfer_index < 0 or golfer_index > len(golfers):
            print("\n\nUmm... You probably type wrong number..!")
            continue
        name, _ = golfers[golfer_index].name.split('.')
        answer = input(f'\n\nYour name is "{name}", right?\t ("y" or "yes" for yes, "n" or "no" for no) : ').lower()

        if answer == 'y' or answer == 'yes':
            print('\n\nCool!! Thanks :) I will check your last datas...')
            with open(f'./golfers/{golfers[golfer_index].name}') as user_data:
                current_user = Golfer.fetch(json.loads(user_data.read()))
            confirm = True

else:
    print('\n\nOh, You came here first time!')
    while True:
        name = input('\n\nPlease tell me your name! Name can be only alphanumeric. (blank is convert to under bar "_") : ')
        if not regex.match('^[a-zA-Z\s]+$', name):
            print('\n\nOops, Something bad charactors in your name...')
            continue
        
        name.replace(' ', '_')
        current_user = Golfer(name)
        current_user.save()
        print(f'\n\nWelcome, {name}!')
        break
