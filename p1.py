from array import array

class Solution:
    def twoSum(self, nums, target):
        for outer, outer_value in enumerate(nums):
            for inner in range(outer + 1, len(nums)):
                inner_value = nums[inner]
                if outer_value + inner_value == target:
                    return outer, inner

def main():
    s1 = input("Enter array: ")
    my_array = array('i', s1)
    target_num = int(input("Enter target number: "))

    sol = Solution()
    print(sol.twoSum(my_array, target_num))

if __name__ == "__main__":
    main()
