#Code block 1
v1 = 4567898
v2 = 3490234
v3 = 3456789
prc = v1 * v2 * v3
print('The product of the values is', prc)
#Print output to console

#Code block 2
a1 = 13456790
a2 = 23423409
a3 = 31256890
asum = a1 + a2 + a3
print(asum)
#Print output to console

#Code block 3
abc1 = 7645670
abc2 = 7756932
abc3 = 7812356
asub = abc1 - abc2 - abc3
print('The final result of compute operation is', asub)

#Code block 4
a = 41289707
c = 35423808
f = 75645130
j = 82367823
p = 103344303
allcomp = a + c - f / j * p
print('Result value is-', allcomp)
#Print output to terminal

#Code block 5
engcc = 998
if engcc > 1000:
    print('The car falls in tax cat c')
elif engcc == 1000:
    print('The car falls in tax cat b')
elif engcc < 1000:
    print('The car falls in tax cat a')
#Print output to terminal for user

#Code block 12
# List of values to compare
values = [12, 45, 67, 88, 74, 54, 66, 56]

# Loop through each value and compare with 10
for value in values:
    if value < 10:
        print('Value is less than 10')
    elif value == 10:
        print('Value is equal to 10')
    else:
        print('Value is greater than 10')
    #Print output to console



    #Code block 15655
    values = [1498, 1356, 1096, 999, 1890, 2855, 1598, 2970]
    for value in values:
        if value > 1200:
            print('This is a high end model')
        elif value == 1200:
            print('This is a mid segment model')
        else:
             print('This is a low end model')
     #Print output to terminal

     #Code block 6577
     # List of values
values = [12, 45, 67, 88, 74, 54, 66, 56]

# Find the largest value
largest_value = max(values)

# Print the largest value
print(f"The largest value is: {largest_value}")


#Code block 4433
valus = [23, 45, 67, 87, 24, 90, 65, 41, 43, 84, 73, 94]
smallest_value = min(valus)
print('The smallest value in the list is:', smallest_value)
#Print output to console

#code

import random
import csv

# Parameters for random data
num_rows = 10        # Number of rows
num_columns = 5      # Number of columns
min_value = 1        # Minimum random integer
max_value = 100      # Maximum random integer

# Output file name
output_file = "random_integers.csv"

# Generate and write random integers to the CSV file
with open(output_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    
    # Optional: Write header
    writer.writerow([f"Column {i+1}" for i in range(num_columns)])
    
    # Write rows of random data
    for _ in range(num_rows):
        row = [random.randint(min_value, max_value) for _ in range(num_columns)]
        writer.writerow(row)

print(f"Random integers written to {output_file}.")


#code 23213
import csv

# Specify the file path
file_path = "random_integers.csv"

# Open and read the CSV file
with open(file_path, mode='r') as file:
    reader = csv.reader(file)
    
    # Print each row in the CSV file
    for row in reader:
        print(row)



#Code 5578
row1 = [231, 451, 341, 461, 641, 521, 391, 471, 331, 531]
for value in row1:
    if value > 326:
        print('It falls in category a')
    elif value == 326:
        print('It falls in category b')
    else:
        print('It falls in category c')
    #Print output to console

#Code 4426
ages = [36, 38, 40, 69, 64, 63, 35, 34]
youngest_element = min(ages)
#Print output to console
print('The youngest element is-', youngest_element)

#Code block 378
brandcxs = [93, 91, 94, 88, 89, 87, 90, 92, 95, 87, 85]
for score in brandcxs:
    if score > 90:
        print('Score is in green')
    elif score ==90:
        print('Score is in orange')
    else:
        print('Scor is in red')
#Print output to console


#Code 26
brandcxs = [93, 91, 94, 88, 89, 87, 90, 92, 95, 87, 85]
lscr = min(brandcxs)
#Print lowest score to console
print('The lowest score for fortnight is', lscr)

#Code 28
brandcxs = [93, 91, 94, 88, 89, 87, 90, 92, 95, 87, 85]
hscr = max(brandcxs)
#Print highest score to console
print('The highest score for fortnight is', hscr)

#Code block 081030
brandcxs = [93, 91, 94, 88, 89, 87, 90, 92, 95, 87, 85]
mean_value = sum(brandcxs) / len(brandcxs)
#Print output to console
print('The mean value for brandcx for fortnight is', mean_value)

#Code 32-0810
calval = [430, 510, 480, 550, 470, 460, 550, 590, 990, 810]
for value in calval:
    if value < 600:
        print('You are undernourished')
    elif value == 600:
        print('You are on borderline')
    else:
        print('You are high on intake')
    #Print output to console


#Code 34-0810
mygoal = 'Put a dent here in the universe'
print('My life goal is-', mygoal)


#Code 35-0810

mol = 'Create best products in the world'
print('The goal of minimal is to', mol)
#Print output to console


#Code 37-0810
sdm = [434, 387, 362, 426, 394, 403, 608, 483, 451, 383]
for score in sdm:
    if score > 401:
        print('Move to cola')
    elif score == 401:
        print('Move to colb' )
    else:
        print('Move to colc')
#Print output to console

#Code 39-0810
str1 = [23, 24, 26, 21, 33, 30, 36, 42, 55, 51, 43, 20, 35, 42, 49, 55, 51, 57, 47, 46, 44, 47, 36, 33]
least_val = min(str1)
#This will return the smallest value in the list
print('The smallest value in the string is', least_val)


#Code 41-0810
str1 = [23, 24, 26, 21, 33, 30, 36, 42, 55, 51, 43, 20, 35, 42, 49, 55, 51, 57, 47, 46, 44, 47, 36, 33]
largest_v = max(str1)
#Display largest value as output
print('The largest value in the string is', largest_v)


#Code 43-0810
str01 = [23, 24, 26, 21, 33, 30, 36, 42, 55, 51, 43, 20, 35, 42, 49, 55, 51, 57, 47, 46, 44, 47, 36, 33, 51, 63, 78, 62]
#Compute the mean
mean_str01 = sum(str01) / len(str01)
#Print output to console
print('The mean of this string is', mean_str01)

#Code 47-0810
dcb = 96
while dcb < 55001:
    print(dcb)
    dcb = dcb * 1.15
#Print output to console

#Code 53-0810
def fxttv(ter1, ter2, ter3, ter4, ter5, ter6, ter7):
    return ter1 + ter2 + ter3 + ter4 + ter5 + ter6 + ter7
ttv = fxttv(6545000, 7693000, 7934500, 11040200, 6632900, 7132300, 9543900)
#Print output to console
print('The value of the total tx value is', ttv)

#Code 56-0810
idv = 389550
if idv < 400000:
    print('Premium will be in cat a')
elif idv >= 400000:
    print('Premium will be in cat b')
#Print output to console






