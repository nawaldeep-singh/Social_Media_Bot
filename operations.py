import cli_format as clif
from tkinter import filedialog as dbox
import shutil as sh
import os

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
        if (ilist.count(num)>1) or (num < '1' or num > '6'): #deleting the dublicate or invalid values
            ilist.remove(num)

    return ilist #returning ilist to media bot
    

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

def open_file():
    temp_resource = (os.getcwd().replace("\\","/"))+"/resources/images"
    path = dbox.askopenfilename(initialdir=os.getcwd(), title='Select Photo', filetypes= ( ('JPEG File', '*.jpg'),('PNG File', '*.png'),('BMP File', '*.bmp'),('RAW File', '*.nef'), ('All Files', '*.*') ) )
    sh.copy(path,temp_resource)
    file = path.split("/")
    file_path = temp_resource + "/" + file[-1]
    return file_path