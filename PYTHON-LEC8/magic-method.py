# magic methods=It's also knoes as Dunder methods(double underrscore) __int __,__str__,__eq__
#               they are automatically called by many of python's built-in operation.
#               they allow developers to define or customize the behavior  of objects


class book:
    def __init__(self,title,author,num_pages):
        self.title=title
        self.author=author
        self.num_pages=num_pages

    def __str__(self):
        return f"{self.title} by {self.author}"
    
    # check 2 object equal to each other  
    def __eq__(self,other):
        return self.title==other.title and self.author==other.author and self.num_pages==other.num_pages

    #lt fun use for chack the value(lessthan(<)) 
    def __lt__(self,other): 
        return self.num_pages<other.num_pages 

    #gt fun use for check the value(greaterthan)
    def __gt__(self,other):
        return self.num_pages>other.num_pages
    
    #add fun use for add 2 object value
    def __add__(self,other):
        return f"{self.num_pages+other.num_pages} pages"
    
    # def  check key and these value is present and not in key 
    def __contains__(self,key):
        return key in self.title or  key in self.author
  
    #check values
    def __getitem__(self,key):
        if key == "title":
          return self.title
        elif key=="author":
            return self.author
        elif key=="num_pages":
            return self.num_pages
        else:
            return f"key {key} was not found"
book1=book("the grade","sanskar-kalal",123)
book2=book("The beautifull","krishna",231)
book3=book("The break-to-heart","minati",221)
book4=book("the grade","sanskar-kalal",123)

# print ho raha ha str ke hisab se 
# print(book1)

#(eq) function use for 2 object check the value is equal
# print("check value is equal to other")
# print(book1==book2)
# print(book1==book4)

# (lt) function use for 2 object check the value is lessthan
# print("check value is lessthan to other")
# print(book1<book2)
# print(book2<book1)

# (gt) function use for 2 object check the value is greaterthan
# print("check value is Greaterthan to other")
# print(book1>book2)
# print(book2>book1)

# (add) function use for (add) 2 object
# print("add to other object value")
# print(book1+book2)
# print(book2+book3)


# check key and these value present in the key so use  (__contains__) function
# print("the grade" in book1) 
# print("the grade" in book2) 
# print("The beautifull" in book2) 
# print("krishna" in book2) 


# check items in object use fun(__getitem__) 
print(book1["title"])
print(book2["title"])
print(book1["author"])
print(book3["author"])
print(book1 ["num_pages"])
print(book2["titlessss"])