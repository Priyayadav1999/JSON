# a=[1,2,3,4]
# b=[2,34,4]
# print(a+b)
# a.append(b)
# print(a)

# a=10
# b=a
# a+=10
# b+=20
# print(a,b)

# a=[10,20]
# b=a
# b.append(30)
# print(a)
# print("b",b)

num=[5,7,-8,-9,10,1,2]
i=0
while i<len(num):
    j=0
    while j<len(num):
        if num[i]<=0:
            num[i]=0
        elif num[i]<num[j]:
            temp=num[i]
            num[i]=num[j]
            num[j]=temp
        j+=1
    i+=1
print( num)

