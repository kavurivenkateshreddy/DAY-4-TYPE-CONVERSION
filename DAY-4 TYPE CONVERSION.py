"""
Date: 21th April 2022 Thursday
Name: kavuri venkatesh reddy
File Desc: Type coversion
"""
'''we can convert the following things like.'''
'''int > int can convert into float and string.'''
'''float > float can convert into int and string.'''
'''we can combine or add int+int,float+float,int+float,float+int.'''
'''string > string cannot be convert into int and float (or) float when it has some text or word.'''
'''string > string can be converted into int and float when it contains a numbers in it.'''
'''Note-1 > when the value inside the str contains a int value then we can convert it into int and float.'''
'''Note-2 > when the value inside the str contains a float value then we cannot convert it into directly
but we can convert it into float.'''
a=5                    #int > float and str
print(float(a)) #5.0
print(str(a))   #5
b=3.5                  #float > int and str
print(int(b))   #3
print(str(b))   #3.5
c=3;d=7.5;             #combine or add > int+int,float+float,int+float,float+int
print(a+c)      #8
print(b+d)      #11.0
print(c+d)      #10.5
print(d+c)      #10.5
s='python'             #str > it can't convert into int and float when it has some text or word
# print(int(s)) #Type error
# print(float(s)) #Type error
x='4'                  #str > ir can be convertrd into int and float when it contains number in it
print(type(x))  #str
                       #Note-1
print(int(x))   #4  
print(float(x)) #4.0
r='5.6'                #Note-2
# print(int(r)) #Error
print(float(r)) #5.6
d=float(r)
print(int(d))   #5
"""STRING CONCATENATION:"""
'''Joining or combining two or multiple strings together is called as concatenation.'''
'''The following things can't be done:
int + str
float + str 
The above two cases are not possible.'''
x=4 ; m='py' ; v=3.2
print(type(x)) # int
print(type(m)) # str
print(type(v)) # float
# print(x+m) # Error
# print(m+v) # Error
'''
We can do the string concatenation only with strings.
we can do the concatenation with the help of '+' symbol.
Ex:
a='python'  ;  b='programming'
print(a+b)  # pythonprogramming'''
