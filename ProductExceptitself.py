def productExceptSelf(nums):
    answer = []
    n = len(nums)
    prefix = [1]*n
    postfix = [1]*n
    
    for i in range(1,n):
        prefix[i] = prefix[i-1]*nums[i-1]
    
    for i in range(n-2,-1,-1):
        postfix[i] = postfix[i+1]*nums[i+1]

    for i in range(n):
        answer.append(prefix[i]*postfix[i]) 
    
    return answer

print(productExceptSelf([1,2,3,4]))
