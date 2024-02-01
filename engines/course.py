import os
import time

from courses.normal import normal
from engines.models.golfer import Golfer
from engines.models.hole import Hole
from engines.models.field import Field
from engines.models.result import Result
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

    print("\n\nRolling your distance condition")
    current_user.set_todays_distance_condition()
    for _ in range(10):
        time.sleep(1)
        print('.')
    for club, grade in current_user.caddy_back.get_grades().items():
        print(f'/n{club} : {grade}')

    if course_name == 'normal':
        print(f"/n/nWe are going to {course_name} course")
        for _ in range(10):
            time.sleep(1)
            print('.')
        return run_course(current_user, normal.COURSE_DATA)
    

def run_course(current_user: Golfer, course: List[Hole]):
    results = []
    hole_counter = 1
    for hole in course:
        goal = hole.total_distance
        print(f'----------< Hole {hole_counter} >----------')
        field = Field.TEE
        swing_counter = 0
        while goal != 0:
            if field == Field.GREEN:
                club = 'Putter'
                c = current_user.caddy_back.putter
            else:
                club, c = current_user.caddy_back.pick(goal)
            if club == 'Pitch' or club == 'Sand':
                print(f'\n\nApproach with {club}')
                distance = current_user.approach(c, goal)
            elif club == 'Putter':
                print(f'\n\nPutting')
                distance = current_user.putting(c, goal)
            else:
                print(f'\n\nSwing with {club}')
                distance = current_user.swing(c, field)

            for _ in range(5):
                time.sleep(1)
                print('.')
            
            print(f'{distance}M')
            goal = goal - distance
            if goal < 0:
                goal = goal * -1
            time.sleep(1)

            if goal == hole.green_distance + 1:
                field = Field.FRINGE
            elif goal <= hole.green_distance:
                field = Field.GREEN
            elif goal == 1:
                print("\n\nConcede!!!")
                swing_counter += 1
                result = Result(swing_counter, hole.par)
                results.append(result)
                print(f'\n{result.score}..!')
                break
            elif goal == 0:
                print("\n\nHole In!!!")
                result = Result(swing_counter, hole.par)
                results.append(result)
                print(f'\n{result.score}..!')
            else:
                field = hole.where_is_my_ball()
            print(f'\nBall is on the {field}')
            
            swing_counter += 1

            if swing_counter == hole.par - 1:
                print("\n\nDouble Par...")
                result = Result(swing_counter, hole.par)
                results.append(result)
                break

    # result 종합이랑 gained exp 표시하고 유저 세이브
