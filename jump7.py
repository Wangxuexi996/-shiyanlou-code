a=0
while a<100:
    a=a+1
    b=a/7
    s=str(b).split('.')
    c='%d'%a
    if float (s[1])==0:
        continue
    elif '7' in c:
        continue
    print(a)
