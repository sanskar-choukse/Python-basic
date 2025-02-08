i=1
while(i<=5):
    if(i==3):
     break
    print(i)
    i+=1
        

# Q.search for a number X  in this tuple using loop
# (1,2,4,16,25,36,49,64,81,100)

num=(1,2,4,16,25,36,49,64,36,81,100)

X=36

ind=0
while(ind<len(num)):
   if(num[ind]==X):
        print("found",ind)
        break
   else:
      print("finding")
   ind+=1 