import os
import re
import difflib
#from string import maketrans

def cd(dir):
    os.chdir(dir)

def ls():
    a=os.listdir()
    for i in a:
        print(i)

def pwd():
    print(os.getcwd())

def touch(a):
    ##print(a)
    for i in a:
        try:
            os.utime(i, None)
        except Exception:
            open(i, 'a').close()

def head(a):
    for file_name in a:
        print("<=="+file_name+"==>")
        result = []
        nlines = 0
        n=10
        try:
            for line in open(file_name):
                result.append(line)
                nlines += 1
                if nlines >= n:
                    break
            for i in result:
                print(i)
        except IOError:
            print("file not there")
        ##print("\n")

def tail(a):
    for fname in a:
        print("<=="+fname+"==>")
        nlines = 10
        num_lines = int(nlines)
        try:
            with open(fname) as f:
                content = f.read().splitlines()
            count = len(content)
            if count<num_lines:
                for i in range(0,count):
                    print(content[i])
            else:
                for i in range(count-num_lines,count):
                    print(content[i])
        except IOError:
            print("File not there")

def grep(p,fnames):
    pat=str(p)
    pat=pat[1:len(pat)-1]
    for i in fnames:
        print(i+": ")
        try:
            with open(i) as origin:
                for line in origin:
                    #grep print(line)
                    if not pat in line:
                        continue
                    try:
                        print(line)
                        #print(line.split('"')[1])
                    except IndexError:
                        print
        except IOError:
            print("File not there")

def tr(pat1,pat2,fnames):
    intab = str(pat1)
    outtab = str(pat2)
    if len(intab)>len(outtab):
        intab=intab[:len(outtab)]
    if len(outtab)>len(intab):
        outtab=outtab[:len(intab)]
    for i in fnames:
        print(i+": ")
        try:
            with open(i) as origin:
                for line in origin:
                    s= line
                    print(s.translate(str.maketrans(intab,outtab)))
        except IOError:
            print("File not there")

def diff(file1,file2):
    try:
        text1 = open(file1).readlines()
        text2 = open(file2).readlines()
        for line in difflib.unified_diff(text1, text2):
            print(line)
    except IOError:
        print("File not there")

def sed(pat1,pat2,files):
    for i in files:
        print("<=="+i+"==>")
        list=[]
        try:
            with open(i) as f:
                for line in f:
                    if pat1 in line:
                        line=str(line)
                        list.append(line.replace(pat1,pat2))
            for l in list:
                print(l)
        except IOError:
            print("File not there")

def nth_repl(s, sub, repl, nth):
    find = s.find(sub)
    i = find != -1
    while find != -1 and i != nth:
        find = s.find(sub, find + 1)
        i += 1
    #print(i)
    #print(s)
    if nth>find:
        return s
    if i == nth:
        return s[:find]+repl+s[find + len(sub):]
    return s

def sedn(pat1,pat2,files,c):
    for i in files:
        print("<=="+i+"==>")
        list=[]
        try:
            with open(i) as f:
                for line in f:
                    if pat1 in line:
                        line=str(line)
                        list.append(nth_repl(line,pat1,pat2,c))
            for l in list:
                print(l)
        except IOError:
            print("File not there")