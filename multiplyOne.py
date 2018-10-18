# MANIPULATING LISTS

# Modify an element of n
n = [1, 3, 5]
# Do your multiplication here
n[1] = 3 * 5
print n

# Append an element to n
n = [1, 3, 5]
# Append the number 4 here
print n
n.append(4)

# Remove an element of n
n = [1, 3, 5]
# Remove the first item in the list here
n.remove(1)
print n

# Multiply by 3
number = 5

def my_function(x):
  return x * 3

print my_function(number)

# Add arguments x and y
m = 5
n = 13
# Add add_function here!
def add_function(x,y):
  return x + y

print add_function(m, n)

# Print only one index of a list
def list_function(x):
  return x[1]

n = [3, 5, 7]
print list_function(n)

# Modify one element in a list with a function

def list_function(x):
  x[1] = x[1] + 3
  return x

n = [3, 5, 7]
print list_function(n)

# Append a list with a function
n = [3, 5, 7]
# Add your function here
def list_extender(lst):
  lst.append(9)
  return lst

print list_extender(n)