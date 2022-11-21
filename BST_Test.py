import unittest
from Binary_Search_Tree import Binary_Search_Tree

class DSQTester(unittest.TestCase):
    
    def setUp(self):
        self.__tree = Binary_Search_Tree()

    def __make_big_tree(self):
        self.__tree.insert_element(100)
        self.__tree.insert_element(50)
        self.__tree.insert_element(150)
        self.__tree.insert_element(40)
        self.__tree.insert_element(200)
        self.__tree.insert_element(60)
        self.__tree.insert_element(125)
        self.__tree.insert_element(30)
        self.__tree.insert_element(55)
        self.__tree.insert_element(70)
        self.__tree.insert_element(300)
        self.__tree.insert_element(45)
        self.__tree.insert_element(65)
        self.__tree.insert_element(75)
        self.__tree.insert_element(20)
        #In order: [ 20, 30, 40, 45, 50, 55, 60, 65, 70, 75, 100, 125, 150, 200, 300 ]

############## __balance single rotations ###############
    #linear tree
    def test_single_right_rot_three_nodes(self):
        self.__tree.insert_element(3)
        self.__tree.insert_element(2)
        self.__tree.insert_element(1)
        self.assertEqual('[ 1, 2, 3 ]', str(self.__tree))
        self.assertEqual('[ 2, 1, 3 ]', self.__tree.pre_order())
        self.assertEqual('[ 1, 3, 2 ]', self.__tree.post_order())

    def test_single_left_rot_three_nodes(self):
        self.__tree.insert_element(1)
        self.__tree.insert_element(2)
        self.__tree.insert_element(3)
        self.assertEqual('[ 1, 2, 3 ]', str(self.__tree))
        self.assertEqual('[ 2, 1, 3 ]', self.__tree.pre_order())
        self.assertEqual('[ 1, 3, 2 ]', self.__tree.post_order())

    def test_height_single_right_rot_three_nodes(self):
        self.__tree.insert_element(3)
        self.__tree.insert_element(2)
        self.__tree.insert_element(1)
        self.assertEqual(2, self.__tree.get_height())

    def test_height_single_left_rot_three_nodes(self):
        self.__tree.insert_element(1)
        self.__tree.insert_element(2)
        self.__tree.insert_element(3)
        self.assertEqual(2, self.__tree.get_height())

    #single rotation with floater
    def test_single_right_rot_with_floater(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(22)
        self.__tree.insert_element(18)
        self.__tree.insert_element(19)
        self.__tree.insert_element(16)
        self.__tree.insert_element(10)
        self.assertEqual('[ 10, 16, 18, 19, 20, 22 ]', str(self.__tree))
        self.assertEqual('[ 18, 16, 10, 20, 19, 22 ]', self.__tree.pre_order())
        self.assertEqual('[ 10, 16, 19, 22, 20, 18 ]', self.__tree.post_order())

    def test_single_left_rot_with_floater(self):
        self.__tree.insert_element(16)
        self.__tree.insert_element(10)
        self.__tree.insert_element(19)
        self.__tree.insert_element(18)
        self.__tree.insert_element(20)
        self.__tree.insert_element(22)
        self.assertEqual('[ 10, 16, 18, 19, 20, 22 ]', str(self.__tree))
        self.assertEqual('[ 19, 16, 10, 18, 20, 22 ]', self.__tree.pre_order())
        self.assertEqual('[ 10, 18, 16, 22, 20, 19 ]', self.__tree.post_order())

    def test_height_single_right_rot_with_floater(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(22)
        self.__tree.insert_element(18)
        self.__tree.insert_element(19)
        self.__tree.insert_element(16)
        self.__tree.insert_element(10)
        self.assertEqual(3, self.__tree.get_height())

    def test_height_single_left_rot_with_floater(self):
        self.__tree.insert_element(16)
        self.__tree.insert_element(10)
        self.__tree.insert_element(19)
        self.__tree.insert_element(18)
        self.__tree.insert_element(20)
        self.__tree.insert_element(22)
        self.assertEqual(3, self.__tree.get_height())

    #single rotation at inner node, not root
    def test_single_right_rot_at_inner_node(self):
        self.__tree.insert_element(50)
        self.__tree.insert_element(25)
        self.__tree.insert_element(75)
        self.__tree.insert_element(0)
        self.__tree.insert_element(100)
        self.__tree.insert_element(60)
        self.__tree.insert_element(65)
        self.__tree.insert_element(66)
        self.assertEqual('[ 0, 25, 50, 60, 65, 66, 75, 100 ]', str(self.__tree))
        self.assertEqual('[ 50, 25, 0, 75, 65, 60, 66, 100 ]', self.__tree.pre_order())
        self.assertEqual('[ 0, 25, 60, 66, 65, 100, 75, 50 ]', self.__tree.post_order())

    def test_single_left_rot_at_inner_node(self):
        self.__tree.insert_element(19)
        self.__tree.insert_element(70)
        self.__tree.insert_element(10)
        self.__tree.insert_element(80)
        self.__tree.insert_element(1)
        self.__tree.insert_element(15)
        self.__tree.insert_element(16)
        self.__tree.insert_element(17)
        self.assertEqual('[ 1, 10, 15, 16, 17, 19, 70, 80 ]', str(self.__tree))
        self.assertEqual('[ 19, 10, 1, 16, 15, 17, 70, 80 ]', self.__tree.pre_order())
        self.assertEqual('[ 1, 15, 17, 16, 10, 80, 70, 19 ]', self.__tree.post_order())

    def test_height_single_right_rot_at_inner_node(self):
        self.__tree.insert_element(50)
        self.__tree.insert_element(25)
        self.__tree.insert_element(75)
        self.__tree.insert_element(0)
        self.__tree.insert_element(100)
        self.__tree.insert_element(60)
        self.__tree.insert_element(65)
        self.__tree.insert_element(66)
        self.assertEqual(4, self.__tree.get_height())

    def test_height_single_left_rot_at_inner_node(self):
        self.__tree.insert_element(19)
        self.__tree.insert_element(70)
        self.__tree.insert_element(10)
        self.__tree.insert_element(80)
        self.__tree.insert_element(1)
        self.__tree.insert_element(15)
        self.__tree.insert_element(16)
        self.__tree.insert_element(17)
        self.assertEqual(4, self.__tree.get_height())

    #single rotation at inner node with floater
    def test_single_right_rot_at_inner_node_with_floater(self):
        self.__tree.insert_element(30)
        self.__tree.insert_element(20)
        self.__tree.insert_element(40)
        self.__tree.insert_element(18)
        self.__tree.insert_element(22)
        self.__tree.insert_element(50)
        self.__tree.insert_element(16)
        self.__tree.insert_element(19)
        self.__tree.insert_element(10)
        self.assertEqual('[ 10, 16, 18, 19, 20, 22, 30, 40, 50 ]', str(self.__tree))
        self.assertEqual('[ 30, 18, 16, 10, 20, 19, 22, 40, 50 ]', self.__tree.pre_order())
        self.assertEqual('[ 10, 16, 19, 22, 20, 18, 50, 40, 30 ]', self.__tree.post_order())

    def test_single_left_rot_at_inner_node_with_floater(self):
        self.__tree.insert_element(30)
        self.__tree.insert_element(20)
        self.__tree.insert_element(40)
        self.__tree.insert_element(18)
        self.__tree.insert_element(50)
        self.__tree.insert_element(35)
        self.__tree.insert_element(45)
        self.__tree.insert_element(55)
        self.__tree.insert_element(60)
        self.assertEqual('[ 18, 20, 30, 35, 40, 45, 50, 55, 60 ]', str(self.__tree))
        self.assertEqual('[ 30, 20, 18, 50, 40, 35, 45, 55, 60 ]', self.__tree.pre_order())
        self.assertEqual('[ 18, 20, 35, 45, 40, 60, 55, 50, 30 ]', self.__tree.post_order())

    def test_height_single_right_rot_at_inner_node_with_floater(self):
        self.__tree.insert_element(30)
        self.__tree.insert_element(20)
        self.__tree.insert_element(40)
        self.__tree.insert_element(18)
        self.__tree.insert_element(22)
        self.__tree.insert_element(50)
        self.__tree.insert_element(16)
        self.__tree.insert_element(19)
        self.__tree.insert_element(10)
        self.assertEqual(4, self.__tree.get_height())

    def test_height_single_left_rot_at_inner_node_with_floater(self):
        self.__tree.insert_element(30)
        self.__tree.insert_element(20)
        self.__tree.insert_element(40)
        self.__tree.insert_element(18)
        self.__tree.insert_element(50)
        self.__tree.insert_element(35)
        self.__tree.insert_element(45)
        self.__tree.insert_element(55)
        self.__tree.insert_element(60)
        self.assertEqual(4, self.__tree.get_height())

############## __balance double rotations ###############
    #simple boomerang
    def test_double_right_rot_three_nodes(self):
        self.__tree.insert_element(3)
        self.__tree.insert_element(1)
        self.__tree.insert_element(2)
        self.assertEqual('[ 1, 2, 3 ]', str(self.__tree))
        self.assertEqual('[ 2, 1, 3 ]', self.__tree.pre_order())
        self.assertEqual('[ 1, 3, 2 ]', self.__tree.post_order())

    def test_double_left_rot_three_nodes(self):
        self.__tree.insert_element(1)
        self.__tree.insert_element(3)
        self.__tree.insert_element(2)
        self.assertEqual('[ 1, 2, 3 ]', str(self.__tree))
        self.assertEqual('[ 2, 1, 3 ]', self.__tree.pre_order())
        self.assertEqual('[ 1, 3, 2 ]', self.__tree.post_order())

    def test_height_double_right_rot_three_nodes(self):
        self.__tree.insert_element(3)
        self.__tree.insert_element(1)
        self.__tree.insert_element(2)
        self.assertEqual(2, self.__tree.get_height())

    def test_height_double_left_rot_three_nodes(self):
        self.__tree.insert_element(1)
        self.__tree.insert_element(3)
        self.__tree.insert_element(2)
        self.assertEqual(2, self.__tree.get_height())

    #double rotation with floater in first rotation
    def test_double_right_rot_with_floater(self):
        self.__tree.insert_element(25)
        self.__tree.insert_element(35)
        self.__tree.insert_element(15)
        self.__tree.insert_element(18)
        self.__tree.insert_element(10)
        self.__tree.insert_element(16)
        self.assertEqual('[ 10, 15, 16, 18, 25, 35 ]', str(self.__tree))
        self.assertEqual('[ 18, 15, 10, 16, 25, 35 ]', self.__tree.pre_order())
        self.assertEqual('[ 10, 16, 15, 35, 25, 18 ]', self.__tree.post_order())

    def test_double_left_rot_with_floater(self):
        self.__tree.insert_element(15)
        self.__tree.insert_element(10)
        self.__tree.insert_element(25)
        self.__tree.insert_element(16)
        self.__tree.insert_element(35)
        self.__tree.insert_element(18)
        self.assertEqual('[ 10, 15, 16, 18, 25, 35 ]', str(self.__tree))
        self.assertEqual('[ 16, 15, 10, 25, 18, 35 ]', self.__tree.pre_order())
        self.assertEqual('[ 10, 15, 18, 35, 25, 16 ]', self.__tree.post_order())

    def test_height_double_right_rot_with_floater(self):
        self.__tree.insert_element(25)
        self.__tree.insert_element(35)
        self.__tree.insert_element(15)
        self.__tree.insert_element(18)
        self.__tree.insert_element(10)
        self.__tree.insert_element(16)
        self.assertEqual(3, self.__tree.get_height())

    def test_height_double_left_rot_with_floater(self):
        self.__tree.insert_element(15)
        self.__tree.insert_element(10)
        self.__tree.insert_element(25)
        self.__tree.insert_element(16)
        self.__tree.insert_element(35)
        self.__tree.insert_element(18)
        self.assertEqual(3, self.__tree.get_height())

    #double rotation at inner node, not root
    def test_double_right_rot_at_inner_node(self):
        self.__tree.insert_element(50)
        self.__tree.insert_element(25)
        self.__tree.insert_element(75)
        self.__tree.insert_element(0)
        self.__tree.insert_element(100)
        self.__tree.insert_element(60)
        self.__tree.insert_element(65)
        self.__tree.insert_element(63)
        self.assertEqual('[ 0, 25, 50, 60, 63, 65, 75, 100 ]', str(self.__tree))
        self.assertEqual('[ 50, 25, 0, 75, 63, 60, 65, 100 ]', self.__tree.pre_order())
        self.assertEqual('[ 0, 25, 60, 65, 63, 100, 75, 50 ]', self.__tree.post_order())

    def test_double_left_rot_at_inner_node(self):
        self.__tree.insert_element(19)
        self.__tree.insert_element(70)
        self.__tree.insert_element(10)
        self.__tree.insert_element(80)
        self.__tree.insert_element(1)
        self.__tree.insert_element(15)
        self.__tree.insert_element(12)
        self.__tree.insert_element(13)
        self.assertEqual('[ 1, 10, 12, 13, 15, 19, 70, 80 ]', str(self.__tree))
        self.assertEqual('[ 19, 10, 1, 13, 12, 15, 70, 80 ]', self.__tree.pre_order())
        self.assertEqual('[ 1, 12, 15, 13, 10, 80, 70, 19 ]', self.__tree.post_order())

    def test_height_double_right_rot_at_inner_node(self):
        self.__tree.insert_element(50)
        self.__tree.insert_element(25)
        self.__tree.insert_element(75)
        self.__tree.insert_element(0)
        self.__tree.insert_element(100)
        self.__tree.insert_element(60)
        self.__tree.insert_element(65)
        self.__tree.insert_element(63)
        self.assertEqual(4, self.__tree.get_height())

    def test_height_double_left_rot_at_inner_node(self):
        self.__tree.insert_element(19)
        self.__tree.insert_element(70)
        self.__tree.insert_element(10)
        self.__tree.insert_element(80)
        self.__tree.insert_element(1)
        self.__tree.insert_element(15)
        self.__tree.insert_element(12)
        self.__tree.insert_element(13)
        self.assertEqual(4, self.__tree.get_height())


############### rotations after removals ################
    #local imbalance caused by removal
    def test_removal_single_local_rotation_right(self):
        self.__tree.insert_element(50)
        self.__tree.insert_element(25)
        self.__tree.insert_element(75)
        self.__tree.insert_element(100)
        self.__tree.insert_element(10)
        self.__tree.insert_element(30)
        self.__tree.insert_element(5)
        self.__tree.remove_element(30)
        self.assertEqual('[ 5, 10, 25, 50, 75, 100 ]', str(self.__tree))
        self.assertEqual('[ 50, 10, 5, 25, 75, 100 ]', self.__tree.pre_order())
        self.assertEqual('[ 5, 25, 10, 100, 75, 50 ]', self.__tree.post_order())

    def test_removal_single_local_rotation_left(self):
        self.__tree.insert_element(50)
        self.__tree.insert_element(25)
        self.__tree.insert_element(75)
        self.__tree.insert_element(100)
        self.__tree.insert_element(10)
        self.__tree.insert_element(60)
        self.__tree.insert_element(200)
        self.__tree.remove_element(60)
        self.assertEqual('[ 10, 25, 50, 75, 100, 200 ]', str(self.__tree))
        self.assertEqual('[ 50, 25, 10, 100, 75, 200 ]', self.__tree.pre_order())
        self.assertEqual('[ 10, 25, 75, 200, 100, 50 ]', self.__tree.post_order())

    def test_removal_double_local_rotation_right(self):
        self.__make_big_tree()
        self.__tree.insert_element(35)
        self.__tree.remove_element(20)
        self.__tree.remove_element(45)
        self.assertEqual('[ 30, 35, 40, 50, 55, 60, 65, 70, 75, 100, 125, 150, 200, 300 ]', str(self.__tree))
        self.assertEqual('[ 100, 50, 35, 30, 40, 60, 55, 70, 65, 75, 150, 125, 200, 300 ]', self.__tree.pre_order())
        self.assertEqual('[ 30, 40, 35, 55, 65, 75, 70, 60, 50, 125, 300, 200, 150, 100 ]', self.__tree.post_order())


    def test_removal_double_local_rotation_left(self):
        self.__make_big_tree()
        self.__tree.remove_element(70)
        self.__tree.remove_element(55)
        self.assertEqual('[ 20, 30, 40, 45, 50, 60, 65, 75, 100, 125, 150, 200, 300 ]', str(self.__tree))
        self.assertEqual('[ 100, 50, 40, 30, 20, 45, 65, 60, 75, 150, 125, 200, 300 ]', self.__tree.pre_order())
        self.assertEqual('[ 20, 30, 45, 40, 60, 75, 65, 50, 125, 300, 200, 150, 100 ]', self.__tree.post_order())



    #global imbalance caused by removal - involves branched floaters

    def test_removal_single_global_rotation_left(self):
        self.__make_big_tree()
        self.__tree.remove_element(20)
        self.__tree.remove_element(30)
        self.__tree.remove_element(45)
        self.assertEqual('[ 40, 50, 55, 60, 65, 70, 75, 100, 125, 150, 200, 300 ]', str(self.__tree))
        self.assertEqual('[ 100, 60, 50, 40, 55, 70, 65, 75, 150, 125, 200, 300 ]', self.__tree.pre_order())
        self.assertEqual('[ 40, 55, 50, 65, 75, 70, 60, 125, 300, 200, 150, 100 ]', self.__tree.post_order())

    def test_height_removal_single_global_rotation_left(self):
        self.__make_big_tree()
        self.__tree.remove_element(20)
        self.__tree.remove_element(30)
        self.__tree.remove_element(45)
        self.assertEqual(4, self.__tree.get_height())

    def test_removal_single_global_rotation_right(self):
        self.__make_big_tree()
        self.__tree.remove_element(300)
        self.assertEqual('[ 20, 30, 40, 45, 50, 55, 60, 65, 70, 75, 100, 125, 150, 200 ]', str(self.__tree))
        self.assertEqual('[ 50, 40, 30, 20, 45, 100, 60, 55, 70, 65, 75, 150, 125, 200 ]', self.__tree.pre_order())
        self.assertEqual('[ 20, 30, 45, 40, 55, 65, 75, 70, 60, 125, 200, 150, 100, 50 ]', self.__tree.post_order())

    def test_height_removal_single_global_rotation_right(self):
        self.__make_big_tree()
        self.__tree.remove_element(300)
        self.assertEqual(5, self.__tree.get_height())


    def test_removal_double_global_rotation_left(self):
        self.__make_big_tree()
        self.__tree.insert_element(122)
        self.__tree.insert_element(136)
        self.__tree.insert_element(140)
        self.__tree.remove_element(65)
        self.__tree.remove_element(75)
        self.__tree.remove_element(20)
        self.__tree.remove_element(45)
        self.__tree.remove_element(70)
        self.__tree.remove_element(55)
        self.__tree.remove_element(30)
        self.assertEqual('[ 40, 50, 60, 100, 122, 125, 136, 140, 150, 200, 300 ]', str(self.__tree))
        self.assertEqual('[ 125, 100, 50, 40, 60, 122, 150, 136, 140, 200, 300 ]', self.__tree.pre_order())
        self.assertEqual('[ 40, 60, 50, 122, 100, 140, 136, 300, 200, 150, 125 ]', self.__tree.post_order())

    def test_height_removal_double_global_rotation_left(self):
        self.__make_big_tree()
        self.__tree.insert_element(122)
        self.__tree.insert_element(136)
        self.__tree.insert_element(140)
        self.__tree.remove_element(65)
        self.__tree.remove_element(75)
        self.__tree.remove_element(20)
        self.__tree.remove_element(45)
        self.__tree.remove_element(70)
        self.__tree.remove_element(55)
        self.__tree.remove_element(30)
        self.assertEqual(4, self.__tree.get_height())
 

    def test_removal_double_global_rotation_right(self):
        self.__make_big_tree()
        self.__tree.remove_element(20)
        self.__tree.remove_element(300)
        self.assertEqual('[ 30, 40, 45, 50, 55, 60, 65, 70, 75, 100, 125, 150, 200 ]', str(self.__tree))
        self.assertEqual('[ 60, 50, 40, 30, 45, 55, 100, 70, 65, 75, 150, 125, 200 ]', self.__tree.pre_order())
        self.assertEqual('[ 30, 45, 40, 55, 50, 65, 75, 70, 125, 200, 150, 100, 60 ]', self.__tree.post_order())

    def test_height_removal_double_global_rotation_right(self):
        self.__make_big_tree()
        self.__tree.remove_element(20)
        self.__tree.remove_element(300)
        self.assertEqual(4, self.__tree.get_height())

################### to_list ##################

    def test_to_list(self):
        self.__make_big_tree()
        self.assertEqual([ 20, 30, 40, 45, 50, 55, 60, 65, 70, 75, 100, 125, 150, 200, 300 ], self.__tree.to_list())

    def test_to_list_maintains_value_type(self):
        self.__make_big_tree()
        self.assertEqual(True, isinstance(self.__tree.to_list()[0], int))

    def test_to_list_after_removals(self):
        self.__make_big_tree()
        self.__tree.remove_element(45)
        self.__tree.remove_element(55)
        self.assertEqual([ 20, 30, 40, 50, 60, 65, 70, 75, 100, 125, 150, 200, 300 ], self.__tree.to_list())

if __name__ == '__main__':
    unittest.main()