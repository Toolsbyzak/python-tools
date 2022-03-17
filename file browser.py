import pathlib as p
import os
print ("""
░█████╗░███████╗░█████╗░░██████╗  ███████╗██╗██╗░░░░░███████╗
██╔══██╗╚════██║██╔══██╗██╔════╝  ██╔════╝██║██║░░░░░██╔════╝
███████║░░███╔═╝██║░░██║╚█████╗░  █████╗░░██║██║░░░░░█████╗░░
██╔══██║██╔══╝░░██║░░██║░╚═══██╗  ██╔══╝░░██║██║░░░░░██╔══╝░░
██║░░██║███████╗╚█████╔╝██████╔╝  ██║░░░░░██║███████╗███████╗
╚═╝░░╚═╝╚══════╝░╚════╝░╚═════╝░  ╚═╝░░░░░╚═╝╚══════╝╚══════╝

███╗░░░███╗░█████╗░███╗░░██╗░█████╗░░██████╗░███████╗██████╗░
████╗░████║██╔══██╗████╗░██║██╔══██╗██╔════╝░██╔════╝██╔══██╗
██╔████╔██║███████║██╔██╗██║███████║██║░░██╗░█████╗░░██████╔╝
██║╚██╔╝██║██╔══██║██║╚████║██╔══██║██║░░╚██╗██╔══╝░░██╔══██╗
██║░╚═╝░██║██║░░██║██║░╚███║██║░░██║╚██████╔╝███████╗██║░░██║
╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░╚═╝░╚═════╝░╚══════╝╚═╝░░╚═╝""")
print ("""based on the github project https://github.com/Semicolonvkak/File-Manager-Python/blob/main/FileManager.py""")

Path = ""
files = None
ext = set()

def GetExtintions():

    for i in files:
        ext.add(i.suffix.replace(".",""))


def CreateFolder():

    for i in ext:
        try:
            os.mkdir( str(Path / i) )
        except:
            pass

def MoveFiles():
    for i in files:
        if i.is_file():
            print(Path / i.suffix.replace(".","") / i.name)
            os.rename(str(i), Path / i.suffix.replace(".","") / i.name)


def main():
    global files,Path

    Path = p.Path(input("Enter Path: "))

    files = list(Path.glob("*"))

    GetExtintions()
    CreateFolder()
    MoveFiles()


if __name__ == "__main__":
    main()