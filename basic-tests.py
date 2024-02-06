import unittest
import math
import numpy as np
from main import HLeaf, HNode, HTNode, tree_lt, base_tree_list, tree_list_insert, \
    initial_tree_sort, coalesce_once, coalesce_all, cnt_freq, build_encoder_array, \
    encode_string_one, bits_to_chars

# please note: these are not real tests! They don't include
# expected results, and they don't actually test that the
# given functions and methods *work*, they just test to make
# sure that the given methods and functions actually exist,
# and run when called with the right # and kind of arguments.

# your test cases must be better than these! Each of your tests
# should include an assertion containing an expected result.

# Also: you can edit this file, but it's probably not a good idea;
# deleting these tests, for instance, would result in "all tests
# passed" from GitHub... but then your code would fail terribly
# against the post-handin test cases. So just don't edit this file.

class MyTests(unittest.TestCase):

    def test_cnt_freq(self):
        table = cnt_freq("abcd")
        table[3]
        table[79]

    def test_tree_construction(self):
        HNode(3,'a',HLeaf(1,'a'),HLeaf(2,'b'))

    def test_tree_lt(self):
        self.assertEqual(type(tree_lt(HLeaf(0,'a'),HLeaf(0,'a'))), bool)

    def test_tree_lists(self):
        HTNode(HLeaf(0,'a'),HTNode(HLeaf(0,'a'),None))

    def test_base_tree_list(self):
        self.assertEqual(type(base_tree_list(np.array([0 for i in range(256)],dtype=np.int32))),HTNode)

    def test_tree_lt_insert(self):
        self.assertEqual(type(tree_list_insert(None,HLeaf(0,'a'))),HTNode)

    def test_initial_tree_sort(self):
        self.assertEqual(type(initial_tree_sort(HTNode(HLeaf(0,'a'),None))),HTNode)

    def test_coalesce_once(self):
        self.assertEqual(type(coalesce_once(HTNode(HLeaf(0,'a'),HTNode(HLeaf(0,'a'),None)))),HTNode)

    def test_coalesce_all(self):
        self.assertEqual(type(coalesce_all(HTNode(HLeaf(0,'a'),HTNode(HLeaf(0,'a'),None)))),HNode)

    def test_build_encoder_array(self):
        build_encoder_array(HLeaf(0,'a'),np.array(["" for i in range(256)],dtype='object'),"")

    def test_encode_string_one(self):
        self.assertEqual(type(encode_string_one("abcd",
                                           np.array(["" for i in range(256)],dtype='object'))),
                         str)

    def test_bits_to_chars(self):
        self.assertEqual(type(bits_to_chars("abcd")),str)

if (__name__ == '__main__'):
    unittest.main()
    MyTests().test_tree_lists()
    #HTNode(HLeaf(0, 'a'), HTNode)
