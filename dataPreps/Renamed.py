from fileinput import filename
import os
import re

FOLDER_NAME : str = "dataset_raw"

COUNT_CAT = 0
COUNT_DOG = 0
def Renamed(file_name):
    name_target = extract_name(file_name)
    global COUNT_CAT
    global COUNT_DOG
    print(name_target)
    if(name_target.lower() == "cat"):
        name_target += "_" + str(COUNT_CAT) + ".jpg"
        COUNT_CAT += 1
    elif(name_target.lower() == "dog"):
        name_target += "_" + str(COUNT_DOG) + ".jpg"
        COUNT_DOG += 1
    os.rename(file_name, name_target)


def extract_name(file_name):
    pattern = r"(dog|cat)"
    return re.findall(pattern, file_name)[0]


if __name__ == "__main__":
    for file_name in os.listdir(FOLDER_NAME):
        Renamed(os.path.join(FOLDER_NAME, file_name))