qustions=[
    ["The International Literacy Day is observed on","spe8","spe9","sep10","sep3","a"],
    ["In which places the Kumbha Mela is held every twelve years?","mumbai","haridwar","varansi","delhi","b"],
    ["The language of Lakshadweep. a Union Territory of India,is","tamil","english","malyalam","pocoloco","c"],
    ["Bahubali festival is related to","Jainism","buddhism","hinduism","islam","a"],
    ["Who is the author of the book 'Amrit Ki Ore'?","mukesh kumar","Narendra mohan","mohan das","nared amrit","b"],
    ["World Health Day is observed on","nov8","jun7","jun27","apr7","c"],
    ["Which day is observed as the World Standards  Day","oct14","spe9","aug10","nov3","a"],
    ["Pongal is a popular festival of which state?","mumbai","tamilnadu","varansi","delhi","b"],
    ["Ghototkach in Mahabharat was the son of","kaurav","arjun","bhima","bhisma","c"],
    ["Which of the following is observed as Sports Day every year?","aug29","nov1","sep10","aug21","a"],
    ["Which of the following Muslim festivals is based on the Holy Quran ?","id ul fakir","id ul zuha","salam valikum","valikum as-salam","b"],
    ["The first month of the Indian national calendar is","chaitra","pritma","vaishak","kartike","c"],
]
levels=[1000,2000,4000,8000,16000,32000,64000,100000,320000,500000,800000,10000000]
money=0
for i in range(0,len(qustions)):
    qustion=qustions[i]
    print(f"\n{i+1}. this is your qustion for {levels[i]} :")
    print(qustion[0])
    print(f"a. {qustion[1]}       b.{qustion[2]}")
    print(f"c. {qustion[3]}       d.{qustion[4]}")
    reply=input("enter your guess a-d or press x for quit : ")
    if reply!="a" and reply!="b" and reply!="c" and reply!="d" and reply!="x":
     raise print("guess only between this a,b,c,d")
    if reply=="x" and i>=1:
      money=levels[i-1]
    else:
      print(f"\nyou will be taking home {money}rs")
    break
    if reply==qustion[-1]:
        money=levels[i]
        print(f"\n you are coreect you won {money}")
        if i==4:
          money=16000
          if i==8:
            money==320000
          if i==11:
            money==10000000
    else:
        print(f"\n you have lost,you will be taking home {money}rs")
        break
        