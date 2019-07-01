import unittest
from array_list import *

class TestList(unittest.TestCase):
    # Note that this test doesn't assert anything! It just verifies your
    #  class and function definitions.

    #1
    def test_interface(self):
        temp_list = empty_list()
        temp_list = add(temp_list, 0, "Hello!")
        length(temp_list)
        get(temp_list, 0)
        temp_list = set(temp_list, 0, "Bye!")
        remove(temp_list, 0)
    #2
    def test_length(self):
        list1 = List([1,2,3,4,5,6], 5, 5)
        test = length(list1)
        self.assertEqual(test, 5)
    #3
    def test_empty_lst(self):
        self.assertEqual(empty_list(), List([None,None], 0, 2))
    #4
    def test_enlarge(self):
        list1 = List([1,2,3,4,5], 5, 5)
        test = enlarge(list1)
        self.assertEqual(test, List([1,2,3,4,5, None, None], 5, 7))
    #5
    def test_add(self):
        list1 = List([1,2,3,4,5], 5, 5)
        test = add(list1, 1, 1.5)
        self.assertEqual(test, List([1,1.5,2,3,4,5, None], 6, 7))
    #6
    def test_add_2(self):
        self.assertRaises(IndexError, add, empty_list(), 1, 1.5 )
    #7
    def test_add_3(self):
        list1 = List([1,2,3,4,5,None], 5, 6)
        test = add(list1, 1, 1.5)
        self.assertEqual(test, List([1,1.5,2,3,4,5], 6, 6))
    #8
    def test_get(self):
        list1 = List([1,2,3,4,5,None], 5, 6)
        test = get(list1,1)
        self.assertEqual(test,2)
    #9
    def test_get_2(self):
        self.assertRaises(IndexError, get, empty_list(), 7)
    #10
    def test_set(self):
        list1 = List([1,2,3,4,5], 5, 5)
        test = set(list1, 1, "poop")
        self.assertEqual(test, List([1,"poop",3,4,5], 5, 5))
    #11
    def test_set_2(self):
        self.assertRaises(IndexError, set, empty_list(), 6, "poop")

    #12
    def test_remove(self):
        list1 = List([1,2,3,4,5], 5, 5)
        test = remove(list1,1)
        self.assertEqual(test, (2, List([1,3,4,5,None], 4, 5)))
    #13
    def test_remove_2(self):
        self.assertRaises(IndexError, remove, empty_list(), 7)
    def test_remove_3(self):
        self.assertRaises(IndexError, remove, empty_list(), 0)
    #14
    print(List([1,2,3,4,5], 5, 5))

    #15
    def testForeach_1(self):
        gather = []
        x = List([1,2,3], 3, 3)
        def f(lst):
            value = lst*2
            gather.append(value)
        foreach(x, f)
        self.assertEqual(gather, [2, 4, 6])

    def testForeach_2(self):
        gather = []
        x = List([1,2,3], 3, 3)
        def f(lst):
            value = lst*3
            gather.append(value)
        foreach(x, f)
        self.assertEqual(gather, [3, 6, 9])

    #16
    def test_sort_1(self):
        x = List([7,3,4], 3, 3)
        def less_than(value1, value2):
            return value1 < value2
        sort(x, less_than)
        self.assertEqual(x, List([3,4,7],3,3))

    def test_sort_2(self):
        x = List([45,67,4], 3, 3)
        def less_than(value1, value2):
            return value1 < value2
        sort(x, less_than)
        self.assertEqual(x, List([4,45,67],3,3))

if __name__ == '__main__':
    unittest.main()
