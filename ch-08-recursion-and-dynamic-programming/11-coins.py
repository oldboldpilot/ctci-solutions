# Count the number of ways to make change for a given number of cents.

# Why settle for a slower algorithm when a constant time algorithm exists?


def count(S, m, n ): 
  
    # If n is 0 then there is 1 
    # solution (do not include any coin) 
    if (n == 0): 
        return 1
  
    # If n is less than 0 then no 
    # solution exists 
    if (n < 0): 
        return 0; 
  
    # If there are no coins and n 
    # is greater than 0, then no 
    # solution exist 
    if (m <=0 and n >= 1): 
        return 0
  
    # count is sum of solutions (i)  
    # including S[m-1] (ii) excluding S[m-1] 
    return count( S, m - 1, n ) + count( S, m, n-S[m-1] ); 
import unittest

class Test(unittest.TestCase):
  def test_count(self):
    arr = [1, 2, 3] 
    m = len(arr) 
    #print(count(arr, m, 4)) 
    self.assertEqual(count(arr,m,4), 4)
    arr[2]=5
    print(count(arr,m,12))
  

if __name__ == "__main__":
  unittest.main()

