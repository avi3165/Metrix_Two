#q1
list_1=[]
num=int(input("Please enter a number: "))
while num !=0:
    list_1.append(num)
    num = int(input("Please enter a number: "))
a=list_1.pop(-1)
list_1.insert(0,a)
print(list_1)