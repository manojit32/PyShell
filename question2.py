import os
import difflib
import re
from commands import *

while(1):
    a=os.getcwd()
    cmd=input(a+" $ ")
    list=cmd.split(' ')
    ##print(list)
    if list[0]=="cd":
        if(len(list)>2):
            name=""
            for i in list[1:]:   
                if list[len(list)-1]!=i:
                    name+=i
                    name+=" "
                else:
                    name+=i
            ##print(name)
            cd(name)
        else:
            cd(list[1])
    elif list[0]=="ls":
        ls()
    elif list[0]=="pwd":
        pwd()
    elif list[0]=="touch":
        touch(list[1:])
    elif list[0]=="head":
        head(list[1:])
    elif list[0]=="tail":
        tail(list[1:])
    elif list[0]=="grep":
        grep(list[1],list[2:])
    elif list[0]=="tr":
        tr(list[1],list[2],list[3:])
    elif list[0]=="diff":
        diff(list[1],list[2])
    elif list[0]=="sed":
        l=list[1].split("/")
        if(l[3]==''):
            c=1
            sedn(l[1],l[2],list[2:],c)
        else:
            if l[3]=='g':
                sed(l[1],l[2],list[2:])
            else:
                c=int(l[3])
                sedn(l[1],l[2],list[2:],c)
    elif list[0]=="exit()":
        exit(0)
