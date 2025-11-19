# solution one 

def two_sum_brute_force_solution(nums,target):
    n=len(nums)
    for i in range(0,n):
        for j in range(i+1,n):
            if nums[i] + nums[j] == target:
                return [i,j]

# print(two_sum_brute_force_solution([2,7,11,15], 9))


def two_sum_optimal(nums,target):
    hash_map = {}
    n = len(nums)
    for i in range(0,n):
        remaining = target - nums[i]
        if remaining in hash_map:
            return [hash_map[remaining],i]
        else:
            hash_map[nums[i]] = i


print(two_sum_optimal([2,7,11,15], 9))