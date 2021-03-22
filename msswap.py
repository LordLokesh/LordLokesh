n=int(input()) #12 
rev=0
for i in range(0,n):
    if n!=0:
     rem=n%10
     rev=(rev*10)+rem
     n=n//10
print(rev)
