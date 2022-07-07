import sys

num_array = [45, 12, 85, 32, 89, 39, 69, 44, 42, 1, 6, 8]

for i in range(len(num_array)):
    for j in range(i, 0, -1):
        if num_array[j] < num_array[j-1]:
            temp = num_array[j]
            num_array[j] = num_array[j-1]
            num_array[j-1] = temp

print(num_array)