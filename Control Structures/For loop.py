#for loops 
#Example 1
city = ['Tokyo','New York','Toronto','Hong Kong']
print('Cities loop:')
#city is a variable that has string values as 'Tokyo','New York', 'Toronto','Hong Kong' in a array that is Tokyo has index value of zero and respectivetively each city has one increase
for x in city:
#x variables value increase till it has last number after that loop ends    
    print('City: ' + x)

print('\n')  # newline
#output for Example 1:
#Cities loop:
#City: Tokyo
#City: New York
#City: Toronto
#City: Hong Kong



#Example 2
num = [1,2,3,4,5,6,7,8,9]
#num is variable which has values as array of numbers 
print('x^2 loop:')
for x in num:
#x will go through each element in index order till it reaches last elementof array and ends the loop 
    y = x * x
    print(str(x) + '*' + str(x) + '=' + str(y))
    
#output of Example 2:
#x^2 loop:
#1*1=1
#2*2=4
#3*3=9
#4*4=16
#5*5=25
#6*6=36
#7*7=49
#8*8=64
#9*9=81
