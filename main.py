
row=eval(input('请输入零星的行数：'))
while row%2==0:
    print('请重新输入')
    row=eval(input('请输入零星的行数：'))
middle=row//2+1
for i in range(1,middle+1):
    for j in range(1,middle+1-i):
        print(' ',end='')

    for k in range(1,i*2):
        if k == 1 or k == i * 2 - 1:
            print('*',end='')
        else :
            print(' ',end='')
    print()
for i in range(1,middle):
    for j in range(1,i+1):
        print(' ',end='')
    for k in range(1,(middle-1)*2-2*i+2):
        if k==1 or k==(middle-1)*2-2*i+2-1:
            print('*',end='')
        else:
            print(' ', end='')
    print()

