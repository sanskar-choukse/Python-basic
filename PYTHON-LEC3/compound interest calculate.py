# A=p(1+r/n)t
# A=final amount
# p=initial principal balance
# r=intrest rate
# t=number of time periods


# principle = 0
# rate = 0
# time = 0

# while principle<=0:
#     principle=float(input("Enter the principle"))
#     if  principle <= 0:
#         print("principle can't be lessthan or equal to zero")
    

# while rate<=0:
#     rate= float(input("Enter the rate"))
#     if rate<=0:
#         print("rate can't be lessthan or equal to zero")

# while time<=0:
#     time= float(input("Enter the time"))
#     if time<=0:
#         print("time can't be lessthan or equal to zero")
    

#     print(principle)
#     print(rate)
#     print(time)

# total=principle*pow((1+rate/100),time)
# print(f"Balance after {time} year/s:${total:.2f}")

# (OR)

while False:
    principle=float(input("Enter the principle"))
    if  principle <= 0:
        print("principle can't be lessthan or equal to zero")
    else:
        break

while True:
    rate= float(input("Enter the rate"))
    if rate<=0:
        print("rate can't be lessthan or equal to zero")
    else:
        break

while True:
    time= float(input("Enter the time"))
    if time<=0:
        print("time can't be lessthan or equal to zero")
    else:
        break

    print(principle)
    print(rate)
    print(time)

total=principle*pow((1+rate/100),time)
print(f"Balance after {time} year/s:${total:.2f}")