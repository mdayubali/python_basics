# list is like as array in another programming language
# list is a sequence of items. It's may string,number or anything
my_var= 10
mylist = [1,4,'hello',my_var]
mylist1 = [1,4,49,24]
# print(type(mylist))
# print(type(my_var)) 
print(mylist)
# append();insert(); sort(); reverse(); pop(); del
# to add a item in a list at the last use append()
mylist.append('40')
print(mylist)
# add a item or new list into any place in a list use insert()
mylist1.insert(2,90)
print(mylist)
# use the sort() to sorting a list number
mylist1.sort()
print(mylist1)
# use reverse() to reverse a list mumber element

mylist1.reverse()
print(mylist1)
# use pop() to remove the last element by default
# You can specify a index number into the pop method as a parameter to delete specific element
mylist1.pop(2)
print(mylist1)

# del also delete the element to a specifix index of list
del mylist[2]
print(mylist)