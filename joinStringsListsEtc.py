# join_strings

n = ["Michael", "Lieberman"]
# Add your function here
def join_strings(words):
  result = ""
  for i in range(len(words)):
    result = result + words[i]
  return result

print join_strings(n)

# join_lists

m = [1, 2, 3]
n = [4, 5, 6]

# Add your code here!
def join_lists(x,y):
  result = x + y
  return result

print join_lists(m, n)
# You want this to print [1, 2, 3, 4, 5, 6]

# flatten_lists

n = [[1, 2, 3], [4, 5, 6, 7, 8, 9]]
# Add your function here

def flatten(lists):
  results = []
  for numbers in lists:
    for number in numbers:
      results.append(number)
  return results

print flatten(n)