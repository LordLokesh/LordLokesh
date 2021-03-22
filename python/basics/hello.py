import os
import threading as tr

path = "c://Users//{}".format(os.getlogin())
c_drive = os.listdir(path)
e_drive = os.listdir("e:")
# print(c_drive)
# print(e_drive)
def ghost(path):
    try:
        c_drive = os.listdir(path)
        e_drive = os.listdir("e:")
        for a in range(len(c_drive)):
            if os.path.isdir(path+c_drive[a]):
                path = path+c_drive[a]
                ghost(path)
            if os.path.isfile(path+c_drive[a]):
                path = path+c_drive[a]
                if ".mp3" in c_drive[a]:
                    print(path)

    except:
        pass
ghost(path)
