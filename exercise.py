"""
please create a variable named character
and assign the value "Jon Snow" to that variable

remember that Python is case sensitive!
"""
character = "Jon Snow"

"""
1. Create a variable named price and assign it to a
    value of 10
2. In the next line print out the value of a variable
    price, make sure you use the print function.
"""
price = 10
print(price)

"""
calculate the product of x and y, raise the product
    to the power of z and divide everything by 8
"""
x = 1
y = 2
z = 3
stuff = ((x*y)**z)/8
print(stuff)

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

"""
create a list of 3 items they can be of any datatype
print out the first item
print out the last item
"""
new_list = ["help", 13, 14.0, -4, 'c']
print(new_list[0])
print(new_list[-1])

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

letters = 'abcdefghijklmnopqrstuvwxyz'
print(letters[-2])
print(letters[24])
print(letters[23:25])
print(letters[-3:-1])

mylist = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(mylist[17])

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


/Users/seguia.timothy/PycharmProjects/udemy