from fileinput import filename
import os

LABEL_FOLDER : str = "label_dog"
change_label : str = "dog"
dict_label = {
    "cat" : "0",
    "dog" : "1"
}
def getTheLines(file_name):
    fileNamepath = os.path.join(LABEL_FOLDER, file_name)
    read = open(fileNamepath, "r")
    lines = read.readlines()
    print(lines)
    read.close()
    return lines, fileNamepath


def rename_the_class(fileNamepath, lines):
    print(lines)
    for line in lines:
        print(line)
        if(line[1].isspace()):
            writeFile = dict_label[change_label] + line[1:]
            writeIt =  open(fileNamepath, "w+")
            writeIt.writelines(writeFile)
    writeIt.close()

def is_txt(file_name):
    return file_name.endswith(".txt")    

if __name__ == "__main__":
    for file_name in os.listdir(LABEL_FOLDER):
        if(is_txt(file_name)):
            lines,fileNamepath = getTheLines(file_name)
            rename_the_class(fileNamepath, lines)
print("Done Changing The class !")