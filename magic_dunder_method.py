class Sample:
    pass 

s = Sample()
#len(s)

class Book:

  def __init__(self,title, author, pages):
    self.title = title 
    self.author = author 
    self.pages = pages

  def __str__(self):
    return f"{self.title} by {self.author}"

  def __len__(self):
    return self.pages

  def __repr__(self):
    pass 

  def __eq__(self):
    pass

  def __del__(self):
    print("a book object has been deleted!")

b = Book("python rock", "Jose", 200)
print(b)

del b # deletes the book and print a special message