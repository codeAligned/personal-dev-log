# BST Successor Search
# In a Binary Search Tree (BST), an Inorder Successor of a node is defined as the node with the smallest key greater than the key of the input node (see examples below). Given a node inputNode in a BST, you're asked to write a function findInOrderSuccessor that returns the Inorder Successor of inputNode. If inputNode has no Inorder Successor, return null.
#
# Explain your solution and analyze its time and space complexities.
#
# alt In this diagram, the inorder successor of 9 is 11 and the inorder successor of 14 is 20.
#
# Example:
#
#            20
#           /  \
#          9    25
#         / \
#        5   12
#            / \
#          11   14
#
# In the diagram above, for inputNode whose key = 11
#
# Your function would return:
#
# The Inorder Successor node whose key = 12
#
# Constraints:
#
# [time limit] 5000ms
# [input] Node inputNode
# [output] Node



#########################################################
# CODE INSTRUCTIONS:                                    #
# 1) The method findInOrderSuccessor you're asked      #
#    to implement is located at line 30.                #
# 2) Use the helper code below to implement it.         #
# 3) In a nutshell, the helper code allows you to       #
#    to build a Binary Search Tree.                     #
# 4) Jump to line 88 to see an example for how the      #
#    helper code is used to test findInOrderSuccessor.  #
#########################################################


# A node
class Node:

  # Constructor to create a new node
  def __init__(self, key):
    self.key = key
    self.left = None
    self.right = None
    self.parent = None

# A binary search tree
class BinarySearchTree:

  # Constructor to create a new BST
  def __init__(self):
    self.root = None

  # ================ Review 2 =================

  def find_in_order_successor(self, inputNode):
    if self.there_is_node_to_the_right(inputNode):
      output = self.get_left_most_node(inputNode.right)
      return output

    else:
      parent = inputNode.parent
      while parent != None:
        if parent.key > inputNode.key:
          return parent
        parent = parent.parent

      return None

  def there_is_node_to_the_right(self,node):
    if node.right == None:
      return False
    return True

  def get_left_most_node(self,node):
    temp_node = node

    while temp_node.left != None:
      temp_node = temp_node.left

    return temp_node

  # ================ Review 3 ====================

   def find_in_order_successor(self, inputNode):
    if self.there_is_node_to_right(inputNode):
      temp_node = inputNode.right

      while temp_node.left != None:
        temp_node = temp_node.left

    else:
      temp_val = inputNode.key
      temp_node = inputNode.parent

      while temp_node.key < temp_val:
        temp_node = temp_node.parent

        if temp_node == None:
          break

    output = temp_node
    return output

  def there_is_node_to_right(self, node):
    if node.right == None:
      return False
    return True

  # Given a binary search tree and a number, inserts a
  # new node with the given number in the correct place
  # in the tree. Returns the new root pointer which the
  # caller should then use(the standard trick to avoid
  # using reference parameters)
  def insert(self, key):

    # 1) If tree is empty, create the root
    if (self.root is None):
      self.root = Node(key)
      return

    # 2) Otherwise, create a node with the key
    #    and traverse down the tree to find where to
    #    to insert the new node
    currentNode = self.root
    newNode = Node(key)
    while(currentNode is not None):

      if(key < currentNode.key):
        if(currentNode.left is None):
          currentNode.left = newNode
          newNode.parent = currentNode
          break
        else:
          currentNode = currentNode.left
      else:
        if(currentNode.right is None):
          currentNode.right = newNode
          newNode.parent = currentNode
          break
        else:
          currentNode = currentNode.right

  # Return a reference to a node in the BST by its key.
  # Use this method when you need a node to test your
  # findInOrderSuccessor function on
  def getNodeByKey(self, key):

    currentNode = self.root
    while(currentNode is not None):
      if(key == currentNode.key):
        return currentNode

      if(key < currentNode.key):
        currentNode = currentNode.left
      else:
        currentNode = currentNode.right

    return None

#########################################
# Driver program to test above function #
#########################################

# Create a Binary Search Tree
bst  = BinarySearchTree()
bst.insert(20)
bst.insert(9)
bst.insert(25)
bst.insert(5)
bst.insert(12)
bst.insert(11)
bst.insert(14)

# Get a reference to the node whose key is 9
test = bst.getNodeByKey(25)

# Find the in order successor of test
succ = bst.find_in_order_successor(test)

# Print the key of the successor node
if succ is not None:
    print ("\nInorder Successor of %d is %d " \
            %(test.key , succ.key))
else:
    print ("\nInorder Successor doesn't exist")
