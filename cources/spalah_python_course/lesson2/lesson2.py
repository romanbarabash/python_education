listUser = (
    {'name': "voeeevan", 'tel': "31231231", "email": "vov@eww.ww"},
    {'name': "wwwww", 'tel': "123123123", "email": "aww.asdsaww"},
    {'name': "wwwww2222", 'tel': "00002312312", "email": "wewwwwwwwww"},
    {'name': "wwwww2222", 'tel': "00002312312", "email": "wewwwwwwwww"},
    {'name': "wwwww2222", 'tel': "00002312312", "email": "wewwwwwwwww"},
    {'name': "wwwww2222", 'tel': "00002312312", "email": "wewwwwwwwww"},
    {'name': "wwwww2222", 'tel': "00002312312", "email": "wewwwwwwwww"},
)


def display(Users):
    print("Hello".center(80, "-"))
    for user in Users:
        # print(user['name'] )
        # print("Name "+str(user["name"])+"xz  "+ "Tel "+str(user["tel
        print("| Name {:19}| tel {:19}|Email {:10}|".format(user['name'], user['tel'], user['email']))
    print("End".center(80, "-"))
    print("allUsers {:} ".format(len(Users)))


def display2(Users):
    print("".center(80, "-"))
    print("|{:^19}|{:^19}|{:^19}|".format("name".capitalize(), "tel".capitalize(), "Email".capitalize()))
    print("".center(80, "-"))
    for user in Users:
        print("|{:19}|{:19}|{:19}|".format(user['name'], user['tel'], user['email']))
    print("".center(80, "-"))
    print("allUsers {:} ".format(len(Users)))
    print("".center(80, "-"))


def wwww():
    print("wwwwwww")


display2(listUser)
print()
print()
print()

