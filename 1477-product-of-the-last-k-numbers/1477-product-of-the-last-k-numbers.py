class ProductOfNumbers:

    def __init__(self):
        self.nums = []
        self.product = []
        self.pointer = -1
        self.zero = None
    def add(self, num: int) -> None:
        self.nums.append(num)
        if self.product and self.product[-1] != 0:
            self.product.append(num* self.product[-1])
            self.pointer+=1
        elif not self.product:
            self.product.append(num)
            self.pointer+=1
        elif self.product and self.product[-1] == 0:
            self.product.append(num)
            self.pointer+=1
        if num == 0:
            self.zero = self.pointer
            

    def getProduct(self, k: int) -> int:
        if self.zero is not None:
            recent_zero = self.zero - len(self.product)
            if -k - 1 == recent_zero:
                return self.product[-1]
            elif -k-1 > recent_zero:
                return self.product[-1]//self.product[-k-1]
            else:
                return 0
        else:
            if k < len(self.product):
                return self.product[-1]//self.product[-k-1]
            if k == len(self.product):
                return self.product[-1]



# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)