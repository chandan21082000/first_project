import random as r
import string
ui=int(input("enter 0 for code your msg and 1 for decode your msg : "))
msg=input("enter your msg  : ")
words=msg.split(" ")
cm=[]     #we are going to save code msg in this
if ui==0:
    for word in words:
        if len(msg)>=3:
            a="".join(r.choices(string.ascii_lowercase,k=3))
            b="".join(r.choices(string.ascii_lowercase,k=3))
            st=a+word[1:]+word[0]+b
            cm.append(st)
        else:
            cm.append(word[::-1])
    print(" ".join(cm))
elif ui==1:
    for word in words:
        if len(msg)>=3:
            st=word[-4]+word[3:-4]
            cm.append(st)
        else:
            cm.append(word[::-1])
    print(" ".join(cm))
