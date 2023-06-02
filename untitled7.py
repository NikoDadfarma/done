"""
resource:
    https://www.tutorialsteacher.com/python/error-types-in-python
"""
import math
#nameError -> Raised when a variable is not found in the 
#local or global scope.
a

#SyntaxError ->Raised by the parser when a syntax error 
#is encountered.
print 'I am Niko'

#TypeError ->Raised when a function or operation 
#is applied to an object of an incorrect type.
inputt='hello world'
print(int(inputt))

#IndexError ->	Raised when the index of a sequence is out 
#of range.
indexx=[1,2,3]
print(indexx[2:4])

#KeyError ->Raised when a key is not found in a dictionary.
keyDict={'Name':'Niko','age':20}
print(keyDict['year'])

#AttributedError -> 	Raised on the attribute assignment 
#or reference fails.	
y=10
print(y.append(12))

#ValueError ->Raised when a function gets an argument 
#of correct type but improper value
math.sqrt(-2)