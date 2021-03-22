c=(input())
if (c>='a' and c<='z'):
    print(f"{c} lowr")
elif (c>='A' and c<='Z'):
       print(f"{c} upr")
elif (c>='0' and c<='9'):
       print(f"{c} no.")
else:
       print(f"{c} is other symbol")