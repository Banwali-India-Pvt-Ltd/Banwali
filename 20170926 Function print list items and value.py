#Function for print list value and Index value together
n = [3, 5, 7]
def print_list(x):
    for i in range(0, len(x)):
        num = i
        print num, x[i]
print_list(n)

n = [3, 5, 7]
def double_list(x):
    for i in range(0, len(x)):
        x1 = x[i]
        print x1*2

print double_list(n)

#Function for print list item double
n = [3, 5, 7]
def double_list(x):
    for i in range(0, len(x)):
        x[i] = x[i] * 2
    return x
# Don't forget to return your new list!

print double_list(n)

#Function for replace a list between a range
def my_function(x):
  for i in range(0, len(x)):
    x[i] = x[i] * 2
  return x

print my_function(range(8)) # Add your range between the parentheses!

#function for add list items through loop
n = [0, 3, 6]

def total(numbers):
  result=0
  for i in range(0,len(numbers)):
    result += numbers[i]
  return result

#Function for concetnate a list items
n = ["Michael", "Lieberman"]
# Add your function here
def join_strings(words):
  result=""
  words.append("")
  result = ''.join(map(str, words))
  return result

print join_strings(n)

#Function for concatenate tow integer list
m = [1, 2, 3]
n = [4, 5, 6]

# Add your code here!
def join_lists(x,y):
    join_lists = x+y
    return (join_lists)

print join_lists(m, n)
# You want this to print [1, 2, 3, 4, 5, 6]

#Function for add list and sublist in a seprate list
n = [[1, 2, 3], [4, 5, 6, 7, 8, 9]]
# Add your function here

def flatten(lists):
  results = []
  for numbers in lists:
    for number in numbers:
      results.append(number)
  return results

print flatten(n)