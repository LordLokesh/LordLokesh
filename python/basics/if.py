h=10
r=5
t=int(input("inter the no. of minute:"))
v=3.14*r*r*h
a=t*15
if a>v:
    print("overflow")
    print("the time in which tank was filled is")
    print(v//15,"minutes")
elif a<v:
    print("underflow")
    print("the height filled yet is:")
    print((15*t)/(3.14*25),"meter")
else:
    print("fulled")