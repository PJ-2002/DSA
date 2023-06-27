class Solution:
    def twoSum(self):
        my_dict = {}
        n = int(input("Enter array size"))
        for i in range(n):
            value = int(input("Enter array values"))
            my_dict[i]= value

        print(my_dict)

sol = Solution()
sol.twoSum()
