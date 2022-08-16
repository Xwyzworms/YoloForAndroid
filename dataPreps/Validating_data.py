import os

FOLDER_NAME : str = "label_dog"
TOPIC : str = "1"

def getFileContent(fileNamepath):
    read = open(fileNamepath, "r")
    t = read.readlines()
    read.close()
    return t

def validateFile(fileNamepath):
    lines = getFileContent(fileNamepath)
    for line in lines:
        if (line[0] != TOPIC):
            return False
    return True

if __name__ == "__main__":
    for file_name in os.listdir(FOLDER_NAME):
        fileNamepath = os.path.join(FOLDER_NAME, file_name)
        if validateFile(fileNamepath) == False:
            print("Failed !! ")
            break
    print("all file's clear")
            
            


