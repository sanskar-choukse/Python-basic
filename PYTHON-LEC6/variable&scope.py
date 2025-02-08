# Variable scope=where a variable is visible and accessible 
# scope resolution=(LEGB) Local->Enclosed->Global->built-in

def fun1():
    a=2
    print(a)
fun1()

# def fun2():
#     b=1
#     print(b)
# fun2()

# or
# def fun1():
#     x=2
#     print(x)
# fun1()

# def fun2():
#     x=1
#     print(x)
# fun2()

# or
# def fun1():
#     x=2
#     print(x)
# # fun1()
# def fun2():
#     x=1
#     print(x)
# fun1()
# fun2()

# or

# def fun1():
#     print(x)

# def fun2():
#     print(x)

# x=1
# fun1()
# fun2()

# or

# def fun1():
#     x=2
#     print(x)

# def fun2():
#     x=4
#     print(x)

# x=1
# fun1()
# fun2()

# or 
# whoes rules follow (import e value & variable e value) 
# from math import e 

# def fun1():
#     print(e)

# e=3    
# fun1()