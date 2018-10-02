num_list = [9, 7, 8, 1, 3, 6, 5, 2, 4]

for i in range(len(num_list)):
    for j in range(len(num_list) - 1):
        if num_list[j] > num_list[j + 1]:
	        num_list[j], num_list[j + 1] = num_list[j + 1], num_list[j]
print(num_list)

# for i in range(len(num_list)):
#     if i 
