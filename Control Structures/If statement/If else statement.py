	
#if else statement

gender = input("Gender? ")

#Taking input from user
gender = gender.lower()
#input taken from user is lowercased 
if gender == "male":
#if statement condition here is that entered string should be "male"
    print("Your cat is male")
elif gender == "female":
#elif is same as if I have added elif in detail in this file "if elif.py" check it
    print("Your cat is female")
else:
# else will activate when someone enters anything other than male or female in input
    print("Invalid input")


#this is a simple if else statement
age = int(input("Age of your cat? "))
if age < 5:
    print("Your cat is young.")
else:
    print("Your cat is adult.")
    
#output  : 
#1]
#Gender? male
#Your cat is male
#Age of your cat? 4
#Your cat is young.

#2]
#Gender? female
#Your cat is female
#Age of your cat? 6
#Your cat is adult.

#3]
#Gender? 0
#Invalid input
#Age of your cat? 0
#Your cat is young.
