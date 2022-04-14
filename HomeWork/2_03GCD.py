nums = [int(i) for i in input('Input numbers:').split(',')]
nums.sort
result = nums[0]
while result !=0:
    for i in range(1, len(nums)):
        r = nums[i] % result
        if r != 0:
            nums.insert(0, r)
            break
    if result != nums[0]:
        result = nums[0]
    else:
        break
print(result)