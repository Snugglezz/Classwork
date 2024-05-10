# Isaiah Hensley
# 2024-05-08

# creating an empty list
lst = []

# using a for loop to add the numbers 1-100 to the list
for i in range(1,101):
    lst.append(i)

# printing the list
print(lst)

# create an empty list named odd
odd = []

# using a for loop to add the odd numbers 1-100 to the list odd
for i in range(1,101,2):
    odd.append(i)

# printing the list odd
print(odd)

# creating an empty list named even
even = []

# using a for loop to add the even numbers 1-100 to the list even
for e in range(2,101,2):
    even.append(e)

# printing the list even
print(even)

# create a variable named b that points to the first list that you create
b=lst

# create a variable named joined that joins even and odd lists using a operator
joined = odd + even

# output the variable joined
print(joined)

# output the type of the joined variable
print(type(joined))

# compare the list b to the list joined using positional comparaison
print(b == joined)