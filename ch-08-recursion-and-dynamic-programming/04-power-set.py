# Compute the power set of a set.
import unittest
from typing import Set, List,Any
from copy import deepcopy


def power_set(start_set: Set[Any]) -> List[Set[Any]]:
    
    if len(start_set) == 0:
          empty: List[Set[Any]] = [set()]
          return empty
    if len(start_set) == 1:
          empty: List[Set[Any]] = [set()]
          empty.append(start_set)
          return empty
    # add to power set
    elem_x = start_set.pop()
    new_powerset = power_set(start_set)
    new_powerset_copy = deepcopy(new_powerset)
    for st in new_powerset_copy:
          st.add(elem_x)
    return new_powerset + new_powerset_copy
# Combinatorics Solution


def getsubsets2(aset):
    allSubsets = []
    max = 1 << len(aset)
    for k in range(max):
        subset = convertIntToSet(k, aset)
        allSubsets.append(subset)
    return allSubsets


def convertIntToSet(x, aset):
    subset = []
    index = 0
    k = x
    while k > 0:
        if k & 1 == 1 and aset[index] not in subset:
            subset.append(aset[index])
        index += 1
        k >>= 1
    return subset
class Test(unittest.TestCase):
    def test_power_set(self):
        s = {'a', 'b', 'c', 'd'}
        ps = power_set(s)
        self.assertEqual(len(ps), 16)
        subsets = [set(), {'a'}, {'b'}, {'c'}, {'d'},
                   {'a', 'b'}, {'a', 'c'}, {'a', 'd'}, {
                       'b', 'c'}, {'b', 'd'}, {'c', 'd'},
                   {'a', 'b', 'c'}, {'a', 'b', 'd'}, {'a', 'c', 'd'}, {'b', 'c', 'd'}, s]
        self.assertEqual(ps, set([frozenset(s) for s in subsets]))


if __name__ == "__main__":
    #unittest.main()
    s = {'a', 'b', 'c', 'd'}
    s2 = ['a', 'b', 'c', 'd']
    print(power_set(s))
    print(list(s))
    print(getsubsets2(list(s2)))
