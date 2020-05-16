def  fibo(num):
    if num == 0:
        return 0
    if num == 1:
        return 1
    else:
        return fibo(num -1) + fibo(num -2)

num = int(input("enter your num : "))
n = fibo(num)
for i  in range(1, n+1):
    print(fibo(i))