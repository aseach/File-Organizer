import os
import shutil

def sort_downloads(downloads, desktop):

    #Makes the path to the sorted folder and creates it if it doesn't exist
    sorted_items = os.path.join(desktop, "DownloadedItems")
    if not os.path.exists(sorted_items):
        os.makedirs(sorted_items)

    #Gets all of the files from the downloads folder
    items = os.listdir(downloads)

    for item in items:

        #Makes the path to the current file from the downloads folder
        curr_path = os.path.join(downloads, item)

        if os.path.isfile(curr_path):

            #Gets the file type
            type = item.split(".")[-1].lower()

            #Makes a folder for the file to be placed into if it doesn't already exist
            type_folder = os.path.join(sorted_items, type)
            if not os.path.exists(type_folder):
                os.makedirs(type_folder)
            
            #Makes the destination for the file and moves it to the organized folder
            destination = os.path.join(type_folder, item)
            shutil.move(curr_path, destination)
        
        elif os.path.isdir(curr_path):

            #Makes a folder for the current folder to be placed into if it doesn't already exist
            type_folder = os.path.join(sorted_items, "Folders")
            if not os.path.exists(type_folder):
                os.makedirs(type_folder)
            
            #Makes the destination for the folder and moves it to the organized folder accordingly
            destination = os.path.join(type_folder, item)
            shutil.move(curr_path, destination)


if __name__ == "__main__":

    #Gets the paths to the downloads and desktop folders and runs the function
    sort_downloads(os.path.expanduser("~/Downloads"), os.path.expanduser("~/Desktop"))