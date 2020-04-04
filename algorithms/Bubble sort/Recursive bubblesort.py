# def bubblesort(l,n):
#     for i in range(len(l)-2):
#         if l[i] > l[i+1]:
#             l[i], l[i+1] = l[i+1], l[i]
#     if n>1:        
#         bubblesort(l,n-1)   

# l = [6,2,9,11,9,3,7,12]
# n=len(l)    
# bubblesort(l,n)
# print(l)


















def bubblesort(num,n):
    for i in range(len(num)-1):
        if num[i] > num[i+1]:
            num[i], num[i+1] = num[i+1], num[i]
    if n>1:
        bubblesort(num, n-1)

num = [1,5,8,24,2,1,56,8,30]
n = len(num)
bubblesort(num,n)
print(num)