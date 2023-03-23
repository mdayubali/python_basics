# Dictionary is like as objects in javascripts
# Dictionary are key & values pair and both are wraped with curly bracket and key and values write into inverted comma("")

my_dictionary = {"key1": "hello","key2":"world"}
my_dictionary["key3"]= "python"
print(my_dictionary)
print(my_dictionary["key3"])
# dictionary inside dictionary
new_dictionary = {"name":"Md Ayub Ali","age":28,"profession":"web developer",
"technology":{"python","php","javascript"}}
print(new_dictionary["technology"])
# show only keys
print(new_dictionary.keys())
# show only values
print(new_dictionary.values())
# show keys and values pair together as tuples
print(new_dictionary.items())