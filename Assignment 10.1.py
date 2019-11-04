# Brie Prater
# CIS 245
# Assignment 10.1

import os

print("Welcome to my address book!")
def userdirectory():
    directory = input("Please enter a directory to store your file: ex. Documents ")
    filename = input("What would you like to call this file? ex. My address ")
    dirflag = 0
    while dirflag == 0:
        print("Validating directory name")
        if os.path.isdir(directory):
            dirflag = 1
            print("Directory confirmed.")
        else:
            dirflag = 0
            print("Please try a different directory.")
        break

def userinfo():
    name = input("Please enter your name: ")
    address = input("Please enter your address: ")
    phone = input("Please enter your phone number: ")

def writedata():
    print("Writing to your file")
    try:
        with open(filename, 'w') as filehandle:
            filehandle.write(name + " , " + address + " , " + phone)
        print(filename + " has been successfully saved!")
    except:
        print("An error has occurred.")

def opendata():
    print("Please verify this information:")
    with open(filename, 'r') as filehandle:
        correctdata = filehandle.readline()
    print(correctdata)

userdirectory()
userinfo()
writedata()
opendata()