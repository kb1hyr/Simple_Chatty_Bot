# put your python code here
first_class = int(input())
second_class = int(input())
third_class = int(input())

desks_first = int((first_class/2)) + (first_class % 2)
desks_second = int((second_class/2)) + (second_class % 2)
desks_third = int((third_class/2)) + (third_class % 2)
total_desks = desks_first + desks_second + desks_third
print(total_desks)

