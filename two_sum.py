nums = [2, 7, 11, 15]
target = 9

def two_sum(nums, target):

    seen = {}

    for i in range(len(nums)):

        needed = target - nums[i]

        if needed in seen:
            return [seen[needed], i]

        seen[nums[i]] = i

    return []

result = two_sum(nums, target)
print(result)  # Output: [0, 1]