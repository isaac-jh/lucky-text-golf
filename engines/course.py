import os
import time
from datetime import datetime

from courses.normal import normal
from engines.models.golfer import Golfer
from engines.models.hole import Hole
from engines.models.field import Field
from engines.models.result import Result
from engines.utils import dot_sleeper
from typing import List

def choose_course(current_user: Golfer):
    courses = list(os.scandir("./courses"))
    course_names = ''
    cnt = 1

    for course in courses:
        course_names += f'{cnt}. {course.name}\n'
        cnt += 1

    course_names += f'{cnt}. back\n'

    while True:
        course_index = int(input(f'\n\nWhich course do you want?\n{course_names}\nPlease type number of course : ')) - 1
        if course_index == len(courses):
            break

        if course_index < 0 or course_index > len(courses):
            print("\n\nUmm... You probably type wrong number..!")
            continue

        course_name = courses[course_index].name

        answer = input(f'\n\nYour choice is "{course_name}", right?\t ("y" or "yes" for yes, "n" or "no" for no) : ').lower()

        if answer == 'y' or answer == 'yes':
            print("\n\nOK!!! Enjoy your rounding :)")
            break

    print("\n\nRolling your distance condition!!\n\n")
    current_user.set_todays_distance_condition()

    for club, grade in current_user.caddy_back.get_grades().items():
        print(f'Rolling <{club}>')
        if grade == 'SSS':
            dot_sleeper(8)
        elif grade == 'SS':
            dot_sleeper(7)
        elif grade == 'S':
            dot_sleeper(6)
        elif grade == 'A':
            dot_sleeper(5)
        elif grade == 'B':
            dot_sleeper(4)
        elif grade == 'C':
            dot_sleeper(3)
        elif grade == 'D':
            dot_sleeper(2)
        else:
            dot_sleeper(1)
        print(f'<{grade}>\n')

    if course_name == 'normal':
        print(f"/n/nWe are going to {course_name} course")
        dot_sleeper(10)
        return run_course(current_user, normal.COURSE_DATA, course_name)
    

def run_course(current_user: Golfer, course: List[Hole], course_name: str):
    round_start = datetime.now()
    results = []
    hole_counter = 1
    for hole in course:
        remain = hole.total_distance
        print(f'----------<<< Hole {hole_counter} >>>----------')
        field = Field.TEE
        swing_counter = 0
        while True:
            if field == Field.GREEN:
                club = 'Putter'
                c = current_user.caddy_back.putter
            else:
                club, c = current_user.caddy_back.pick(remain)
            if field != Field.TEE and (club == 'Pitch' or club == 'Sand'):
                print(f'\n\nApproach with {club}')
                distance = current_user.approach(c, remain)
            elif club == 'Putter':
                print(f'\n\nPutting')
                distance = current_user.putting(c, remain)
            else:
                print(f'\n\nSwing with {club}')
                distance = current_user.swing(c, field)

            if club == 'Putter':
                dot_sleeper(distance)
            else:
                dot_sleeper(distance // 10)
            
            print(f'{distance}M')
            remain = remain - distance
            if remain < 0:
                remain = remain * -1
            time.sleep(1)

            if remain == hole.green_distance + 1:
                field = Field.FRINGE
            elif remain <= hole.green_distance:
                field = Field.GREEN
            elif remain == 1:
                print("\n\nConcede!!! :D")
                swing_counter += 1
                break
            elif remain == 0:
                print("\n\nHole In!!! XD")
                break
            else:
                field = hole.where_is_my_ball()
            print(f'\nBall is on the {field}')
            
            swing_counter += 1

            if swing_counter == hole.par - 1:
                print("\n\nDouble Par...X(")
                break

            print("\n\nMoving to ball")
            if field == Field.GREEN:
                dot_sleeper(distance)
            else:
                dot_sleeper(distance // 10)

        result = Result(swing_counter, hole.par)
        results.append(result)
        print(f'\n{result.score}..!')
        hole_counter += 1

    # result 종합이랑 gained exp 표시하고 유저 세이브
    total_exp = 0
    total_swing_score = 72
    for result in results:
        total_exp += result.exp
        total_swing_score += result.score_num
    
    results_for_save = { 'course': course_name, 'started_at': round_start, 'ended_at': datetime.now, 'holes': results }
    
    print("\n\nRounding ended!!\n\nYour Scores :")
    print("\n\nTotal Swing Score is")
    dot_sleeper(5)
    print(f' {total_swing_score}!!')
    print("\n\nTotal exp gained")
    dot_sleeper(5)
    print(f' {total_exp}exp!!')
    print("\n\n-----<<< All Holes Score >>>-----\n")
    hc = 1
    
    for result in results:
        time.sleep(1)
        print(f'Hole {hc} : {result.score}\n')
        hc += 1

    current_user.exp += total_exp
    current_user.cleared_courses.append(results_for_save)
    current_user.save()

    print("\nThanks for playing!")
    print("\nReturn to Club House")
    dot_sleeper(10)
