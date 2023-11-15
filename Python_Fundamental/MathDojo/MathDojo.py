class MathDojo:
    def __init__(self):
        self.result = 0   
    
    def add(self, num, *nums):
        for number in nums:
            self.result = self.result + number
            #print(self.result)
        self.result += num 
        #print(self.result)   
        return self
    
    def subtract(self, num, *nums):
        sum = 0
        for number in nums:
            sum += number
            #print(sum)
        self.result -= (num + sum)
        return self
    
# create an instance:
md = MathDojo()
# to test:
x = md.add(2).add(2,5,1).subtract(3,2).result
print(x)
y = md.add(3,4,6).add(2,5).subtract(3,2,2).result
print(y)
z = md.add(1,8,11,9).add(6).subtract(6,7).subtract(2,6).result
print(z)
num = md.subtract(10,32).add(9,4).subtract(5,3,4).add(8,7).result
print(num)
num2 = md.add(3,5).subtract(1,2).add(9).subtract(5,8,5).add(7,4,5).result
print(num2)
num3 = md.subtract(1,12).add(1,2,3).subtract(5,7,9).add(4,6,8,2,6).result
print(num3)
