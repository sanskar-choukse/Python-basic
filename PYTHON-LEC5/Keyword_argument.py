# Keyword argument=An argument proceded by an identifier 
#                  helps with readabiltiy
#                 order of arguments does't Matter
#                 1.position 2.default 3.keyword 4.arbitrary

def hello(greeting,title,firts,last):
    print(f"{greeting} {title} {firts} {last}")


# sequntely is compulsary
hello("hello","Mr","Sanskar","Chouksey") 

# order of arguments does't Matter
hello(greeting="hii",last="Chouksey",firts="Sanskar",title="Mr.")


def get_phone(country,area,firts,second):
    # print(f"{country}-{area}-{firts}-{second}")
    # or
    return f"{country}-{area}-{firts}-{second}"
get_phone("1","123","456","789")
get_phone("91","73","896","11006")
# or
print(get_phone("1","123","456","789")) 