a=int(input())


for i in range (1,a+1):
    ch=65
    for k in range(0,i):
        print (chr(ch),end=" ")
        ch=ch+1
    print("")
