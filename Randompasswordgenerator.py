import random

def rpg(length):
	lower = "abcdefghijklmnopqrstuvwxyz"

	upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

	numbers = "0123456789"

	symbols = "[{}0*;/,._-"

	all = lower + upper + numbers + symbols

	if length<=3:
		print(' Enter password length more than 3')
 
	else:
		password = "".join(random.sample(all, length))
		print("password is : ",password)


length= int(input('Enter length of password: '))
rpg(length)
