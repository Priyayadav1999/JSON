a=[[10,20],20,[80,9]]
i=0
sum=0
max=0
while i<len(a):
    if type(a[i])==list:
        j=0
        while j<len(a[i]):
            sum=sum+a[i][j]
            j+=1
    else:
        sum=sum+a[i]
    i+=1
print(sum)