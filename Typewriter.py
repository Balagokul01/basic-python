#shows text word by word like it's typed
from time import sleep
def printte(string, delay):
	for i in str(string):
		print(i, end="", flush=True)
		sleep(delay)
	print('')


printte('This string will be "typed" out letter by letter.\nPretty cool, right?',0.05)
printte(f'Here is an example of typing out an integer\n{1234}\n', 0.08)
printte(f'And a float: {1.234}', 0.0)
