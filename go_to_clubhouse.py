from datetime import datetime

from engines.user import login_or_create
from engines.course import choose_course
from engines.utils import show_banner

show_banner(entry=True)

input("\n\n----------< Press Enter To Start >----------")

current_user = login_or_create()

while True:
    choice = input('\n\nWhat you going to do?\n\n1. Rounding\n2. See My Profile\n3. Go to Home\n\nPlease type number : ')
    if choice == '1':
        choose_course(current_user)
    elif choice == '2':
        profile = current_user.profile()
        print(f'name : {profile.get('name')}')
        print(f'level : {profile.get('level')}')
        print(f'total exp earned : {profile.get('exp')}')
        print(f'total clear count : {profile.get('cleared_count')}')

        cleared_courses = profile.get('cleared_course_detail')
        score_aggregation = {}
        total_play_time: datetime

        for courses in cleared_courses:
            total_play_time += datetime.fromisoformat(courses.get('ended_at')) - datetime.fromisoformat(courses.get('started_at'))
            holes = courses.get('holes')
            for detail in holes:
                score_aggregation[detail.get('score')] = score_aggregation.get(detail.get('score'), 0) + 1

        print(f'total playtime : {total_play_time}\n')
        for score, count in score_aggregation.items():
            print(f'{score} : {count}')

        answer = input("If you want see more details, type 'y' or 'yes'. : ")
        if answer == 'y' or answer == 'yes':
            for course in cleared_courses:
                print(f'started at : {course.get('started_at')}')
                print(f'ended at : {course.get('ended_at')}')
                for hole in course.get('holes'):
                    for k, v in hole.items():
                        print(f'\t{k} : {v}')

    elif choice == '3':
        print("Thank you for comming :) I'll wait your return!")
        break
    else:
        print("Wrong number..!!")
