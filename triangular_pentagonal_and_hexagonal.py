""" Triangular, pentagonal and hexagonal """
# import time module for calculate the time of operation
import time

start = time.time()
# tri_list for calculated triangular numbers
tri_lst = []
# pent_list for calculated pentagonal numbers
pent_lst = []
# hex_list for calculated hexagonal numbers
hex_lst = []

i = 1
num = 1
last_digit = 2000000000
# while loop for calculate triangular numbers
while num < last_digit:
    num = i * (i + 1) / 2
    if num < last_digit:
        tri_lst.append(int(num))
    i += 1


i = 1
number = 1
# while loop for calculate pentagonal numbers
while number < last_digit:
    number = i * (3 * i - 1) / 2
    if number < last_digit:
        pent_lst.append(int(number))
    i += 1


i = 1
numbers = 1
# while loop for calculate hexagonal numbers
while numbers < last_digit:
    numbers = i * (2*i - 1)
    if numbers < last_digit:
        hex_lst.append(int(numbers))
    i += 1

# same_values list for select value in above three list
same_values = []
for i in tri_lst:
    if i == 1:
        pass
    else:
        if i in pent_lst:
            if i in hex_lst:
                same_values.append(i)
# tri_count_list for count the position of same values in tri_list
tri_count_lst = []
for i in same_values:
    tri_count = 0
    for j in tri_lst:
        tri_count += 1
        if i == j:
            tri_count_lst.append(tri_count)

# pent_count_list for count the position of same values in pent_list
pent_count_lst = []
for i in same_values:
    pent_count = 0
    for j in pent_lst:
        pent_count += 1
        if i == j:
            pent_count_lst.append(pent_count)

# hex_count_list for count the position of same values in hex_list
hex_count_lst = []
for i in same_values:
    hex_count = 0
    for j in hex_lst:
        hex_count += 1
        if i == j:
            hex_count_lst.append(hex_count)


print("Tri(", tri_count_lst[0], ") = Pent(", pent_count_lst[0], ") = Hex(",hex_count_lst[0], ") =", same_values[0])
print("Tri(", tri_count_lst[1], ") = Pent(", pent_count_lst[1], ") = Hex(",hex_count_lst[1], ") =", same_values[1])
end = time.time()
print(f"Time :{end - start}")
