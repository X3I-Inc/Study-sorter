import shutil
import os
from pathlib import Path

#Alternating current grids, Operating systems, Digital Signal Processing, Electronic Design, Philosophy, Sensors and Actuaators
Subjectlist = ["AC", "OS", "DE", "DSP", "ED", "PH", "SA"] 

#List of types Lecture, Lab, Exercise
Typelist = ["Lec", "Lab", "Ex"]

#Exception names have to be coded seperately
exceptions = ["basics", "S&A"]

def addsubj():
    sub = input("Subject code?: ")
    Subjectlist.append(sub)
    print("added: " + sub)
    return
while True:    
    add = input("Any additional subject codes? (y/n): ")
    match add:
        case "y":
           addsubj()
        case "n":
            break

#Finds file in given directory
def find_file(filename, search_path):
    for root, dirs, files in os.walk(search_path):
        if filename in files:
            return os.path.join(root, filename)
    return None

#finds type of file cases can be added seperately
def seperate_types(name):
    for t in Typelist:
        if t in name:
            return t
        else:
            return "Lec"
    
#Moves file into sorted directory (filename, initial directory,  Course code)
def move_file(filename, search_directory, s):
    ftype = seperate_types(filename)
    fpath = os.path.join(search_directory, filename) #initial filepath
    cpath = os.path.join(r"C:\Users\emilh\OneDrive\Desktop\Year 3",s,ftype) #complete filepath
    if not Path(os.path.join(r"C:\Users\emilh\OneDrive\Desktop\Year 3", s, ftype, filename)).exists():
        shutil.move(fpath, cpath)
        print(filename)
        return

#directory of download by default
search_directory = r"C:\Users\emilh\Downloads"
default_dir = r"C:\Users\emilh\OneDrive\Desktop\Year 3\Unknown"
while True:
    for filename in os.listdir(search_directory):
        for s in Subjectlist:
            if s in filename[0: 5]:
                if "crdownload" not in filename:
                    move_file(filename, search_directory, s)
            
        for e in exceptions:
            if e in filename:
                match e:
                    case "basics":
                        if "crdownload" not in filename:
                            move_file(filename, search_directory, "DSP")
                    case "S&A":
                        if "crdownload" not in filename:
                            move_file(filename, search_directory, "SA")
                    
                    

