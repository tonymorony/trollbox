#!/usr/bin/env python3

import os


header = "\
 _____       _                               _____  _____ \n\
|  __ \     | |                             /  __ \/  __ \\\n\
| |  \/ __ _| |_ _____      ____ _ _   _ ___| /  \/| /  \/\n\
| | __ / _` | __/ _ \ \ /\ / / _` | | | / __| |    | |    \n\
| |_\ \ (_| | ||  __/\ V  V / (_| | |_| \__ \ \__/\| \__/\\\n\
 \____/\__,_|\__\___| \_/\_/ \__,_|\__, |___/\____/ \____/\n\
                                    __/ |                 \n\
                                   |___/                  \n"

def colorize(string, color):

    colors = {
        'blue': '\033[94m',
        'magenta': '\033[95m',
        'green': '\033[92m',
        'red': '\033[91m'
    }
    if color not in colors:
        return string
    else:
        return colors[color] + string + '\033[0m'


def function1():
    print("You called function1")
    input("Press any key to continue")


def function2():
    print("You called function2")
    input("Press any key to continue")


menuItems = [
    {"Function1": function1},
    {"Function2": function2},
    {"Exit": exit}
]


def main():
    while True:
        os.system('clear')
        print(colorize(header, 'pink'))
        print(colorize('CLI for Alright\n', 'green'))
        for item in menuItems:
            print(colorize("[" + str(menuItems.index(item)) + "] ", 'blue') + list(item.keys())[0])
        choice = input(">> ")
        try:
            if int(choice) < 0:
                raise ValueError
            # Call the matching function
            list(menuItems[int(choice)].values())[0]()
        except (ValueError, IndexError):
            pass

if __name__ == "__main__":
    main()
