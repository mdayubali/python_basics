# Everyting is in python class object
# class name will be CamelCase
# Use can use with () or without ()
# you can use the pass keyword to avoid getting errors in empty statement because empty state is not allowed in loop, class, function eventhough in if statement. Using pass keyword you can this for future
class Sample():
        # pass
        # Class object 
        full_name = "Md Ayub Ali"
        # instance creation
        # self if used to access the attributes
        def __init__(self,age,profession): 
                # attribute
                self.age = age
                self.profession  = profession
       
result = Sample(26,profession="Web Developer")

print(f"I am {result.age} years old, and I am professional {result.profession} ")
