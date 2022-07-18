def some_function(a,b):
  #return 5% of the sum of a and b 
  return sum((a,b))*0.05

print(some_function(40,60))

#why use *args: allows to use arbrary number of arguments 
def some_function(*args):
  #all parameters passed in the some_function will create a tuple
  a,b = args
  print(f"a is {a} and b is {b}")
  return sum(args) * 0.05
some_function(1,2)

#why use **kwargs; allows to use arbitrary number of keyworded arguments 
def some_function(**kwargs):
  if "fruit" in kwargs.keys(): 
    print("hooray")
  else:
    print("no fruit")

some_function(fruit = "apple", )

  