numbers = [1, 2, 3, 4]

#new_list = [new_item for item in list]

new_numbers = [n + 1 for n in numbers]

print(new_numbers)

name = "Yousiff"

letter_list = [l for l in name]

print(letter_list)

doubles = [n * 2 for n in range(1, 5)]

print(doubles)

#tested_list = [new_item for item in list if test]

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

upper_names = [name.upper() for name in names if len(name) > 4]

print(upper_names)