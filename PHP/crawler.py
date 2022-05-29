import csv
from re import M
from git import Repo
import os

def start():
    file = open('result.csv')
    data = csv.reader(file)
    array = list(data)
    # print(len(array))
    array.pop(0)
    # print(array)
    # print(len(array))
    # print(array[0][1])
    os.chdir('..')
    os.chdir('..')
    path = os.getcwd()
    print(path)
    path = os.path.join(path, "Repos")
    print(path)
    try:
        os.mkdir(path)
    except OSError as error:
        print(error)
    os.chdir(path)
    min = 0
    max = len(array)
    # for i in range(len(array)):
    while min < max:
        url = array[min][1]
        print(url)
        fileName = url[19:]
        fileName = fileName.replace("/","-")
        clonePath = os.path.join(path, fileName)
        # print(fileName)
        try:
            Repo.clone_from(url, clonePath)
        except:
            print("File already installed")
        min = min + 1

if __name__ == "__main__":
    start()