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
# א#
# metrix=[[1,2,3,5],[12,13,14,15],[11,12,19,61],[18,61,12,22]]
# list_7=[]
# list_6=[]
# list_8=[]
# dict_1={}
# the_most_number=0
# num=0
# for i,x in enumerate(metrix):
#     for a,b in enumerate(x):
#         list_7.append(b)
#         if b not in dict_1.keys():
#             dict_1[b]=1
#         elif b in dict_1.keys():
#             dict_1[b]+=1
#         if a%2==0:
#             list_6.append(b)
#     list_8.append(list_6)
#     list_6=[]
# print(list_8)
# #ב
# print(sum(list_7))
# #ג
# for k,v in dict_1.items():
#     if v>the_most_number:
#         the_most_number=v
#         num=k
# print (num,"is the number that we have the most",the_most_number)
#q7
# metrix=[[1,2,3,4,5],
#         [6,7,8,9,10],
#         [11,12,13,14,15],
#         [16,17,18,19,20],
#         [21,22,23,24,25]]
# a=1
# #א
# first_slant,second_slant=[],[]
# first_column,last_column=[],[]
# frame=0
#
# for i,v in enumerate(metrix):
#     first_slant.append(v[i])
#     second_slant.append(v[-a])
#     a+=1
#     first_column.append(v[0])
#     last_column.append(v[-1])
#     if i==0:
#         frame+=sum(v)
#     elif i==len(metrix)-1:
#         frame+=sum(v)
#     else:
#         frame+=v[0]+v[-1]
# print("The sum of the first slant is",sum(first_slant))
# print("The sum of the second slant is",sum(second_slant))
# #ב
# print("The sum of the first column is",sum(first_column))
# print("The sum of the last column is",sum(last_column))
# #ג
# print("The sum of the matrix frame is",frame)
#q8
matrix=[[1,2,3,4,5],
        [6,7,8,9,10],
        [11,12,13,14,15],
        [16,17,18,19,20],
        [21,22,23,24,25]]
maximum=matrix[0]
max_index=0
minimum=matrix[0]
min_index=0
#א
for i,v in enumerate(matrix):
    if sum(v)>sum(maximum):
        maximum=v
        max_index=i
    elif sum(v)<sum(minimum):
        minimum=v
        min_index=i
print("The index with the max value is",max_index)
#ב
print("The index with the min value is",min_index)
# ג
new_matrix=[]
for a in range(len(matrix)):
    new_matrix.append([])
for i,v in enumerate(matrix):
    for j in range(1,len(matrix)+1):
        new_matrix[i].append(matrix[-j][i])
print(matrix)
for i in range(len(new_matrix)):
    print(new_matrix[i])