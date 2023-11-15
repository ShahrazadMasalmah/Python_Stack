import unittest

# this is what we are running our test on
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

# initialized by creating a class that inherits from unittest.TestCase
class MathDojoTests(unittest.TestCase):
    # each method in this class is a test to be run
    def testOne(self):
        calculate = self.md.add(6).subtract(2).result
        self.assertEqual(calculate, 4)
    def testTwo(self):
        calculate = self.md.add(2,4,7).subtract(3,4,9).result
        self.assertEqual(calculate, -3)
    def testThree(self):
        calculate = self.md.subtract(2,1).add(3,10,8).result
        self.assertEqual(calculate, 18)
    def testFour(self):
        calculate = self.md.add(2,6,4,7).add(5,34,55).result
        self.assertEqual(calculate, 113)
    def testFive(self):
        calculate = self.md.subtract(2,8).subtract(8,3).result
        self.assertEqual(calculate, -21)        
   
    # any task you want run before any method above is executed, put them in the setUp method
    def setUp(self):
        # add the setUp tasks
        print("running setUp")
        self.md = MathDojo()
    # any task you want run after the tests are executed, put them in the tearDown method
    def tearDown(self):
    # add the tearDown tasks
        print("running tearDown tasks")
if __name__ == '__main__':
    unittest.main() # this runs our tests

