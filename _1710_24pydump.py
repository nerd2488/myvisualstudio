
# Define the three values
num1 = 8.77
num2 = 9.43
num3 = 7.62

# Find the largest and second largest values using sorting
sorted_values = sorted([num1, num2, num3], reverse=True)

# Extract the first two largest values
largest_value, second_largest_value = sorted_values[:2]

# Print the first two largest values
print("The first two largest values are:", largest_value, "and", second_largest_value)


#codeII
# Define the three values
num1 = 8.77
num2 = 9.43
num3 = 7.62

# Find the smallest value using the min() function
smallest_value = min(num1, num2, num3)

# Print the smallest value
print("The smallest value is:", smallest_value)


#code 03
import statistics

# Define the list of values
values = [34, 38, 43, 46, 47, 59, 69, 78, 84, 91]

# Calculate the standard deviation using the statistics.stdev() function
standard_deviation = statistics.stdev(values)

# Print the standard deviation
print("The standard deviation is:", standard_deviation)


#code 7
# Define the list of values
values = [54, 66, 90, 33, 61, 102, 665]

# Sort the values in ascending order using the sorted() function
sorted_values = sorted(values)

# Print the sorted values
print("The values in ascending order are:", sorted_values)


#44
# Define the list of values
values = [334, 75656, 934545, 102, 145, 93, 994, 124545]

# Sort the values in descending order using the sorted() function with reverse=True
sorted_values = sorted(values, reverse=True)

# Print the sorted values
print("The values in descending order are:", sorted_values)



#2233
# Define the list of values
values = [14.33, 13.21, 10.89, 9.94, 11.43, 14.40, 18.54, 11.12]

# Iterate through the values and print those smaller than 8.75
for value in values:
    if value < 8.75:
        print(value)

#code 459
# Define the list of values
values = [14.33, 13.21, 10.89, 9.94, 11.43, 14.40, 18.54, 11.12]

# Iterate through the values and print those greater than 8.75
for v in values:
    if v > 8.75:
        print(value)



# Define the list of values
values = [14.33, 13.21, 10.89, 9.94, 11.43, 14.40, 18.54, 11.12]

# Iterate through the values and print those smaller than 8.75
for value in values:
    if value < 8.75:
        print('value less than 8.75')
    elif value == 8.75:
        print('value equals 8.75')
    else:
        print('value greater than 8.75')
#print output to console


#cd334
val1 = 56.98
val2 = 69.34
val3 = 61.26
minvlue = min(val1, val2, val3)
#print output to console
print('the smallest value in list is', minvlue)

#34tytu
oracle_clock_speed = 6.43
postgresql_clock_speed = 5.47
mysql_clock_speed = 6.92
sqlserver_clock_speed = 6.46
best_clock_speed = min(oracle_clock_speed, postgresql_clock_speed, mysql_clock_speed, sqlserver_clock_speed)
#print output to console
print('the best performance of the group is', best_clock_speed)