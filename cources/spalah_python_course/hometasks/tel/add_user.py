#!/usr/bin/env python3
from sys import argv, exc_info

try:
    first_name = str(argv[1]).capitalize()
    last_name = str(argv[2]).capitalize()
    phone = argv[3]
    email = argv[4]

    min_phone_len = 6
    at_char = "@"
    dot_char = "."
    separator = ":+:"

    at_char_index = email.rfind(at_char)
    dot_char_index = email.rfind(dot_char)

    if len(phone) < min_phone_len:
        print("Phone should be at least '{}' digit".format(min_phone_len))
        exit()
    if ("@" not in email or "." not in email) or dot_char_index < at_char_index:
        print("Email should have valid '@', '.' characters")
        exit()

    serialize_str = "{first}{sep}{second}{sep}{phone}{sep}{email}".format(first=first_name, sep=separator,
                                                                          second=last_name, phone=phone, email=email)

    print(serialize_str)

    file_open = open('tel_book.txt', 'a')
    file_open.write(serialize_str + '\n')
    file_open.close()

except Exception:
    print(exc_info())
    exit(9)
