#import random module 
import random

#creating or definning function
def rpg(length):
	lower = "abcdefghijklmnopqrstuvwxyz"

	upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

	numbers = "0123456789"

	symbols = "[{}0*;/,._-"

	all = lower + upper + numbers + symbols
# accepting value more than 3 because most password are 4 digits
	if length<=3:
		print(' Enter password length more than 3')
 
	else:
		password = "".join(random.sample(all, length))
		print("password is : ",password)


while True:
	length= int(input('\nEnter length of password: '))
	rpg(length)
	
	k=input("\n Do you want to continue(Y)or(N)? : ")
	if k=='y'and'Y':
		continue
	else:
		print('\nbye')
		break
