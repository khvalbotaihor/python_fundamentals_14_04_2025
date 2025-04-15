dict = {"key": "value"}  # key can be a string , an integer or a float
# value can be anything

a = {"name": "John", "age": 30, "city": "New York", "internal_dic": {"key1": "value1", "key2": "value2"}}

print(a)



name = 'Max'
age = 67
temperature=36.6
email= "example@test.com"
name_4_test = 'gggg'


my_info = {'name': 'ihor', 'age': 67,}

print(my_info.values())
print(my_info.pop('age'))
print(my_info)

print(my_info.get('name'))
print(my_info.update({'address':'test'}))

print(my_info)  # None

print(my_info.popitem())  # remove item from dictionary
print(my_info)  # None
print(my_info.update({'address':'test'}))  # add item to dictionary
print(my_info)  # None  
print(my_info.keys())