#*******************************
import unittest
import merge
#******************************
def testcompare(list1,list2):
    if len(list1) != len(list2):
        return False
    for idx, val in enumerate(list1) :
            if val != list2[idx] :
                return False
    return True
#***********************************************
class TestMergeMethods ( unittest.TestCase ) :
    # test when two list are equal
    def test_merg1(self) :
        list1 = [1,3,5,7]
        list2 = [2,4,6,8]
        list3 = merge.merge(list1,list2)
        exp_list = [1, 2, 3, 4, 5, 6, 7, 8]
        self.assertTrue(testcompare(exp_list,list3))    
    #test when first list is smaller.  
    def test_merg2(self) :
        list1 = [1,2,3]
        list2 = [4,5,9,10]
        list3 = merge.merge(list1,list2)
        exp_list = [1,2,3,4,5,9,10]
        self.assertTrue(testcompare(exp_list,list3))
    # test when secondlist is smaller.
    def test_merg3(self) :
        list1 = [1,2,3,4,5]
        list2 = [6,7,8]
        list3 = merge.merge(list1,list2)
        exp_list = [1,2,3,4,5,6,7,8]
        self.assertTrue(testcompare(exp_list,list3))
    # test when first list has only 1 element. 
    def test_merge4(self) :
        list1 = [1]
        list2 = [4,5,6]
        list3 = merge.merge(list1,list2)
        exp_list = [1,4,5,6]
        self.assertTrue(testcompare(exp_list,list3))
    # test when second list has 1 element only.
    def test_merge5(self) :
        list1 = [1,4,5]
        list2 = [6]
        list3 = merge.merge(list1,list2)
        exp_list = [1,4,5,6]
        self.assertTrue(testcompare(exp_list,list3))
    # test when first list is empty.
    def test_merg6(self) :
        list1 = [ ]
        list2 = [1,6]
        list3 = merge.merge(list1,list2)
        exp_list = [1,6]
        self.assertTrue(testcompare(exp_list,list3))      
    # test when 2nd list is empty.
    def test_merg7(self) :
        list1 = [1,6]
        list2 = [ ]
        list3 = merge.merge(list1,list2)
        exp_list = [1,6]
        self.assertTrue(testcompare(exp_list,list3))
    # test when both lists are empty
    def test_merg8(self) :
        list1 = [ ]
        list2 = [ ]
        list3 = merge.merge(list1,list2)
        exp_list = [ ]
        self.assertTrue(testcompare(exp_list,list3))
#******************************
if __name__ == '__main__':
    unittest.main()
