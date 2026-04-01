class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # there are two zeros
        
        # there is one zeros
        zeroExist = False
        product = 1
        for num in nums:
            if (num == 0):
                if (zeroExist):
                    return [0]*(len(nums))
                zeroExist = True
            else:
                product *= num
        # Non-zero case
        print(zeroExist)
        productList = []
        for num in nums:
            if(num == 0):
                productList.append(product)
            elif (zeroExist):
                productList.append(0)
            else:
                productList.append(product//num)
        return productList

