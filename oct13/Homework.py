#Explain the difference between the = operator and the == operator in Python.
"""THe "=" it assigns the value to variable & == it verifies the operands are equal
or not if equal it will return Ture,else False"""
a = 2
b = 3
print(f'{a} and {b}') #assignment
print(a==b)#False
#What does the ** operator do in Python, and how is it used?
'''it is Arthimatic operaion i.e mathematical exponential operator'''
print('The exponential of 3 of 2',a**b)
#What does the ^ operator do in Python, and in what context is it commonly used?
'''It is Xor operator it is also called logic operators it set the output 1 when any input is high(1) 
& set the output to 0 when both the input is 1 or 0'''
print(a^a)# returns 0 as both are same here
print(b^a)# returns 1 as both are different  here