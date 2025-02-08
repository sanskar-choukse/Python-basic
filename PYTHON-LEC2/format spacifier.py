# format spacifier={value :flags}format a value based on what  
#                  flags are inserted

#1 .(number)f=round to that many decimal places(fixed point)
#2 :(number)=allocate that many spaces
#3 :03=allocate and zero pad that many spaces 
#4 :< = left justify
#5 :> = right justify
#6 :^ = center align
#7 :+=use a plus sign to indicate positive value
#8 := = place sign to leftmost postive
#9 :  = insert a space before postive number
#10:, =comma separator 

# (.)(number)f=round to that many decimal places(fixed point)
Price1=30000.14159
price2=-98700.65
price3=1200.34

print(f"price 1 is ${Price1:.2f}")
print(f"price 2 is ${price2:.2f}")
print(f"price 3 is ${price3:.2f}")

# (number)=allocate that many spaces

print(f"price 1 is ${Price1:10}")
print(f"price 2 is ${price2:10}")
print(f"price 3 is ${price3:10}")

# 03=allocate and zero pad that many spaces 
print(f"price 1 is ${Price1:010}")
print(f"price 2 is ${price2:010}")
print(f"price 3 is ${price3:010}")

# (or)

print(f"price 1 is ${Price1:010.2f}")
print(f"price 2 is ${price2:010.2f}")
print(f"price 3 is ${price3:010.2f}")

# < = left justify
print(f"price 1 is ${Price1:<10}")
print(f"price 2 is ${price2:<10}")
print(f"price 3 is ${price3:<10}")

#:> = right justify
print(f"price 1 is ${Price1:>10}")
print(f"price 2 is ${price2:>10}")
print(f"price 3 is ${price3:>10}")

#:^ = center align
print(f"price 1 is ${Price1:^10}")
print(f"price 2 is ${price2:^10}")
print(f"price 3 is ${price3:^10}")

# +=use a plus sign to indicate positive value
print(f"price 1 is ${Price1:+}")
print(f"price 2 is ${price2:+}")
print(f"price 3 is ${price3:+}")


# :, =comma separator 
print(f"price 1 is ${Price1:,}")
print(f"price 2 is ${price2:,}")
print(f"price 3 is ${price3:,}")

print(f"price 1 is ${Price1:,.1f}")
print(f"price 2 is ${price2:,.1f}")
print(f"price 3 is ${price3:,.1f}")