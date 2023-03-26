# In python function is define as def keyword and use snakecase to define function name
def my_func():
    return "Hello world"
my_var = my_func()
print(my_var)
# Always focus on the indentation 
my_list  = [1,3,423,42,10,2,5,20,20,9,8,7,6]

def checker(list_to_check):
    for num in list_to_check:
        if num == 10:
            return True 
    return False
print(checker(my_list))