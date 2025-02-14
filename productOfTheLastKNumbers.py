"""
"""
class ProductOfNumbers:
    # Space: O(n)
    def __init__(self):
        self.prefix_product = [1]

    def add(self, num: int) -> None:
        # O(1)
        # if num is 0 reset the prefix product, as the product before this point is bound to be zero
        if num == 0:
            self.prefix_product = [1]
        else:
            self.prefix_product.append(self.prefix_product[-1]*num)
       

    def getProduct(self, k: int) -> int:
        # O(1)
        # if k is greater than the length of prefix stored, then the product would be 0
        if k >= len(self.prefix_product):
            return 0
        # e.g a*b*c / a*b = c 
        return self.prefix_product[-1] // self.prefix_product[-(k + 1)]


class ProductOfNumbers:
    # Space: O(n)
    # Time Limit Exceeds for this case   

    def __init__(self):
        self.nums = []
        self.suffix_product = []

    def add(self, num: int) -> None:
        # Time O(n)
        for i in range(len(self.nums)):
            self.suffix_product[i]*=num
        self.nums.append(num)
        self.suffix_product.append(num)

    def getProduct(self, k: int) -> int:
        # Time O(1)
        return self.suffixfix_product[-k]
