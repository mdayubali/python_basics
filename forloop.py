my_iterable = [4,5,3, 6,2,1]
for item in my_iterable:
    print("hello")

sales = [2,4,2,4,55,33]
for sale in sales:
    print(f"Example sale on: {sale}")
employees  = {"chef":"leo","admin": "Ali"}
for key in employees:
    print(employees[key])
for position in employees:
    print(f"the key is {position} and the value is {employees[position]}")
print(employees.items())
# for loop in truple
my_list = [('chef', 'leo'), ('admin', 'Ali'),(1,2)]
for item1 ,item2 in my_list:
    print(item1, item2)

website design will not be affected by PHP version update