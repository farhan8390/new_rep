#      0   1    2    3    4    5    6    7   8   9  10  11  12
a = ("a", "b", "c", "d", "e", "f", "g", "h","i","j","k","l","m")
    # -13  -12  -11  -10  -9   -8   -7   -6  -5  -4  -3  -2  -1                 
print(a[::-1])
print(a[2:5:1])
print(a[-1:-8:-1])
print(a[-6::7])
print(a[-6:-10:-1])
print(a[0:14:2])
print(a[-1:-14:-2])
print(a[-1:-11:-3])

str="Characters"
print(str[::-1])
print(str[6:9:1])
print(str[3:8:1])
print(str[3:10:2])
text1="my name is john and i m from london"
print(text1.split())
text2 = "abc$xyz$123"
print(text2.split("$"))
#Write a program to find smallest of given 2 numbers?
a = 7
b = 52
minimum = min(a, b)
print(f'Minimum of {a}, {b} is {minimum}')
 #Write a program to find biggest of given 3 numbers from the commad prompt?
a = 5
b = 4
c = 7

largest = 0

if a > b and a > c:
    largest = a
if b > a and b > c:
    largest = b
if c > a and c > b:
    largest = c

print(largest, "is the largest of three numbers.")

#Write a program to find biggest of given 2 numbers from the commad prompt?
a = 7
b = 52
maximum = max(a, b)
print(f'Maximum of {a}, {b} is {maximum}')
#using if statements
a = 7
b = 52

maximum = a
if b > a :
    maximum = b

print(f'Maximum of {a}, {b} is {maximum}')
#lambda fuction
a = 7
b = 52
maximum = max(a, b)
print(f'Maximum of {a}, {b} is {maximum}')
#Write a program to find smallest of given 3 numbers?
a = 22
b = 33
c = 11

smallest = 0

if a < b and a < c :
    smallest = a
elif b < c :
    smallest = b
else :
    smallest = c

print(smallest, "is the smallest of three numbers.")
#Write a program to check whether the given number is even or odd?
"""num = int(input("Enter a number: "))
if (num % 2) == 0:
   print("{0} is Even".format(num))
else:
   print("{0} is Odd".format(num))"""
#Eg 2:To print characters present in string index wise
text = 'Python is fun'
result = text.index('is')
print(result)
#To print Hello 30 times
print("Hello\n"*30)
#To display numbers from 0 to 10
for i in range(1, 11):
    print(i)
#To display odd numbers from 0 to 20    
for i in range(0,20):
    if i%2!=0:
        print(i,end=" ")
#To display numbers from 10 to 1 in descending order        
print("====Numbers from 10 to 1 in descending order====")
i = 10

while(i >= 1):
    print(i)
    i = i - 1
#To print sum of numbers presenst inside list
list = [12, 8, 9, 2, 5]
print(list)
print("sum of list: ",sum(list))
#To print numbers from 1 to 10 by using while loop
i = 1
while(i<=10):
    print(i)
    i += 1
#To display the sum of first n numbers    
"""n=int(input("Enter a number: "))
sum1 = 0
while(n > 0):
    sum1=sum1+n
    n=n-1
print("The sum of first n natural numbers is",sum1)"""
#write a program to prompt user to enter some name until entering Sumayya
"""NAME=str(input("enter the name: "))
print("hello",NAME)"""
#Write a program to access each character of string in forward and backward direction 
   #by using while loop and for loop?"""

def reverse_string(str):  
    str1 = ""
    for i in str:  
        str1 = i + str1  
    return str1
     
str = "FSONLINE"   
print("The forward string is: ",str)  
print("The backward string is",reverse_string(str))
str = "FARHAN" 
print ("The forward string  is : ",str)   
reverse_String = ""   
count = len(str)
while count > 0:   
    reverse_String += str[ count - 1 ] 
    count = count - 1 
print ("The backward string using a while loop is : ",reverse_String)
#Counting substring in the given String ?s="abcabcabcabcadda" count a,ab,"""
s = "abcabcabcabcadda"
substring = "a"
substring2="ab"
count = s.count(substring)
count = s.count(substring2)
print("The count a:", count)
print("The count ab:", count)
#Replacing a string with another string:
   #s="Learning Python is very difficult"
  # o/p:Learning Python is very easy"""
s="Learning Python is very difficult"
s1 = s.replace("difficult", "easy")
print(s1)
"""Q.Joining of Strings ?
t=('sunny','bunny','chinny')
o/p:sunny-bunny-chinny
"""
t=('sunny','bunny','chinny')
s = "-"
s = s.join(t)
print(s)
"""Q.
l=['hyderabad','singapore','london','dubai']
o/p:hyderabad:singapore:london:dubai
"""
"""s='learning Python is very Easy'
o/p: LEARNING PYTHON IS VERY EASY
o/p:learning python is very easy
o/p:LEARNING pYTHON IS VERY eASY
o/p:Learning Python Is Very Easy
o/p:Learning python is very easy
"""
s='learning Python is very Easy'
print(s.lower())
print(s.upper())
print(s.swapcase())
print(s.title())
a= s.capitalize()
print(a)
"""Q.Formatting the Strings ?
name="john"
salary=30000
address="london"
age=48
o/p:john 's salary is 30000 and his age is 48 and he is from london"""
"""Q.Program to reverse order of words 
input:Enter Some String:Learning Python is very easy!!
o/p: easy!!! very is Python Learning"""

def rev_words(string):  
    words = string.split(' ') 
    rev = ' '.join(reversed(words)) 
    return rev
 
s= "Learning Python is very easy!!"
print ("reverse: ",rev_words(s))
"""Q3. Program to reverse internal content of each word.
input: web Software Solutions
output:bew erawtfoS snoituloS
"""
"""Write a program to print characters at odd position and even position for the given 
String?"""

given_str = "Hi I AM Farhan saudagar "
  
print("Even Characters:", given_str[::2]) 
print("Odd Characters:", given_str[1::2])
"""Q6. Write a program to sort the characters of the string and first alphabet symbols 
followed by numeric values
input: B4A1D3
Output: ABD134
"""
"""QT]
words="the quick brown fox jumps over the lazy dog" 
o/p: ['the', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog'] 
"""

str = "The quick brown fox jumps over the lazy dog"

words = str.split(" ")

print(words)
"""Qt] 
words=["Balaiah","Nag","Venkatesh","Chiranjeevi"] 
o/p:['B', 'N', 'V', 'C'] 
"""