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
main_list=[]
tmp_list = []
for i in range(1,101):
    tmp_list.append(i)
    if i%10==0:
        main_list.append(tmp_list)
        tmp_list=[]
print(main_list)