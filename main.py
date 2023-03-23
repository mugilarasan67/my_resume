"""
i = 1
while i <= 50:
    if i % 5 != 0:
        print(i)
    i = i+1
""
for i in range(1, 5):

    print("#", end="")
print()

for j in range(1, 5):
    print("&", end="")
""

for i in range(5):
    for j in range(i):
        print(i, end="")
    print()

""
for i in range(4):
    for j in range(4-i):
        print(j+1, end="")
    print()
""
x = int(input("enter a number :"))
if x <= 5:
    print("pass")
else:
    print("fail")
""

a = [1,2,3,4,5]
a.recerse
print(a)
""
i = 1
while i <= 10:
    print(i)
    i = i+1
""
for i in range(10):
    print(i+1)
""
import math
for i in range
""

a = int(input("enter a number1 : "))
b = int(input("enter a number2 : "))
c = int(input("enter a number3 : "))
d = int(input("enter a number4 : "))
if (a < b) & (c < b) & (d < b):
    print("is the greatest :", input(b))
elif (b < a) & (c < a) & (d < a):
    print("is the greatest :", input(a))
elif (a < d) & (b < d) & (c < d):
    print("is the greatest :", input(d))
else:
    print("is the greatest :", input(c))

""

i = 100
for i in range(100, -1, -1):
    print(i)
""

a = [1, 2, True, 33.45, "MUGIL"]
a.append(23)
print(a)


a = [1, 2, True, 33.45, "MUGIL"]
a.pop()
print(a)

a = [1, 2, True, 33.45, "MUGIL"]
a.pop(3)
print(a)

a = [1, 2, True, 33.45, "MUGIL"]
a.insert(1,122)
print(a)

a = [1, 2, True, 33.45, "MUGIL"]
a.remove(2)
print(a)

a = [1, 2, True, 33.45, "MUGIL"]
x = a.index(2)
print(x)

a = [1, 2, True, 33.45, "MUGIL",1,1,1,1,1]
x = a.count(0)
print(x)

a = [1, 2, True, 33.45, 1, 1, 1, 1, 1]
a.reverse()
print(a)
""
a = [111,222,333]
b = (1,5,6.7,88,9.56,1,5)
a.extend(b)
print(a)
print(b)
""

a = {1,2,3,4}
b = {3,4,5,6,7}
c = a.union(b)
print(c)

a = {1,2,3,4}
b = {3,4,5,6,7}
c = a.intersection(b)
print(c)

a = {1,2,3,4}
b = {3,4,5,6,7}
c = b.difference(a)
print(c)
""

a = "ADFG 34gh kjhg"
x = a.replace('g','r')
print(x)
""


a = 'mithrsn'
b = 'greem'
c = 'red'
mustr = "hi {}, {}bike, {}car"
x = mustr.format(a,b,c)
print(x)

""
a = 20
b = 30
c = a + b
print(c)

""

print("Printing current and previous number and their sum in a range(10)")
previous_num = 0

# loop from 1 to 10
for i in range(1, 11):
    x_sum = previous_num + i
    print("Current Number", i, "Previous Number ", previous_num, " Sum: ", x_sum)
    # modify previous number
    # set it to the current number
    previous_num = i

""

# accept input string from a user
word = input('Enter word ')
print("Original String:", word)

# get the length of a string
size = len(word)

# iterate a each character of a string
# start: 0 to start with first character
# stop: size-1 because index starts with 0
# step: 2 to get the characters present at even index like 0, 2, 4
print("Printing only even index chars")
for i in range(0, size - 1, 2):
    print("index[", i, "]", word[i])

""
a = input("the word")
x = list(a)
for i in x[4:]:
    print(i)

""
x = [10, 20, 30, 40, 10]
y = [75, 65, 35, 75, 30]

if x.index(0==4):
    print("true")
""

def first_last_same(numberList):
    print("Given list:", numberList)

    first_num = numberList[0]
    last_num = numberList[-1]

    if first_num == last_num:
        return True
    else:
        return False


numbers_x = [10, 20, 30, 40, 10]
print("result is", first_last_same(numbers_x))

numbers_y = [75, 65, 35, 75, 30]
print("result is", first_last_same(numbers_y))
""


a = [10,20,33,43,55]
for i in a:
    if i % 5 == 0:
        print(i)
""

x = "Emma is good developer. Emma is a writer"
print(x.count("Emma"))
""

num = 8
print('%o' % num)

""






a = input("enter a number")
print("the number" + a)


""

a = int(input("enter the number1 :"))
b = int(input("enter the number2 :"))
print(a + b)

""
a = input("enter the string")
b = a[::-1]
print(b)

""
a = input("enter:")
print(a.title())
print(a.upper())
print(len(a))
b = a[::-1]
print(b)
print(a.isalpha())
""

a = 87654
print("enter" + " " + str(a))

""

a = " anandh "
b = 15
c = 2021
print(" dear" + a + "," + "\n you have" + " " + str(b) + "days of leave balance for this \n year " + str(c) + ".")
""

a = input("user name : ")
b = input("email id : ")
c = input("phone no : ")
print("user name :" + a + "\nemail id :" + b + "\nphone no :" + c)
""
import math

x = float(input("number:"))
b = math.exp(x)
print(b)
""

param1 = 1
param2 = 2
print(str(int(param1+param2)))

""
a = "happy"
for i in range(4,-1,-1):
    print(a[i:])
""

a = "happy"
for i in range(0, 5, 1):
    print(a[:i+1])
""

a = input("enter your value :")
i = 0
while i < len(a):
    print(a[0:i+1])
    i = i + 1
""
a = "mugil"
for i in range(1,101,1):
    print(a)
""
a = int(input("enter a number : "))

for i in range(1, a+1):
    if a % i == 0:
        print(i)
""
# Define the input list
lst = [1, 2, -9, 6, -4, -3, 6, 4]

# Create two empty lists for positive and negative numbers
pos = []
neg = []

# Separate positive and negative numbers into their respective lists
for i in lst:
    if i >= 0:
        pos.append(i)
    else:
        neg.append(i)

# Concatenate the positive and negative lists to get the final list
lst = pos + neg

# Print the final list
print(lst)
""
a = "a,s,d,f,g,h"
for i in a:
    print(a[2:4])

""

a = "a,v,t,s,d"
b = ''
for i in a:
    if i == "," and "s":
        continue
    b = b + i
print(b)
""

from array import *
arr = array('i', [1, 2, 3, 4, 5])
br = array('i', [1, 2, 3, 4])

arr.append(2)
print(arr)

arr.remove(4)
print(arr)

arr.index(3)
print(arr)

arr.reverse()
print(arr)

br.extend(arr)
print(br)
""

a = [1,2,3,4,5,6,7,8]
b = (22,55,3,5,43,987)
del[2] = a
print(a)

""

a = ["mugil", "ram", "mugil"]
a.pop(1)
print(a)

""

a = [2, 3, 1, 4, 5, 2, 4, 3]
b = 1
for i in a:
    i *= b
    print(a)

""

# only allows alphabets and "4"
a = input("enter a letter :")
for i in range(1, 10):
    if a.isalpha() or a == '4':
        print(a)
        break
    elif i == 11:
        print("sorry try again later")
    else:
        print("try again")
    a = input("enter again:")
    i = i+1

""

for i in range(1, 101):
    print(i)
""
i = 1
while i <= 101:
    print(i)
    i = i+1

""

import random
a = random.randint(1, 20)
guess = int(input("enter a number :"))
while a != guess:
    if guess < a:
        print("number is small")
    else:
        print("number is large")
    if guess in range(1, 5):
        print("bye")
    guess = int(input("try again :"))
print("you won")
""

# guess a number with (guess count limitation)
import random
a = random.randint(1, 20)
guess = int(input("enter a number :"))
for i in range(1, 6):
    if a != guess:
        if a < guess:
            print("your guess is high")
        elif a > guess:
            print("your guess is low")
        guess = int(input("enter again :"))
    else:
        print("you guess the correct one")
        break
print("sorry try again later")
""

# print factors of input
a = int(input("enter a number"))
b = []
for i in range(1, a+1):
    if a % i == 0:
        b.append(i)
print("factors :", b)

"""

# split positive and negative separately
a = [2, -3, 4, 1, -5, 6, -1]
neg = []
pos = []
for i in a:
    if i < 0:
        neg.append(i)
    else:
        pos.append(i)
b = pos + neg
print(b)










































































































































































