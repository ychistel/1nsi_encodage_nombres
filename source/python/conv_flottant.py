x = float(input("saisir le nombre à convertir : "))

n = int(x)
d=x-n
if n== 0:
    print('0',end='')
while n>0:
    r = n%2
    n = n//2
    print(r,end='')
print('.',end='')
while d!= 0:
    d=d*2
    if d >= 1:
        print('1',end='')
        d=d-1
    else:
        print('0',end='')
