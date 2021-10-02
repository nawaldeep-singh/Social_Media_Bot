import cli_format as clif

def getinsta():
    print("Retrieving Instagram Operations",end="")
    clif.dot()
    print("""
    1 : Upload a Photo
    2 : Upload a Story
    3 : Upload a Video
    4 : Follow Someone
    5 : Like photo(s)
    6 : Send Message 
    """)

    ilist = input("Enter the respective numbers (seprated by \",\") : ").split(",")
    ilist.sort()
    for num in ilist:
        if ilist.count(num)>1:
            ilist.remove(num)

    return ilist
    

def getfb():
    print("""
    1 : Upload a Photo
    2 : Follow Someone
    3 : Like photo(s) 
    """)

def gettwitter():
    print("""
    1 : Upload a Photo
    2 : Follow Someone
    3 : Like photo(s) 
    """)

