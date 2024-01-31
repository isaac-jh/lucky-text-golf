from engines.user import login_or_create

with open("./banner.txt") as banner:
    print(banner.read())

input("\n\n----------< Press Enter To Start >----------")

login_or_create()
