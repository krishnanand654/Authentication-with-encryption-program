import os                       
import time
from msvcrt import getch

f=open("log.txt",'a+')
f.close()

class encryptcode:
    def __init__(self):
        self.lst=[]
        
    def encrypt(self,z):
        self.a=z
        for i in self.a:
            a=(hex(ord(i)))
            self.lst.append(a)
        return self.lst

def input1():
    x=input("\n\t\tenter username : ")
    y=input("\n\t\tenter password : ")
    a=encryptcode()
    b=encryptcode()
    e1=a.encrypt(x)
    e2=b.encrypt(y)
    return e1,e2
    
def signup():
    os.system('cls')
    print("\t\tSignup\n")
    test=input1()
    e1=test[0]
    e2=test[1]
    
    f=open("log.txt",'r')
    data=f.readlines()
    f.close()

    flag=0
    f=open("log.txt",'r')
    for lines in data:
        if str(e1) in lines:
            flag=1
            break
    if flag==1:
        print("\n\t\tUsername already exist\n \n\t\tTry to signup with another username")
        getch()
    else:
        f=open("log.txt",'a+')
        f.write(str(e1)+str(e2)+"\n")
        f.close()
        print("\n\t\tSignup successfull\n")
        getch()
    

def signin():
    os.system('cls')
    print("\t\tSignin\n")
    test=input1()
    e1=test[0]
    e2=test[1]
    code=(str(e1)+str(e2))
    
    def check(code):
        flag=0
        f=open("log.txt","r")
        data=f.readlines()
        f.close()
        for i in data:
            if code in i:
                flag=1
                break
            else:
                flag=0
        if flag==1:
            print("\n\t\tlogin succesfully\n")
            getch()
        else:
            print("\n\t\tlogin unsuccesfully\n")
            getch()
    check(code)
    
ch=0

while(ch!='z'):
    os.system('cls')
    print("\t\t\tLogin")
    print("\n\nsignup-x\t\tsignin-y\t\texit-z\n\n")
    ch=input("\t\tenter choice : ") 
    if ch=='x':
        e1=""
        e2=""
        signup()
    
    if ch=='y':
        signin()
    
    if ch=='z':
        exit()
