#q1
# list_1=[]
# num=int(input("Please enter a number: "))
# while num !=0:
#     list_1.append(num)
#     num = int(input("Please enter a number: "))
# a=list_1.pop(-1)
# list_1.insert(0,a)
# print(list_1)
#q2
#answer=[5,8,9,8,5]
# q3
# arr1 = [5,4,3]
# arr2 = [1,10,-5]
# arr3 = [10, 30, 15, 2]
# arr4 = [200, 20]
# All=[arr1,arr2,arr3,arr4]
# print(len(All))
# chek=[3,44,10,5,6]
# for num in chek:
#     x=0
#     for b_i,b_v in enumerate(All):
#         if num in b_v:
#             print(num,"in All",b_i)
#             x=1
#             break
#     if x==0:
#         print(num, 'not in All',b_i)
#q4
# main_list=[]
# tmp_list = []
# for i in range(1,101):
#     tmp_list.append(i)
#     if i%10==0:
#         main_list.append(tmp_list)
#         tmp_list=[]
# print(main_list)
#q5
# num=int(input("Please enter a number: "))
# main_list=[]
# tmp_list = []
# for i in range(1,num*num+1):
#     tmp_list.append(i)
#     if i%num==0:
#         main_list.append(tmp_list)
#         tmp_list=[]
# print(main_list)
#q6
# א
metrix=[[1,2,3,5],[12,13,14,15],[11,12,19,61],[18,61,12,22]]
list_7=[]
list_6=[]
list_8=[]
dict_1={}
the_most_number=0
num=0
for i,x in enumerate(metrix):
    for a,b in enumerate(x):
        list_7.append(b)
        if b not in dict_1.keys():
            dict_1[b]=1
        elif b in dict_1.keys():
            dict_1[b]+=1
        if a%2==0:
            list_6.append(b)
    list_8.append(list_6)
    list_6=[]
print(list_8)
#ב
print(sum(list_7))
#ג
for k,v in dict_1.items():
    if v>the_most_number:
        the_most_number=v
        num=k
print (num,"is the number that we have the most",the_most_number)