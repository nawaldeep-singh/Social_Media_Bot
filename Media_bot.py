from instabot import Bot
import operations as op
import cli_format as clif
import os
import network
import shutil as sh
import clear_temp as ct



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

                temp_resource = (os.getcwd().replace("\\","/"))+"/resources/images"
                
                for opr in ilist:
                    if '1' in opr:
                        count = int(input("How many Pics you want to upload ? : "))
                        for i in range(0,count):
                            if count == 1:
                                print(f"Select Image ",end=" ")
                                clif.dot()
                            else:
                                print(f"Select Image {i+1}",end=" ")
                                clif.dot()

                            file_path = op.open_file()
                            print("file path : ",file_path)
                            cap = input("Enter the caption : ")
                            ibot.upload_photo(file_path, caption = cap)

                            #------------------------------------
                            #file_path = file_path + ".REMOVE_ME"  # not a good idea 
                            #-------------------------------------
                            print("temp res. dir = ",temp_resource)
                            ct.clr_dir(temp_resource)
                            
                            try:
                                ct.clr_dir((os.getcwd().replace("\\","/"))+'/__pycache__')
                                ct.clr_dir((os.getcwd().replace("\\","/"))+'/config/log')
                                ct.clr_dir((os.getcwd().replace("\\","/"))+'/config')
                            
                            except:
                                sh.rmtree((os.getcwd().replace("\\","/"))+'/__pycache__',ignore_errors=True)
                                sh.rmtree((os.getcwd().replace("\\","/"))+'/config',ignore_errors=True)
                                sh.rmtree((os.getcwd().replace("\\","/"))+'/config/log',ignore_errors=True)
                                

                    elif '2' in opr:
                        count = int(input("Enter the number of stories you want to post ? : "))
                        
                        for i in range(0,count):
                            if count == 1:
                                print(f"Select Image ",end=" ")
                                clif.dot()
                            else:
                                print(f"Select Image {i+1}",end=" ")
                                clif.dot()

                            file_path = op.open_file()
                            ibot.upload_story_photo(file_path)

                    elif '3' in opr:
                        print("This option is not available yet",end="")
                        clif.dot()
                        pass
                            
                            
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