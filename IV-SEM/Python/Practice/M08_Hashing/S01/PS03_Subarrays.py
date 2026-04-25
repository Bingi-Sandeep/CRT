def subarraySum(nums, k):
        d = {0:1}
        pref_sum = 0
        count = 0

        for val in nums:        
            pref_sum += val
            comp = pref_sum - k
            if comp in d:
                count += d[comp]
            d[pref_sum] = d.get(pref_sum, 0) + 1
        return count

# Example usage:
print("Enter List: ")
nums = list(map(int, input().split()))
k = int(input("Enter k: "))
result = subarraySum(nums, k)
print(result)

#Iterations
# nums = [1, 1, 1], k = 2
# Iteration 1: pref_sum = 1, comp = -1, count = 0, d = {0:1, 1:1}
# Iteration 2: pref_sum = 2, comp = 0, count = 1, d = {0:1, 1:1, 2:1}
# Iteration 3: pref_sum = 3, comp = 1, count = 2, d = {0:1, 1:1, 2:1, 3:1}
# Final count = 2 
