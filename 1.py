#nums=input("Please enter three integers: ")
#nums=nums.split()
#nums.sort()
#print(nums)
#smallest=nums[0]
#print(int(smallest))

min=10000000000
for i in nums:
    if int(i) < min :
        min=int(i)
print(min)