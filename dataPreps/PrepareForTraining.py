from copy import copy
import os
from pickle import FALSE
import random
import shutil
import re
from typing import List
random.seed(5)

LABELLED_PATH : str = ""

READY_TRAIN_PATH : str = "../ReadyToTrain/"

IMAGES_PATH : str = "../ReadyToTrain/images"
LABELS_PATH : str ="../ReadyToTrain/labels"

TRAINING_PATH : str ="../ReadyToTrain/images/train/"
VALIDATION_PATH : str = "../ReadyToTrain/images/validation/"

TRAINING_LABEL_PATH : str = "../ReadyToTrain/labels/train"
VALIDATION_LABEL_PATH : str = "../ReadyToTrain/labels/validation"

CAT_PATH : str ="./cat"
DOG_PATH : str ="./dog"

CAT_PATH_LABEL : str ="./label_cat"
DOG_PATH_LABEL : str = "./label_dog"

ONWORKFolders : List = ["cat", "dog", "label_cat", "label_dog"]

OnWorkClasses : List = ["cat", "dog"]

def prepareTrainingPrequisites():
    try :
        if(os.path.exists(READY_TRAIN_PATH) == False):
            os.mkdir(READY_TRAIN_PATH)

        if(os.path.exists(IMAGES_PATH) == False ) :
            os.mkdir(IMAGES_PATH)

        if(os.path.exists(LABELS_PATH) == False):
            os.mkdir(LABELS_PATH)

        if(os.path.exists(TRAINING_PATH) == False):
            os.mkdir(TRAINING_PATH)

        if(os.path.exists(VALIDATION_PATH) == False):
            os.mkdir(VALIDATION_PATH)

        if(os.path.exists(TRAINING_LABEL_PATH) == False):
            os.mkdir(TRAINING_LABEL_PATH)
        
        if(os.path.exists(VALIDATION_LABEL_PATH) == False):
            os.mkdir(VALIDATION_LABEL_PATH)
        
    except Exception as e:
        print(e)

def getDataset():
    full_list : List = []
    for folder_name in OnWorkClasses:
        data_list : List = []
        for file_name in os.listdir(folder_name):
            data_list.append(file_name)
        full_list.append(data_list)
    return full_list

def splitEachClass(listOfClass : List, percentage : float):
    trainingList : List  = []
    validationList : List = []

    for data_list in listOfClass:
        percentage_data : int = int(len(data_list) - len(data_list) * percentage)
        random.shuffle(data_list)
        trainingList = trainingList + data_list[:percentage_data]
        validationList += data_list[percentage_data:]
    return  trainingList, validationList

def extractClassNames(fileName):
    pattern = r"^(cat|dog)"
    return re.findall(pattern, fileName )[0]

def prepareCopydata(dataset, isValidation : bool = False, isImg : bool =True):
    for fileName in dataset:
        if(isImg):
            if(extractClassNames(fileName) == "cat"):
                checkData(CAT_PATH, fileName, isValidation, True)       
            elif(extractClassNames(fileName) == "dog"):
                checkData(DOG_PATH, fileName, isValidation, True)
        else:
            if(extractClassNames(fileName) == "cat"):
                checkData(CAT_PATH_LABEL, re.sub(".jpg",".txt", fileName), isValidation, False)       
            elif(extractClassNames(fileName) == "dog"):
                checkData(DOG_PATH_LABEL, re.sub(".jpg", ".txt", fileName), isValidation, False)

def checkData(path, fileNameTarget, isValidation : bool, isImg : bool):
    for fileName in os.listdir(path):
        currentFilePath = os.path.join(path, fileName)
        if(isImg):
            currentFileCopyPath = os.path.join(TRAINING_PATH, fileName)
            if(fileName == fileNameTarget):
                if(isValidation):
                    currentFileCopyPath = os.path.join(VALIDATION_PATH, fileName)
                copyData(currentFilePath, currentFileCopyPath )
        elif(isImg == False):
            print(fileNameTarget)
            currentFileCopyPath = os.path.join(TRAINING_LABEL_PATH, fileName)
            if(fileName == fileNameTarget):
                print("ITS is same")
                if(isValidation):
                    currentFileCopyPath = os.path.join(VALIDATION_LABEL_PATH, fileName)
                copyData(currentFilePath, currentFileCopyPath)    

def copyData(path, fileNametarget):
    shutil.copy(path, fileNametarget)

if __name__ == "__main__":
    prepareTrainingPrequisites()
    dataset = getDataset()
    training_dataset, validation_dataset = splitEachClass(dataset, 0.2)
    prepareCopydata(training_dataset)
    prepareCopydata(validation_dataset, True)

    ## Copying Label
    prepareCopydata(training_dataset,False, False)
    prepareCopydata(validation_dataset,True, False)


