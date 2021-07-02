import random
def generateotp():
	otp=random.randint(1000,9999)
	return otp
print(" your 4 digit otp is:",generateotp())
