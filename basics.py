'''
Question: Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number. 
Suppose the following input is supplied to the program: 34,67,55,33,12,98 Then, 
the output should be: ['34', '67', '55', '33', '12', '98'] ('34', '67', '55', '33', '12', '98')

Hints: In case of input data being supplied to the question, it should be assumed to be a console input. tuple() method can convert list to tuple
################################################################################################################################################
n=input("Enter : ")
list1=n.split(",")
tuple1=tuple(list1)
print(list1, tuple1)
'''
################################################################################################################################################
'''

Question: Define a class which has at least two methods: getString: to get a string from console input printString: to print the string in upper case.
 Also please include simple test function to test the class methods.

Hints: Use init method

##############################################################################################################################################
class TwoMethods(object):
    def __init__(self):
        self.string = ""

    def gets_string(self):
        self.string = input("Give me a text: ")

    def __str__(self):
        print(self.string.upper())

tm = TwoMethods()
tm.gets_string()
tm.__str__()
'''
##############################################################################################################################################
'''

Question: Write a program that calculates and prints the value according to the given formula: Q = Square root of [(2 * C * D)/H]
 Following are the fixed values of C and H: C is 50. H is 30. D is the variable whose values should be input to your program in a comma-separated sequence. 
 Example Let us assume the following comma separated input sequence is given to the program: 100,150,180 The output of the program should be: 18,22,24

Hints: If the output received is in decimal form, it should be rounded off to its nearest value (for example, if the output received is 26.0, it should be printed as 26) 
In case of input data being supplied to the question, it should be assumed to be a console input.

##############################################################################################################################################
import math
c, h = 50, 30
d = input("Enter : ")
d_list, result = d.split(","), []
[result.append(round(math.sqrt(((2 * int(i) * c)/h)))) for i in d_list]
print(result)
'''

##############################################################################################################################################
'''
Question: Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array.
The element value in the i-th row and j-th column of the array should be i*j. Note: i=0,1.., X-1; j=0,1,¡­Y-1. 
Example Suppose the following inputs are given to the program: 3,5 Then, the output of the program should be: [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]

Hints: Note: In case of input data being supplied to the question, it should be assumed to be a console input in a comma-separated form.

'''

Question 7 ------>>>>>
 