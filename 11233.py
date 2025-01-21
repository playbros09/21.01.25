i = 3786

a=len(str(i))# 4
b=int(i/1000)# 1
c=int((i-(b*1000))/100)# 2
d=int((i-(b*1000)-(c*100))/10)# 3
f=int(i-(b*1000)-(c*100)-(d*10))# 4
print(b)
print(c)
print(d)
print(f)
if i % 1000>=1 and a==4:
    if 1==b:
        print("M",end="")
    elif 2==b:
        print("MM",end="")
    elif 3==b:
        print("MMM",end="")
if i % 100>=1 and a==3 or i % 1000>=1 and a==4:
    if 1==c:
        print("C",end="")
    elif 2==c:
        print("CC",end="")
    elif 3==c:
        print("CCC",end="")
    elif 4==c:
        print("CD",end="")
    elif 5==c:
        print("D",end="")
    elif 6==c:
        print("DC",end="")
    elif 7==c:
        print("DCC",end="")
    elif 8==c:
        print("DCCC",end="")
    elif 9==c:
        print("CM",end="")
if i % 10>=1 and a==2 or i % 100>=1 and a==3 or i % 1000>=1 and a==4:
    if 1==d:
        print("X",end="")
    elif 2==d:
        print("XX",end="")
    elif 3==d:
        print("XXX",end="")
    elif 4==d:
        print("XL",end="")
    elif 5==d:
        print("L",end="")
    elif 6==d:
        print("LX",end="")
    elif 7==d:
        print("LXX",end="")
    elif 8==d:
        print("LXXX",end="")
    elif 9==d:
        print("XC",end="")
if i>=1 and a==1 or i % 10>=1 and a==2 or i % 100>=1 and a==3 or i % 1000>=1 and a==4:
    if 1==f:
        print("I",end="")
    elif 2==f:
        print("II",end="")
    elif 3==f:
        print("III",end="")
    elif 4==f:
        print("IV",end="")
    elif 5==f:
        print("V",end="")
    elif 6==f:
        print("VI",end="")
    elif 7==f:
        print("VII",end="")
    elif 8==f:
        print("VIII",end="")
    elif 9==f:
        print("IX",end="")