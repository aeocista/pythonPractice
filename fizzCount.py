# Write your function below!
def fizz_count(x):
  count = 0
  for item in x:
    if item == "fizz":
      count = count + 1
  return count

lotto = [4, 8, 'fizz', 'fizz', 23, 42]
lotto_fizz_count = fizz_count(lotto)
print lotto_fizz_count