import unittest
from typing import List,Optional  # Find a magic index in a sorted array.


def magic_index_distinct(array: List[int]):
    if len(array) == 0 :
        return -1
    return magic_index_distinct_bounds(array, 0, len(array)-1)


def magic_index_distinct_bounds(array: List[int], lower: int, upper: int):
    if lower == upper:
        return -1
    middle = (lower + upper) // 2
    if array[middle] == middle:
        return middle
    elif array[middle] > middle:
        return magic_index_distinct_bounds(array, lower, middle)
    else:
        return magic_index_distinct_bounds(array, middle+1, upper)


def magic_index_bounds(array: List[int], lower: int, upper: int) -> int:
    if lower > upper:
        return -1
    middle = (lower + upper)//2
    if array[middle] == middle:
        return middle
  
    left_search_index = min(middle-1,array[middle])
    left = magic_index_bounds(array,lower,left_search_index)
    if left >= 0:
        return left
    right_search_index = max(middle+1,array[middle])
    right = magic_index_bounds(array,right_search_index,upper)
    if right >= 0:
        return right
    return -1

def magic_index(array:List[int])->int:
    if len(array) == 0:
          return -1
    return magic_index_bounds(array, 0, len(array)-1)



class Test(unittest.TestCase):
    def test_magic_index_distinct(self):
        self.assertEqual(magic_index_distinct([3, 4, 5]), -1)
        self.assertEqual(magic_index_distinct([-2, -1, 0, 2]), -1)
        self.assertEqual(magic_index_distinct(
            [-20, 0, 1, 2, 3, 4, 5, 6, 20]), -1)
        self.assertEqual(magic_index_distinct(
            [-20, 0, 1, 2, 3, 4, 5, 7, 20]), 7)
        self.assertEqual(magic_index_distinct([-20, 1, 2, 3, 4, 5, 6, 20]), 3)

    def test_magic_index(self):
        self.assertEqual(magic_index([3, 4, 5]), -1)
        self.assertEqual(magic_index([-2, -1, 0, 2]), -1)
        self.assertEqual(magic_index([-20, 0, 1, 2, 3, 4, 5, 6, 20]), -1)
        self.assertEqual(magic_index([-20, 0, 1, 2, 3, 4, 5, 7, 20]), 7)
        self.assertEqual(magic_index([-20, 1, 2, 3, 4, 5, 6, 20]), 1)
        self.assertEqual(magic_index([-20, 5, 5, 5, 5, 5, 6, 20]), 5)


if __name__ == "__main__":
    unittest.main()
