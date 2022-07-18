#user input: whenever you are taking in user inputs, make sure that you validate
def user_input():  
  num = "wrong" #start with what you know is wrong
  while num.isdigit() == False:
    num = input("please enter a number between 0-10: ") #ask for input that is not wrong until you get it
  return num
num = user_input()

#validation: 
  #come up with a list of corner cases 
  #make sure that you handle each corner cases
  #start with what you do not want and eliminate that from user inputs




