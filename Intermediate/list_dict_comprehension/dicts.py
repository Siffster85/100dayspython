import random

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

#new_dict = {new_key:new_value for item in list}
#same as list, go through an iterable and create a dict

scores = {student:random.randint(1,100) for student in names}
print(scores)

#new_dict = {new_key:new_value for (key,value) in dict.items()}
#go through a dict and extract the keys and values

#new_dict = {new_key:new_value for (key,value) in dict.items() if test}
#as above but adding a test condition

passed_students = {student:score for (student,score) in scores.items() if score >= 60}
print(passed_students)

