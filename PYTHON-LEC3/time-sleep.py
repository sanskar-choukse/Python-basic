import time

# time.sleep(3)
# print("Mahadev")

# # matlab kitne time badh print kerna ha
# time.sleep(5)
# print("radhe radhe")

# time.sleep(7)
# print("radhe krishna") 

# time.sleep(10)
# print("Jai shree mahakal")

# @@ WATCH 
my_time=int(input("Enter the  Time"))

for count in range(my_time,0,-1):
      second=count%60
      minutes=int(count/60)%60
      hours=int(count/3600)
      print(f"{hours:02}:{minutes:02}:{second:02}")
      time.sleep(1)

      