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
        print(current_user.profile())
    elif choice == '3':
        print("Thank you for comming :) I'll wait your return!")
        break
    else:
        print("Wrong number..!!")
