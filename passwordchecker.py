import sys

argv=[]
argc=0


def checkPassword(passW):
    score=0
    specialArr=["+", "-", "&", "|", "!", "(", ")", "{", "}", "[", "]", "^", "~", "*", "?", ":", "@", "#", "'", "%", "$", "\"", "\\", "`", "/", ".",";","_","="]
    
    lowArr=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    numArr=["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    
    uppArr=[x.upper() for x in lowArr]
    
    specialScore=0
    lowScore=0
    uppScore=0
    numScore=0
    
    if(len(passW)>=10):
        score+=1
    else:
        print("Increase password length")
    
    for i in specialArr:
        for j in range(0, len(passW), 1):
                if(passW[j]==i):
                    specialScore+=1
    
    if(specialScore>0):
        score+= 1 #specialScore
    else:
        print("add special char")
    
    
    for i in lowArr:
        for j in range(0, len(passW), 1):
                if(passW[j]==i):
                    lowScore+=1
                    
    if(lowScore>0):
        score+= 1 #specialScore
    else:
        print("add lower case char")
        
    for i in uppArr:
        for j in range(0, len(passW), 1):
                if(passW[j]==i):
                    uppScore+=1
                    
    if(uppScore>0):
        score+= 1 #specialScore
    else:
        print("add upper case char")
        
        
        
    for i in numArr:
        for j in range(0, len(passW), 1):
                if(passW[j]==i):
                    numScore+=1
                    
    if(numScore>0):
        score+= 1 #specialScore
    else:
        print("add numbers")
        
    filename="ignis.txt"
    
    lines=""
    with open(filename, "r", encoding="utf-8") as f:
        lines=f.read().splitlines()
    
    
    if passW in lines:
        print("Your Password was found in a Dictonary !!!!")
  
    return score
    
    
    
    

def main():
    global argv
    global argc
    argv=sys.argv
    argc=len(argv)
    
    passTocheck=argv[1]
    
    points=checkPassword(str(passTocheck))
    
    print( "Your password has overall scored "+ str(points)+ "/5")

main()