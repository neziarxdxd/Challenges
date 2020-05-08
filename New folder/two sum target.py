nums= [3,3,2, 7, 11, 15,1]
target = 18



'''
for i in range(len(nums)-1):
    for 
    print(i,i+1,":",nums[i] + nums[i+1])
        
'''
x=([i for i in nums if(target > i)])
x1= max(x)
if (nums.index(target-x1)==nums.index(x1)):
   print(*(i  for i, e in enumerate(nums) if e == x1))
else:
    print(nums.index(target-x1),nums.index(x1),":",target-x1,x1)
    
