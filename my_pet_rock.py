"""this cute little ascii art pet rock tells you pickup lines!!!"""

import random

def display_joke(jokes):
	a= random.choice(jokes)
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


jokes = ['You rock.',
		 'Please don\'t take my feelings for granite.',
		 'I lava you.',
		 'Can you make my bedrock?',
		 'Igneous is bliss.',
		 'I\'m a 10 on the Moh\'s scale of hardness.',
		 'You make me hard like a diamond.',
		 'Of quartz I\'ll marry you!',
		 'Can you ruby my back?',
		 'Are you sedimentary? Cuz I want a piece of you.',
		 'Without you, my life is in obsidian.',
		 'I marble over how great you are.',
		 'We are more than plutonic.',
		 'You are a basalt to my emotions.',
		 'You are as flat as a plateau.',
		 'You should be boulder.',
		 'Let\'s get stoned.',
		 'You crack me up like a fault line.',
		 'That is a nice cleavage you have.',
		 'You make me rock hard.',
		 'You are marblelous.',
		 'You have a heart of coal.',
		 'Take everything with a grain of sand.',
		 'Nice astroid.',
		 'We are like two tectonic plates; there is too much friction.',
		 'Is my subduction working?',
		 'You magmafy my heart.',
		 'My heart erupted like a volcano for you.',
		 'There\'s a lot of pressure underneath, if you know what I mean.',
		 'Will you be mine?',
		 'You aluminum my life!',
		 'Your Grand Tetons make me rocky.',
		 'Are you a mountain? \'Cuz I want to hump you.',
		 'You are a gem.',
		 'Under your pressure I metaphorphisize.',
		 'You are purpurate for me.',
		 'Are you a rare earth metal? Because mining you has polluted my heart.',
		 'I thought you were gold, but you are a pyrite bitch.',
		 'You poison my mind like arsenic.']

display_joke(jokes)


