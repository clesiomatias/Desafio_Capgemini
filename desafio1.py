n = int(input('digite o valor de n: '))
c=n-1
for i in range (n):
    for j in range(n): 
        if j < c:
            print(' ', end='')
        else:
            print('*', end='')
    print()
    c-=1