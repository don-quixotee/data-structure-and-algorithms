
def insertionsort(nums):
    for i in range(1,len(nums)):
        key = nums[i]
        j = i-1

        while j >= 0 and  key < nums[j]:
            nums[j+1] = nums[j]
            j -= 1

        nums[j+1] = key
    print(nums)
num = [6,4,7,4,2,6]
insertionsort(num)

"""
when i=1
-------------------
i=1
j=i-1=>0
num[j]=>6
key=num[i]=>4
key<num[j]=>true
num[j+1]=>num[1] = num[j]=>num[0]
num[1]=4
num[j+1]=k=6
-------------------
when i=2
--------------------
i=2
j=1
key=7
num[j]=>6

-------------------




"""
