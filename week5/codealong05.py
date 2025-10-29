# Enter a list of numbers, type 0 when finished.
# Enter number: 18
# Enter number: 36
# Enter number: 2
# Enter number: 48
# Enter number: 6
# Enter number: 12
# Enter number: 9
# Enter number: 0
# The sum is: 131
# The average is: 18.714285714285715
# The largest number is: 48

num_list = []
counter = ""


def enter_numbers():
    num_list = []
    counter = ""
    while counter != 0:
        counter = input("Enter number: ")
        while not counter.isnumeric():
            counter = input("Please enter a number: ")
        counter = int(counter)
        if counter != 0:
            num_list.append(counter)
    return num_list

# num_list = [3, 4, 5]

# sum_list = sum(num_list)


# another_sum = 0
# for i in num_list:
#     another_sum += i

# print(sum_list)
# print(another_sum)

# counter = 0
# sum_list = 0

# for item in num_list:
#     counter +=1
#     sum_list += item

# print(sum_list / counter)

