CODE_HELLO = "1"
CODE_GOODBYE = "2"
CODE_HAPPY = "1"
CODE_PESSIMISTIC = "2"
CODE_BACK = "3"
CODE_RUSSIAN = "1"
CODE_ENGLISH = "2"

INITIAL_MENU = {"1": "HELLO", "2": "GOODBYE"}
HELLO_MENU = {"1": "Happy", "2": "Pessimistic", "3": "Back"}
LOCALIZED_MENU = {"1": "Привет", "2": "Hello", "3": "Back"}


while True:
    for key in INITIAL_MENU:
        print(key, ":", INITIAL_MENU[key])
    print()

    init = input('Please make a selection: ')

    if init is CODE_HELLO:
        for key in HELLO_MENU:
            print(key, ":", HELLO_MENU[key])
        print()

        mood = input('Please make a selection: ')
        if mood is CODE_HAPPY:

            while True:
                for key in LOCALIZED_MENU:
                    print(key, ":", LOCALIZED_MENU[key])
                print()

                localized = input('Please make a selection: ')
                if localized is CODE_RUSSIAN:
                    print("Здравствуй, дорогой друг\n")
                    continue
                elif localized is CODE_ENGLISH:
                    print("Hello, my dear friend\n")
                    continue
                elif localized is CODE_BACK:
                    break

        elif mood is CODE_PESSIMISTIC:
            print(":(")
            break
        elif mood is CODE_BACK:
            continue

    elif init is CODE_GOODBYE:
        print("buy buy")
        break




