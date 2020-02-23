import csv
import zipfile,requests,io,os
from pathlib import Path
import gfl as ejgen
from zipfile import ZipFile

def convertByteToString(ejByteText=None):
   return ejByteText.decode("utf-8")

def getCurrentProjectPath():
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    return ROOT_DIR.split("ejagruti")[0]
def getCurrentWorkingDirecotry():
    return os.getcwd()
def readAllLines(ejFilePath=None):
    file = open(ejFilePath, mode='r')# Open a file: file
    all_of_it = file.readlines() # read all lines at once
    file.close()  # close the file
    return all_of_it
def readEntireFile(ejFilePath=None):
    file = open(ejFilePath, mode='r')  # Open a file: file
    all_of_it = file.read()  # read all lines at once
    file.close()  # close the file
    return all_of_it
def createCSVFile(ejFilePath=None):
    f=open(ejFilePath,"w+")
    f.close()
def isFilePresent(ejFilePath=None):
    return os.path.exists(ejFilePath)
def appendCSVFile(ejFilePath=None,ejDataToAppend=None):
    if not Path(ejFilePath).is_file():
        createCSVFile(ejFilePath=ejFilePath)
    f=open(ejFilePath,"a+")
    f.write(ejDataToAppend+"\r")
    f.close()
def writeToCSVFile(ejFilePath=None,ejDataToAppend=None):
    f=open(ejFilePath,"w")
    f.write(ejDataToAppend+"\r")
    f.close()
def __ApplyFilterCriteria(ejRowData=None,ejFilterCriteria=None):
    bolcontainschk=False
    for val in ejFilterCriteria:
        if val.upper() in str(ejRowData).upper():
            bolcontainschk=True;break
    return bolcontainschk
def removeRowsFromFile(ejFilePath=None,ejGivenRowMustContainsAtLeastOneValueFromTheList=None,ejFirstRowIsHeader=True):
    lines = list()
    allLines=readAllLines(ejFilePath)

    for line in allLines:
        lines.append(line)
        if not __ApplyFilterCriteria(ejRowData=line,ejFilterCriteria=ejGivenRowMustContainsAtLeastOneValueFromTheList):
                lines.remove(line)
    if ejFirstRowIsHeader:
        headerrow=allLines[0]
        lines.insert(0,headerrow)
    with open(ejFilePath, 'w') as writeFile:
        writeFile.writelines(lines)
        writeFile.close()
def zipFileExtract(ejZipFilePath=None,ejUnzipToFolderPath=None):
    with zipfile.ZipFile(ejZipFilePath, 'r') as zip_ref:
        zip_ref.extractall(ejUnzipToFolderPath)
def zipFileURLDownloadAndExtract(ejZipFileURL=None,ejUnzipToFolderPath=None):
    r = requests.get(ejZipFileURL)
    z = zipfile.ZipFile(io.BytesIO(r.content))
    z.extractall(ejUnzipToFolderPath)
def zipFileContainsList(ejZipFileURL=None):
    r = requests.get(ejZipFileURL)
    z = zipfile.ZipFile(io.BytesIO(r.content))
    return z.filelist
def zipFileURLDownloadAndReadParticularFile(ejZipFileURL=None,ejFileName=None,ejIndex=0):
    r = requests.get(ejZipFileURL)
    z = zipfile.ZipFile(io.BytesIO(r.content))
    if ejFileName is not None:
        return z.open(ejFileName).read().decode("utf-8")
    else:
        return z.open(z.filelist[ejIndex]).read().decode("utf-8")



