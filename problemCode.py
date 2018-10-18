# Getting a none?
n = [3, 5, 7, 8]

def print_list(x):
  for i in range(0, len(x)):
    print x[i]
  return

# The problem was here:
print print_list(n)

# Should do this instead:
print_list(n)

# Double your list!
n = [3, 5, 7]

# Don't forget to return your new list!
def double_list(x):
  for i in range(0, len(x)):
    x[i] = x[i] * 2
  return x

print double_list(n)

# Ranges are a lot like lists

# range(6) # => [0, 1, 2, 3, 4, 5]
# range(1, 6) # => [1, 2, 3, 4, 5]
# range(1, 6, 3) # => [1, 4]

def my_function(x):
  for i in range(0, len(x)):
    x[i] = x[i]
  return x

print my_function(range(0,3)) # Add your range between the parentheses!

# The sum of a list
n = [3, 5, 7]

def total(numbers):
  result = 0
  for i in range(len(numbers)):
    result = result + numbers[i]
  return result
    