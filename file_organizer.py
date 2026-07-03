import os
import shutil
def get_folder_path():
    path=input("Enter folder path : ")
    files=os.listdir(path)
    print(files)
    categories={
        ".jpg": "Images",
        ".png": "Images",
        ".pdf": "Documents",
        ".mp3": "Music",
        ".mp4": "Videos",
        ".txt": "Documents"
    }   
    for file in files:
        name,extension=os.path.splitext(file)
        if extension in categories:
            folder=categories[extension]
            destination_folder=os.path.join(path,folder)
            if not os.path.exists(destination_folder):
                os.makedirs(destination_folder)
            print(f"{file} -> {folder}")
            source=os.path.join(path,file)
            destination=os.path.join(destination_folder,file)
            shutil.move(source,destination)
get_folder_path()
