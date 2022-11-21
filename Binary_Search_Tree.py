class Binary_Search_Tree:

  class __BST_Node:

    def __init__(self, value):
      self.value = value
      self.height = 1
      self.left = None
      self.right = None

  def __init__(self):
    self.__root = None
    self.__length = 0



  def __balance(self,t):
    #determine left and right child balances
    right_balance = 0
    left_balance = 0
    if t.right is not None:
      right_balance = t.right.height
    if t.left is not None:
      left_balance = t.left.height
    #if subtree is unbalanced:
    if (right_balance - left_balance) == -2:
      #determine double rotation balances
      right_2_balance = 0
      left_2_balance = 0
      if t.left.right is not None:
        right_2_balance = t.left.right.height
      if t.left.left is not None:
        left_2_balance = t.left.left.height
      #is double rotation necessary?
      if (right_2_balance - left_2_balance) == 1:
        old_root = t.left
        new_root = t.left.right
        floater = t.left.right.left
        new_root.left = old_root
        old_root.right = floater
        old_root.height = self.__calc_height(old_root)
        new_root.height = self.__calc_height(new_root)
        t.left = new_root
      #rotate right
      old_root = t
      new_root = t.left
      floater = new_root.right
      new_root.right = old_root
      old_root.left = floater
      old_root.height = self.__calc_height(old_root)
      new_root.height = self.__calc_height(new_root)
      return new_root
    elif (right_balance - left_balance) == 2:
      #determine double rotation balances
      right_2_balance = 0
      left_2_balance = 0
      if t.right.right is not None:
        right_2_balance = t.right.right.height
      if t.right.left is not None:
        left_2_balance = t.right.left.height
      #is double rotation necessary? 
      if (right_2_balance - left_2_balance) == -1:
        old_root = t.right
        new_root = t.right.left
        floater = t.right.left.right
        new_root.right = old_root
        old_root.left = floater
        old_root.height = self.__calc_height(old_root)
        new_root.height = self.__calc_height(new_root)
        t.right = new_root
      #rotate left
      old_root = t
      new_root = t.right
      floater = new_root.left
      new_root.left = old_root
      old_root.right = floater
      old_root.height = self.__calc_height(old_root)
      new_root.height = self.__calc_height(new_root)
      return new_root
    else:
      return t

  def to_list(self):
      if self.__root is None:
        return []
      else:
        array = [None] * self.__length
        return self.__recursive_to_list(self.__root,0,array)

  def __recursive_to_list(self, t, index, array):
    if t is None:
      return index
    else:
      index = self.__recursive_to_list(t.left, index, array)
      parent = t.value
      array[index] = parent
      index = self.__recursive_to_list(t.right, index+1, array)
      if t is self.__root:
        return array
      return index



  def __calc_height(self, subroot):
    if (subroot.left is None) and (subroot.right is None):
      return 1
    elif subroot.left is None:
      return subroot.right.height +1
    elif subroot.right is None:
      return subroot.left.height +1
    elif subroot.left.height > subroot.right.height:
      return subroot.left.height +1
    else:
      return subroot.right.height +1    

  def insert_element(self, value):
    self.__root = self.__recursive_insert(value, self.__root)
    self.__length += 1

  def __recursive_insert(self, value, subroot):
    if subroot is None:
      return self.__BST_Node(value)
    elif value == subroot.value:
      raise ValueError
    elif value < subroot.value:
      subroot.left = self.__recursive_insert(value, subroot.left)
      subroot.height = self.__calc_height(subroot)
      return self.__balance(subroot)
    else: # value > subroot.value
      subroot.right = self.__recursive_insert(value, subroot.right)
      subroot.height = self.__calc_height(subroot)
      return self.__balance(subroot)

  def remove_element(self, value):
    self.__root = self.__recursive_removal(value, self.__root) 
    self.__length -= 1

  def __recursive_removal(self, value, subroot):
    if subroot is None: #made it to end of tree: value not found
      raise ValueError
    elif value < subroot.value: #move left
      subroot.left = self.__recursive_removal(value, subroot.left)
      subroot.height = self.__calc_height(subroot)
      return self.__balance(subroot)
    elif value > subroot.value: #move right
      subroot.right = self.__recursive_removal(value, subroot.right)
      subroot.height = self.__calc_height(subroot)
      return self.__balance(subroot)
    else: # value == subroot.value
      if (subroot.left != None) and (subroot.right != None): #subtree has 2 children
        current = subroot.right #move to right subtree
        while current.left != None:
          current = current.left
        subroot.value = current.value #recycle the node, changing its value
        subroot.right = self.__recursive_removal(current.value, subroot.right) #remove the duplicate value
        subroot.height = self.__calc_height(subroot)
        return self.__balance(subroot)
      elif subroot.left is None: #only has right child, or has no children
        return subroot.right
      else: #only has left child
        return subroot.left #return left child to be linked to subroot's original parent

  def in_order(self):
    if self.__root is None:
      return '[ ]'
    else:
      array = [None] * self.__length
      return '[ ' + ', '.join(self.__in_order_recursion(self.__root, 0, array)) + ' ]'

  def __in_order_recursion(self, subroot, index, array):
    if subroot is None:
      return index
    else:
      index = self.__in_order_recursion(subroot.left, index, array)
      parent = str(subroot.value)
      array[index] = parent
      index = self.__in_order_recursion(subroot.right, index+1, array)
      if subroot is self.__root:
        return array
      return index

  def pre_order(self):
    if self.__root is None:
      return '[ ]'
    else:
      array = [None] * self.__length
      return '[ ' + ', '.join(self.__pre_order_recursion(self.__root, 0, array)) + ' ]'

  def __pre_order_recursion(self, subroot, index, array):
    if subroot is None:
      return index
    else:
      parent = str(subroot.value)
      array[index] = parent
      index += 1
      index = self.__pre_order_recursion(subroot.left, index, array)
      index = self.__pre_order_recursion(subroot.right, index, array)
      if subroot is self.__root:
        return array
      return index

  def post_order(self):
    if self.__root is None:
      return '[ ]'
    else:
      array = [None] * self.__length
      return '[ ' + ', '.join(self.__post_order_recursion(self.__root, 0, array)) + ' ]'

  def __post_order_recursion(self, subroot, index, array):
    if subroot is None:
      return index
    else:
      index = self.__post_order_recursion(subroot.left, index, array)
      index = self.__post_order_recursion(subroot.right, index, array)
      parent = str(subroot.value)
      array[index] = parent
      if subroot is self.__root:
        return array
      return index + 1

  def get_height(self):
    if self.__root is None:
      return 0
    return self.__root.height

  def __str__(self):
    return self.in_order()

# if __name__ == '__main__':
#   tree = Binary_Search_Tree()
#   tree.insert_element(50)
#   tree.insert_element(25)
#   tree.insert_element(113)
#   tree.insert_element(14)
#   print(tree.to_list())
  


