# By Mohanad Hatem 
# Linkedin : https://www.linkedin.com/in/mohanadbinhatem/
# Github   : https://github.com/mohaxad
import os
import shutil
from os.path import  splitext
import tkinter as tk
from tkinter import messagebox as messageBox
from tkinter.filedialog import askdirectory
root = tk.Tk().withdraw()  # to hide the tkinter main window, --not needed--


# ----------------only files with extensions will be organized, folders will not be moved!----------------

# ask the user to choose the folder to organize
directory_to_orgnize = askdirectory(title='Select Folder to organize') + '\\'

# change root directory to user's choice of directory  >> $directory_to_orgnize
os.chdir(directory_to_orgnize)

# list of all files and folders in the "directory_to_orgnize" 
file_list = os.listdir()

# counter for files have been moved and organized 
how_many_files_moved=0;
# counter for  organized and dublicated files
how_many_files_dublicated_and_deleted=0

# loop for all files in the  "directory_to_orgnize" 
for file in file_list:
    file_name, extension = splitext(file)
    folder_destination = "{0}{1}".format(directory_to_orgnize, extension[1::])
    # if the file is not a directory => orgnaize 
    if(os.path.isdir(file) == False):
        # try and make a folder with the extension of the file, if its already exsits than catch an exception and pass "do nothing"
        try:
            os.mkdir(folder_destination)
        except Exception as gException:
            pass
        # try and move the file to the right folder, if the file already exsits "Dublicated", 
        # catch an exception and delete the file for more optimized storage  
        try:
            shutil.move(file, folder_destination)
            how_many_files_moved+=1
        except Exception as alreadyExists :
            os.remove(file)
            how_many_files_dublicated_and_deleted+=1
         
# sum of all the operations for detailed view
detailed_Message ='({0}) - Files have been Organized successfully!\n({1}) - Files are Dublicated and Deleted successfully!\nBy Mohanad Hatem <Mohanadbinhatem@gmail.com>'.format(how_many_files_moved,how_many_files_dublicated_and_deleted)

messageBox.showinfo('Feedback',detailed_Message)
