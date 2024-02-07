import os
import time
from datetime import datetime

from engines.models.golfer import Golfer
from engines.models.hole import Hole
from engines.models.field import Field
from engines.models.result import Result
from engines.models.course import Course
from engines.utils import dot_sleeper, show_banner
from typing import List

def choose_course(current_user: Golfer):
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

    course = Course()
    easy = 0
    normal = 0
    hard = 0
    print("\n\nGenerating Course")
    for hole in course.data:
        print(f'\nGenerating Hole <{hole.num}>')
        dot_sleeper(3)
        print(f'par : {hole.par}  distance : {hole.total_distance}')
        if hole.par == 3:
            if hole.total_distance < 120:
                easy += 1
                print("-----EASY-----")
            elif hole.total_distance > 160:
                hard += 1
                print("-----HARD-----")
            else:
                normal += 1
                print("-----NORMAL-----")
        elif hole.par == 4:
            if hole.total_distance < 270:
                easy += 1
                print("-----EASY-----")
            elif hole.total_distance > 320:
                hard += 1
                print("-----HARD-----")
            else:
                normal += 1
                print("-----NORMAL-----")
        else:
            if hole.total_distance < 450:
                easy += 1
                print("-----EASY-----")
            elif hole.total_distance > 550:
                hard += 1
                print("-----HARD-----")
            else:
                normal += 1
                print("-----NORMAL-----")

    diff = sorted([('easy', easy), ('normal', normal), ('hard', hard)], key=lambda x: x[1])[2][0]

    print(f'\n\nAverage course difficulty : {diff}\n easy -> 1 * exp | normal -> 1.5 * exp | hard -> 2 * exp')
    time.sleep(2)

    print(f'\n\nWe are going to course')
    dot_sleeper(10)
    return run_course(current_user, course.data, diff)
    

def run_course(current_user: Golfer, course: List[Hole], diff: str):
    round_start = str(datetime.now())
    results = []
    hole_counter = 1
    for hole in course:
        remain = hole.total_distance
        print(f'\n\n<<<-----<<<-----<<< Hole {hole_counter} Par {hole.par} Distance {hole.total_distance}M >>>----->>>----->>>')
        time.sleep(3)
        field = Field.TEE
        swing_counter = 0
        while remain != 0:
            if field == Field.GREEN:
                club = 'Putter'
                c = current_user.caddy_back.putter
            else:
                club, c = current_user.caddy_back.pick(remain, field)

            if field != Field.TEE and (club == 'Pitch' or club == 'Sand'):
                print(f'\n\n[{swing_counter + 1}] Approach with {club}')
                distance = current_user.approach(c, field, remain)
            elif club == 'Putter':
                print(f'\n\n[{swing_counter + 1}] Putting')
                distance = current_user.putting(c, remain)
            else:
                print(f'\n\n[{swing_counter + 1}] Swing with {club}')
                distance = current_user.swing(c, field)
            dot_sleeper(3)
            print('💥')

            if distance == 0:
                print("\n\nOhhh..... Ball is flys away....")
                dot_sleeper(3)
                if hole.miss_shot_rule == Field.PENALTYAREA:
                    print("\nBall goes to Penalty Area")
                    print("\nScore Penalty  +1")
                    print("\nContinue at the Penalty Tee")
                    swing_counter += 2
                    remain -= int(remain * 3 / 10)
                    if remain <= hole.green_distance + 1:
                        remain = hole.green_distance + 5
                    field = Field.FAIRWAY
                else:
                    print("\nBall goes to O.B")
                    print("\nScore Penalty  +1")
                    swing_counter += 2
                time.sleep(5)
                print(f'\n<<<<<<< Remaining distance to hole : {remain} >>>>>>')
                continue

            if club == 'Putter':
                dot_sleeper(5)
            else:
                dot_sleeper(distance // 10)
            
            print(f'> {distance}M <')
            remain = remain - distance
            if remain < 0:
                remain = remain * -1
            time.sleep(1)

            if remain == hole.green_distance + 1:
                field = Field.FRINGE
                print(f'\nBall is on the FRINGE')
            elif remain == 1:
                print("\n\n/////////////// Concede!!! :D ///////////////")
                time.sleep(3)
                swing_counter += 1
                remain = 0
            elif remain == 0:
                print("\n\n/////////////// Hole In!!! XD ////////////////")
                time.sleep(3)
            elif remain <= hole.green_distance:
                field = Field.GREEN
                print(f'\nBall is on the GREEN')
            else:
                field = hole.where_is_my_ball()
                print(f'\nBall is on the {field.name}')
            time.sleep(3)
            
            swing_counter += 1

            if swing_counter >= (hole.par * 2):
                swing_counter = hole.par * 2
                break
            
            if remain != 0:
                print(f'\n<<<<<<< Remaining distance to hole : {remain} >>>>>>')

                print("\n\nMoving to ball")
                dot_sleeper(5)

        result = Result(swing_counter, hole.par)
        results.append(result)
        show_banner(result.score)
        hole_counter += 1

        print('\n\nGo to next hole')
        dot_sleeper(10)

    # result 종합이랑 gained exp 표시하고 유저 세이브
    total_exp = 0
    total_swing_score = 72
    for result in results:
        total_exp += result.exp
        total_swing_score += result.score_num

    if diff == 'normal':
        total_exp = int(total_exp * 1.5)
    elif diff == 'hard':
        total_exp = total_exp * 2
    
    results_for_save = { 'course': diff, 'started_at': round_start, 'ended_at': str(datetime.now()), 'holes': [result.__dict__ for result in results] }
    
    print("\n\nRounding ended!!\n\nYour Scores :")
    print("\n\nTotal Swing Score is")
    dot_sleeper(5)
    print(f' {total_swing_score}!!')
    print("\n\nTotal exp gained is")
    dot_sleeper(5)
    print(f' {total_exp}exp!!')
    if diff == 'normal':
        print(f' <<NORMAL course bonus x1.5>>')
    if diff == 'hard':
        print(f' <<<HARD course bonus x2>>>')
    before_level = current_user.get_level()

    print("\n\n-----<<< All Holes Score >>>-----\n")
    hc = 1
    
    for result in results:
        time.sleep(1)
        print(f'Hole {hc} : {result.score}\n')
        hc += 1

    current_user.exp += total_exp
    current_user.cleared_courses.append(results_for_save)
    current_user.save()
    time.sleep(5)

    if before_level != current_user.get_level():
        print("\nLevel up!!! Before :", before_level, " After :", current_user.get_level())

    print("\nThanks for playing!")
    print("\nReturn to Club House")
    dot_sleeper(10)
