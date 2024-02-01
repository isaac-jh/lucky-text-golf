import os

from courses.normal import normal
from engines.models.golfer import Golfer

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

            if course_name == 'normal':
                return normal.go_round(current_user)
            
            break
