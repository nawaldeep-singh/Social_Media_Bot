import sqlite3 as sql
import os


obj = sql.connect("media.db")
platforms_available = ["Instagram"]



def workspaces():
    cur = obj.cursor()
    for val in cur.execute("select workspaces from platforms; "):
        print(val)


def isAvailable(workspace):
    for tup in obj.execute("select distinct workspaces from platforms; "):
        for ws in tup:
            if ws == workspace:
                return True
    return False


def list_ws():
    
    if isEmpty() == True:
        print("No Workspace Available...")
        print("Create one for you in just few clicks...\n")

    else:
        print("Workspaces Available :-")
    
        for tup in obj.execute("select distinct workspaces from platforms;"):
            for ws in tup:
                print(" -> "+ws.capitalize())



def show_platforms(workspace):
    i=0
    for tup in obj.execute(f"select platform from platforms where workspaces = '{workspace}';"):
        for ws in tup:
            print(f"{i+1} -> "+ws.capitalize())
            i += 1


def isEmpty():
    for items in obj.execute("select count(workspaces) from platforms;"):
        for count in items:
            if count == 0:
                return True

    return False


def add_ws(workspace, plist):
    index = 0
    while index < len(plist):
        obj.execute(f"insert into platforms values ('{workspace}','{plist[index]}', null, null);")
        obj.commit()
        index += 1
    
        

def media_available():
    return platforms_available

def overwrite(workspace, plist):
    obj.execute(f"delete from platforms where workspaces = '{workspace}'; ")
    obj.commit()
    add_ws(workspace, plist)
    print(f"Workspace {workspace} overwrited...")

def print_platforms():
    print("Platforms available :-\n")
    i=1
    for media in platforms_available:
        print(f"{i} ->"+media)
        i += 1
    print()

def save_data(workspace_name, login_info):
    '''login_info  = [platform name ,  login_id, password]'''
    for login_id in obj.execute(f"select login_id from platforms where workspaces = '{workspace_name}' and platform = '{login_info[0]}';"):
        if None in login_id:
            obj.execute(f"update platforms set login_id = '{login_info[1]}' where workspaces = '{workspace_name}' and platform = '{login_info[0]}' ; ")

    if login_info[2] != None:
        obj.execute(f"update platforms set password = '{login_info[2]}' where workspaces = '{workspace_name}' and platform = '{login_info[0]}' ;")
    
    obj.commit()

def get_login(workspace_name, social_media):
    for details in obj.execute(f"select login_id, password from platforms where workspaces = '{workspace_name}' and platform = '{social_media}'"):
        return list(details)
    

def get_platforms(workspace_name):
    platform=[]
    for media in obj.execute(f"select platform from platforms where workspaces = '{workspace_name}';"):
        platform = platform + list(media)
    return platform

def delete_ws(workspace):
    if workspace != 'insta':
        obj.execute(f"delete from platforms where workspaces = '{workspace}'; ")
        obj.commit()
    
    else:
        print(f"You cannot delete prebuild workspace : {workspace}")
        ch = input("Do you want to reset all workspaces ? (y for yes else no) : ").lower()

        if ch == 'y' or ch=='yes':
            delete_all_ws()
            print("All workspaces are set to default...")

        else:
            print("Please start the program again...")
            exit()


def delete_all_ws():
    os.startfile("repair.py")