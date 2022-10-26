"""this cute little ascii art pet rock tells you pickup lines!!!"""

import random


def display_joke(jokes):
    a = random.choice(jokes)
    print(
        '╭─' + ('─' * len(a)) + '─╮\n' +
        '│ ' + a + ' │\n' +
        '╰◹' + ('─' * len(a)) + '─╯\n' +
        '     ____________________\n'
        '    ⎛⎛     ◜       ◝     ⎞\n'
        '   ╱░│      ◔     ◔      │\n'
        '  ⎛░░⎛         ◡          ╲\n'
        '  ╲░░╲▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁⎠\n')


with open('jokes.txt') as f:
    content = f.readlines()
jokes = [x.strip() for x in content]

display_joke(jokes)
