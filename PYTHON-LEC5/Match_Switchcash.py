# # match_case Statement(switch):an Alternartiveto using many "elif" statement 
# #                              :Executive some code if a  value matches  a 'case'
# #                              Benefits:cleanner and syntax is more readable 

def day_of_week(day):
    if day==1:
        return "It is Sunday"
    elif day==2:
        return "It is Monday"
    elif day==3:
        return "It is tuesday"
    elif day==4:
        return "It is wednesday"
    elif day==5:
        return "It is thuesday"
    elif day==6:
        return "It is Friday"
    elif day==7:
        return "It is sunday"
    
   
print(day_of_week(1))

# or without if and else

# def day_of_week(day):
#     match day:
#        case 1:
#         return "It is Sunday"
#        case 2:
#         return "It is Monday"
#        case 3:
#         return "It is tuesday"
#        case 4:
#         return "It is wednesday"
#        case 5:
#         return "It is thuesday"
#        case 6:
#         return "It is Friday"
#        case 7:
#         return "It is sunday"
#        case _: 
#           return "Not a valid day"
       
# print(day_of_week(9))


# def is_week(day):
#     match day:
#        case "Monday":
#         return True
#        case "Tuesday":
#         return False
#        case "Wednesday":
#         return False
#        case "thuesday":
#         return True
#        case "Friday":
#         return True
#        case "Suterday":
#         return False
#        case "Sunday":
#         return True
#        case _: 
#         return "Not a valid day   "
       
# print(is_week("unday"))



# def is_week(day):
#     match day:
#        case "Monday" | "Tuesday":
#         return True
#        case "Tuesday" | "Suterday":
#         return False
#        case "Wednesday" | "thuesday":
#         return False
#        case "thuesday" | "Friday":
#         return True
#        case "Friday" | "Suterday":
#         return True
#        case "Suterday" | "Sunday":
#         return False
#        case "Sunday" | "Monday":
#         return True
#        case _: 
#         return "Not a valid day   "
       
# print(is_week("thuesday"))