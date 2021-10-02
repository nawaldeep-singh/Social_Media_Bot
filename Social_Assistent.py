#--------------------Modules-------------------------------->>>>

import Media_bot as mb
import db_space as dbs
import time
import cli_format as clif
import os
#------------------------------------------------------------->>>>

#--------------------Functions-------------------------------->>>>

try:
    def add_platforms():
        plist_input = input("select the platforms using thier respective number seprated by comma (,) : ").replace(" ","")
        #if plist_input.count(",") > 0: error
        plist_input = plist_input.split(",")
        allmedia = dbs.media_available()


        for index in range(0,len(plist_input)):
            if plist_input[index].isnumeric() == True:
                plist_input[index] = int(plist_input[index])

            elif plist_input[index].isnumeric() == False:
                plist_input.remove(plist_input[index])


        if len(plist_input) == 0:
            print("No valid value")
            print("Please restart the program")
            print("Closing",end="")
            clif.dot(value = 3, sec = 0.2)
            exit()

        plist = []
        for i in plist_input:
            plist.append(allmedia[i-1])

        return plist

    def clearConsole():
        command = 'clear'
        if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
            command = 'cls'
        os.system(command)

    def login_info(workspace_name):
        '''takes workspace name and platform list and returns list of all platforms login id and password list '''
        
        
        workspace_info =[] #lists of different login data

        platform = dbs.get_platforms(workspace_name)

        for social_media in platform:
            login_details = [] #reset list to empty
            login_data = [] #platform, user_id and password
            login_data.append(social_media)
            print()
            print(f"Passing social media as {social_media}",end="")
            clif.dot()
            login_details = dbs.get_login(workspace_name, social_media)

            if login_details[0] != None:
                login_data.append(login_details[0])

                if login_details[1] != None:          
                    login_data.append(login_details[1])

                    print(f"{social_media} credentials found",end="")
                    clif.dot()


                else:
                    print(f"Logging in to {social_media}",end="")
                    clif.dot()
                    print(f"\nLogin ID : {login_details[0]}")
                    password = input("Enter your password : ").replace(" ","")
                    login_data.append(password)

                    choice = input("Do you want to save password securely? (y for 'yes' else 'no') : ").lower()

                    if choice in ['y','yes']:
                        dbs.save_data(workspace_name, login_data)

                    else:
                        print("Your password won't save",end="")
                        clif.dot()
                    print() 
            
            else:
                no_pass_save = []
                no_pass_save.append(social_media)
                print(f"\nLogging in to {social_media}",end="")
                clif.dot()
                loginID = input("Enter your Login ID : ").replace(" ","")
                login_data.append(loginID)
                no_pass_save.append(loginID)
                password = input("Enter your password : ").replace(" ","")
                login_data.append(password)
                no_pass_save.append(None)
                

                choice = input("Do you want to save/overwrite password securely? (y for 'yes' else 'no') : ").lower()

                if choice in ['y','yes']:
                    dbs.save_data(workspace_name, login_data)

                else:
                    dbs.save_data(workspace_name, no_pass_save)
                    print("Your password won't save",end="")
                    clif.dot()

            
            workspace_info.append(login_data)
        
        return workspace_info


except:
    print("Some Error occur due to your input or some technical issue...")
    print("Please restart the program")
    clif.dot()

    print("program died")
    

#---------------------------------------------------------------->>>>

#--------------------Program Logic-------------------------------->>>>


dbs.list_ws()

workspace = input("Enter the name of Workspace : ").lower()
start = True

while start == True:

    if dbs.isAvailable(workspace) == True:

        start = False
    
        print(f"{workspace.capitalize()} Workspace Available",end="")
        clif.dot()
        choice = None
        restart = False
        while choice not in ['y','yes','o',"overwrite"] or restart == True:
        
            if restart != True:      
                choice = input(f"""\nDo you want to use \"{workspace.capitalize()}\" workspace ?
                \n -> 'y' to 'USE THIS WORKSPACE'
                \n -> 'o' to 'OVERWRITE'
                \n -> 'e' to 'EXIT'
                \n Choice (y/o/e) : """).lower()
                print()
            restart = False

            if choice == 'y' or choice == 'yes':
                print(f"\nYou are using \"{workspace.capitalize()}\" Workspace\n")
                print(f"Platforms Available in {workspace} :-")
                dbs.show_platforms(workspace)

                credentials = login_info(workspace)
                mb.MediaBot(credentials)
                # program working true and returning credentials in format [[platform_name , userid, password]]
            


            elif choice == 'o' or choice == "overwrite":
        
                dbs.print_platforms()

                plist = add_platforms()                  

                dbs.overwrite(workspace, plist)
                clearConsole()
                restart = True
                print(f"restarting \"{workspace.capitalize()}\" Workspace",end="")
                clif.dot(value = 3, sec = 0.4)
                choice = 'y'
                clearConsole()


            elif choice == 'e' or choice == 'exit':
                print("\n Closing program",end="")
                i=0
                while i < 3:
                    time.sleep(0.2)
                    print(".",end="")
                    i += 1
                print()
                exit()

            else:
                print("Invalid Option")
                print("restarting Program",end="")
                clif.dot(value = 3, sec = 0.4)
            
                clearConsole()            
                print()
                time.sleep(0.5)


    else:
        print("Their is no such workspace")

        print("Creating new one for you",end="")
        clif.dot(value = 3, sec = 0.4)
        p_list = []
        dbs.print_platforms()
        p_list = add_platforms()
        dbs.add_ws(workspace,p_list)
        start = True
    
#---------------------------------------------------------------------------------->>>>>