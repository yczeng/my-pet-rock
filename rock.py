"""this cute little ascii art pet rock tells you pickup lines!!!"""

import random

def display_joke(jokes):
	a = random.choice(jokes)
	print (
'  _'+ ('_' * (len(a) - 1))+ '\n' + 
'< ' + a +' >\n' + 
'  -'+ ('-' * (len(a) - 1))+ '\n' + 
'      \\\n' +
'       \\\n' + 
'    ___________________\n'
'   /                   \\\n'
'  (       o     o       )\n'
' (           u           )\n'
'  (_____________________)\n')


with open('jokes.txt') as f:
	content = f.readlines()
jokes = [x.strip() for x in content]

display_joke(jokes)


