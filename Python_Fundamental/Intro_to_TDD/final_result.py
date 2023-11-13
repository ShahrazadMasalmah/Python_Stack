import unittest
# this is what we are running our test on
def reverseList(my_list):
    i=0
    j= len(my_list) - 1
    while(j > i):
        my_list[i],my_list[j] = my_list[j], my_list[i]
        i += 1
        j -= 1
    return my_list 

def isPalindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False    

def coins(amount):
    denominations = [25,10,5,1]
    counts = []
    for d in denominations:
        counts.append(amount//d)
        amount = amount % d
    return counts

def factorial(number):
    mult = 1
    while number > 0:
        mult = mult * number
        number -= 1
    return mult 

def fibonacci(number):
    numOne = 0
    numTwo = 1
    sum = 0
    while number > 1:
        sum = numOne + numTwo 
        numOne = numTwo
        numTwo = sum
        number -= 1
    return numTwo      

# initialized by creating a class that inherits from unittest.TestCase
class IsEvenTests(unittest.TestCase):
    def testOne(self):
        self.assertEqual(reverseList([11,10,5,20]), [20,5,10,11])
    def testTwo(self):
        self.assertEqual(reverseList([1,3,5]), [5,3,1])
    def testThree(self):
        self.assertEqual(reverseList([4,6,7]), [7,6,4])

    def testOneOne(self):
        self.assertEqual(isPalindrome("racecar"), True)
    def testTwoOne(self):
        self.assertEqual(isPalindrome("ogo"), True)
    def testThreeOne(self):
        self.assertEqual(isPalindrome("helleh"), True)
    def testFourOne(self):
        self.assertEqual(isPalindrome("lool"), True)
    def testFiveOne(self):
        self.assertEqual(isPalindrome("backkcab"), True)

    def testOneTwo(self):
        self.assertEqual( coins(87), [3,1,0,2])
    def testTwoTwo(self):
        self.assertEqual(coins(100), [4,0,0,0])
    def testThreeTwo(self):
        self.assertEqual(coins(43), [1,1,1,3])
    def testFourTwo(self):
        self.assertEqual(coins(35), [1,1,0,0])
    def testFiveTwo(self):
        self.assertEqual(coins(157), [6,0,1,2]) 

    def testOneThree(self):
        self.assertEqual( factorial(5), 120)
    def testTwoThree(self):
        self.assertEqual(factorial(10), 3628800)
    def testThreeThree(self):
        self.assertEqual(factorial(3), 6)
    def testFourThree(self):
        self.assertEqual(factorial(6), 720)
    def testFiveThree(self):
        self.assertEqual(factorial(4), 24)

    def testOneFour(self):
        self.assertEqual( fibonacci(5), 5)
    def testTwoFour(self):
        self.assertEqual( fibonacci(7), 13)
    def testThreeFour(self):
        self.assertEqual( fibonacci(10), 55)
    def testFourFour(self):
        self.assertEqual( fibonacci(12), 144)
    def testFiveFour(self):
        self.assertEqual( fibonacci(6), 8) 

    # any task you want run before any method above is executed, put them in the setUp method      
    def setUp(self):
        #add the setUp tasks
        print("running setUp")
    # any task you want run after the tests are executed, put them in the tearDown method
    def tearDown(self):
        # add the tearDown tasks
        print("running tearDown tasks")
if __name__ == '__main__':
    unittest.main() # this runs our tests

