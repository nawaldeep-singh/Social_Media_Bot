from instabot import Bot
import operations as op
import cli_format as clif
import os
import network
from tkinter import filedialog as dbox
import shutil as sh
import clear_temp as ct

temp_resource = (os.getcwd().replace("\\","/"))+"/resources/images"

def MediaBot(credentials):
    for media_info in credentials:
        if media_info[0].lower() == "instagram":
            check = network.isConnected()
            
            if check == True:
                print("Connecting To Bot",end="")
                clif.dot()
                print("Logging in to Instagram",end="")
                clif.dot()
                ibot = Bot()
                ibot.login(username = media_info[1],password = media_info[2])
                print("What operation you want to do ?")
                ilist = op.getinsta()

                #-------remove afterwords---------
                print(ilist)
                #-------remove afterwords---------

                for opr in ilist:
                    if '1' in opr:
                        count = int(input("How many Pics you want to upload ? : "))
                        for i in range(0,count):
                            print(f"Select Image {i+1}",end=" ")
                            clif.dot()
                            path = dbox.askopenfilename(initialdir=os.getcwd(), title='Select Photo', filetypes= ( ('JPEG File', '*.jpg'),('PNG File', '*.png'),('BMP File', '*.bmp'),('RAW File', '*.nef'), ('All Files', '*.*') ) )
                            sh.copy(path,temp_resource)
                            file = path.split("/")

                            file_path = temp_resource + "/" + file[-1]
                            print("file path : ",file_path)
                            cap = input("Enter the caption : ")
                            ibot.upload_photo(file_path, caption = cap)

                            #------------------------------------
                            #file_path = file_path + ".REMOVE_ME"  # not a good idea 
                            #-------------------------------------
                            print("temp res. dir = ",temp_resource)
                            ct.clr_dir(temp_resource)
                            #sh.rmtree((os.getcwd().replace("\\","/"))+'/__pycache__',ignore_errors=True)
                            #sh.rmtree((os.getcwd().replace("\\","/"))+'/config',ignore_errors=True)
                            try:
                                ct.clr_dir((os.getcwd().replace("\\","/"))+'/__pycache__')
                                ct.clr_dir((os.getcwd().replace("\\","/"))+'/config/log')
                                ct.clr_dir((os.getcwd().replace("\\","/"))+'/config')
                            
                            except:
                                return
                            
                            
                #idict = {1 : "ibot.upload_photo()", 2 : "upload_story_photo", 3 : 
                # "upload_video", 4 : "follow", 5 : "like"}



            
        elif media_info[0].lower() == "whatsapp":
            print("wahtsapp not supported")
            pass
                

        else:
            print("""Some technical issue occur...
            Program and database corrupted
            Repairing database...""")
            os.startfile("repair.py")