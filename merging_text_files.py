import glob2
from datetime import datetime
"""
A script to merge three text files together
 - Timothy Seguia 8/27/18
"""
# glob2.glob('*.txt')
# print(glob2.glob('*.txt'))
fileList = sorted(glob2.glob('*.txt'))
fileName = datetime.now().strftime("%y-%-m-%d-%h-%M-%S-%f")+".txt"
print(fileName)

for files in fileList:
    if files == "file1.txt" or files == "file2.txt" or files == "file3.txt":
        with open(files, "r") as fileVariable:
            content = fileVariable.read()
        with open(fileName,"a") as contentFile:
            contentFile.write(content+"\n")
