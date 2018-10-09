
def new_line():
    print()
"""
please create a variable named character
and assign the value "Jon Snow" to that variable

remember that Python is case sensitive!
"""
character = "Jon Snow"
new_line()
"""
1. Create a variable named price and assign it to a
    value of 10
2. In the next line print out the value of a variable
    price, make sure you use the print function.
"""
price = 10
print(price)
new_line()
"""
calculate the product of x and y, raise the product
    to the power of z and divide everything by 8
"""
x = 1
y = 2
z = 3
stuff = ((x*y)**z)/8
print(stuff)
new_line()
"""
calculate the sum of a and b and printing out the integer
    version of the sum using a print function
a = 1.0
b = 2 
you want to have the integer version so you want to print out 3
"""
a = 1.0
b = 2
print(int(a) + b)
new_line()
"""
create a list of 3 items they can be of any datatype
print out the first item
print out the last item
"""
new_list = ["help", 13, 14.0, -4, 'c']
print(new_list[0])
print(new_list[-1])
new_line()
"""
1. print out the index of item 'h' in the square brackets
2. print out 'hn'
3. print out 'y' from letters
4. print out 'xy' from letters
5. print out the 18th item from mylist
"""
name = "John Smith"
print(name[2])
print(name[2:4])
new_line()

letters = 'abcdefghijklmnopqrstuvwxyz'
print(letters[-2])
print(letters[24])
print(letters[23:25])
print(letters[-3:-1])
new_line()

mylist = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(mylist[17])
new_line()
"""
1. add "John" to mylist
2. remove "John" from mylist
3. append the last item of list1 to list2

"""
mylist = ["Marry", "Jack"]
mylist.append("John")
print(mylist)
#mylist.insert(0,"John")
#print(mylist)
mylist.remove("John")
print(mylist)

list1 = [1.2323442655, 1.4534345567, 1.023458894]
list2 = [1.9934332091]
list2.append(list1[-1])
print(list2)

#tuples
mytuple = ("one", 2, 'three')
#/Users/seguia.timothy/PycharmProjects/udemy
new_line()

"""
creating a dictionary made of two keys and two values 
to mydict
"""
mydict = {"name":"tim", "lastName":"seguia"}
print(mydict.keys())
print(mydict.values())
new_line()

"""
creating your own functions
"""


print("hello!")
print("world!")
new_line()

def sum(a, b):
    return a + b

def converter(kg, coef = 2.20462):
    return kg * coef

def cel_to_fahr(c):
    return (c * (9 / 5)) + 32
print(cel_to_fahr(10))

def string_length(mystring):
    if type(mystring) == float or type(mystring) == int:
        print("Sorry integers don't have length")
    else:
        print(len(mystring))
string_length(10)
new_line()

"""
open fruits.txt
Then write some code that reads the content of the file and generates the following output in the command line:

pear
apple
orange
mandarin
watermelon
pomegranate
"""
myfile = open("fruits.txt","r")
content = myfile.read()
myfile.close()
print(content)
# contentList = content.splitlines()
# print(contentList)
# for i in contentList:
#     print(i)
"""
when it comes to for loops in other languages you need
to know the length of the actual list in order to 
iterate throughout that list. 
"""


"""
Create a for  loop block that iterates through the following list and prints out each item of the list in each iteration.

mylist = [1, 2, 3, 4, 5] 

Expected output:

1
2
3
4
5
"""

mylist = [1, 2, 3, 4, 5]
for i in mylist:
    print(i)
new_line()

"""
Create a for  loop that iterates through all the items of the following list and prints out the item if the item is greater than 2. 

mylist = [1, 2, 3, 4, 5] 

Expected output:

3
4
5
"""
mylist = [1, 2, 3, 4, 5]
for i in mylist:
    if i > 2:
        print(i)
new_line()

myfile = open("fruits.txt", "r")
content = myfile.read()
myfile.close()
contentlist = content.splitlines()
for i in contentlist:
    print(len(i))
new_line()
"""
The function gets celsius degrees as input and converts them to fahrenheit.

Please implement a for  loop that iterates through the following temperatures  list:

temperatures = [10, -20, 100]  and calls the above cel_to_fahr   function in each iteration.

In other words, this time you are using the function to calculate a series of values instead of just one value. 

The expected output: 

50.0
-4.0
212.0
"""

temperatures = [10, -20, 100]
for i in temperatures:
    print(cel_to_fahr(i))
new_line()

"""
creating a new file
"""

newfile = open("newfile.txt","w")
newfile.write("Tim\nJoe\nJack\n")
newfile.close()

myfile = open("newfile.txt","r")
content = myfile.read()
contentlist = content.splitlines()
print(contentlist)
# seek is brought back to zero and everything is overwritten
# append if you want to add to a file
myfile = open("newfile.txt","a")
# myfile.write("Mike")
# myfile.write("chub")
myfile.write("Mike\nChub\n")
myfile.close()

myfile = open("newfile.txt","r")
content = myfile.read()
contentlist = content.splitlines()
print(contentlist)
myfile.close()

newfile2 = open("newfile2.txt","w")
numbers = [1, 2, 3]
for i in numbers:
    newfile2.write(str(i)+"\n")
newfile2.close()
newfile2 = open("newfile2.txt","r")
content = newfile2.read()
newfile2.close()
contentlist = content.splitlines()
print(contentlist)
new_line()

x = 0
while x < 3:
    print("smaller " + str(x))
    x+=1


temperatures = [10, -20, -289, 100]


def c_to_f(c):
    if c < -273.15:
        return ""
    else:
        f = c * 9/5 + 32
        return f


with open("tempfile.txt","w") as tempfile:
    for t in temperatures:
        if t > -273.15:
            print(c_to_f(t))
            tempfile.write(str(c_to_f(t)) + "\n")


