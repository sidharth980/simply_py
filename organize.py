import os
import shutil

class Organizer:
    files_types = {
        "Music" : ["mp3","flac"],
        "Movies": ["avi", "mkv"],
        "Videos" : ["mp4"],
        "Docs" : ["csv","pdf","doc"],
        "Scripts" : ['py'],
        "Images" : ['jpg','png'],
        "Other" : [None]
    }
    def __init__(self):
        self.folder_path = "./"
        print("Creating Folders That Doesnt Exist")
        for x in self.files_types.keys():
            self.create_folder_if_not_exists(x)

    def organize_folder(self):
        for filename in os.listdir(self.folder_path):
            if os.path.isfile(filename) and filename != "organize.py":
                file_type = self.file_type_folder(filename)
                self.move_file(filename,file_type)

    def file_type_folder(self,file_name):
        file_type = file_name.split(".")[-1]
        for x,y in self.files_types.items():
            if file_type in y:
                return x
        return "Other"


    def create_folder_if_not_exists(self,folder_path):
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
            print(f"Folder '{folder_path}' created.")
        else:
            print(f"Folder '{folder_path}' already exists.")
    
    def move_file(self,file_name,destination):
        try:
            shutil.move(self.folder_path+file_name,self.folder_path+destination+"/"+file_name)
            print(f"File {file_name} Moved to {destination}")
        except:
            print("Error Moving File")



if __name__ == "__main__":
    # Organizer().create_folder_if_not_exists("Music")
    # Organizer().move_file("12th_Digilocker.pdf","Docs")
    # print(Organizer().file_type_folder("12th_Digilocker.pdf"))
    # shutil.move("./12th_Digilocker.pdf", "./Docs/12th_Digilocker.pdf")
    Organizer().organize_folder()