import unittest
from minimal_tree import BinarySearchTree, Node

class TestMinimalTree(unittest.TestCase):
	def setUp(self):
		self.a1 = [1,2,3,4,5,6,7]
		self.a2 = [1,2,3,4]


	def test_create_bst(self):
		# exercise
		rootNode = BinarySearchTree.create_bst(0, 6, self.a1)
		rootNode2 = BinarySearchTree.create_bst(0, 3, self.a2)

		# verify
		self.assertEqual(rootNode.data, 4)
		self.assertEqual(rootNode.leftChild.data, 2)
		self.assertEqual(rootNode.rightChild.data, 6)
		self.assertEqual(rootNode.leftChild.leftChild.data, 1)
		self.assertEqual(rootNode.leftChild.rightChild.data, 3)
		self.assertEqual(rootNode.rightChild.leftChild.data, 5)
		self.assertEqual(rootNode.rightChild.rightChild.data, 7)

		self.assertEqual(rootNode2.data, 2)
		self.assertEqual(rootNode2.leftChild.data, 1)
		self.assertEqual(rootNode2.rightChild.data, 3)
		self.assertEqual(rootNode2.rightChild.rightChild.data, 4)


if __name__ == '__main__':
	unittest.main()