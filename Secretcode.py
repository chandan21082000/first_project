import random as r
import string

def encode_decode(msg, ui):
   words = msg.split(" ")
   cm = []
   
   if ui == 0:
       for word in words:
           if len(word) >= 3:
               a = "".join(r.choices(string.ascii_lowercase, k=3))
               b = "".join(r.choices(string.ascii_lowercase, k=3))
               st = a + word[1:] + word[0] + b
               cm.append(st)
           else:
               cm.append(word[::-1])
       return " ".join(cm)
   
   elif ui == 1:
       for word in words:
           if len(word) >= 3:
               st = word[-4] + word[3:-4]
               cm.append(st)
           else:
               cm.append(word[::-1])
       return " ".join(cm)

   else:
       raise ValueError("ui must be 0 or 1")

def main():
   try:
       ui = int(input("enter 0 for code your msg and 1 for decode your msg : "))
       if not 0 <= ui <= 1:
           raise ValueError("enter 0 for code and 1 for decode")
       
       msg = input("enter your msg : ")
       print(encode_decode(msg, ui))
   
   except ValueError:
       print("please enter valid input 0 or 1")

if __name__ == "__main__":
   main()