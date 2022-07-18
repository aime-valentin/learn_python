#lambda: unnamed function for one-time use
#map function: maps a function to an iterator
#filter function: returns an iterator created by a filter function that return true or false

#MAP
def square(a):
  return a**2

some_list = [1,2,3,4,5]

squares = list(map(square, some_list)) #when passing in function, you do not call the function, instead you just pass in the name of the function. 

print(squares)

def splicer(mystr):
  if len(mystr)%2 ==0:
    return 'EVEN'
  else:
    return 'ODD'

some_list = ['andy', 'eve', 'saly']
print(list(map(splicer,some_list)))

## FILTER
def check_even(num):
  return num%2 ==0

some_list = [1,2,3,4,5,6,7,8,9,10]
print(list(filter(check_even, some_list))) #check_even function must  return 1/0 true/false

#LAMBDA: some functionality intended to use on time
def square(n):
  return n**2 

#transform the above function to a lambda function
#lambda num: num**2 and this can actually be assigned to a variable square = lambda num: num**2

squares = list(map(square, some_list))
squares = list(map(lambda num:num**2, some_list))

