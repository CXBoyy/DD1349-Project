from cgi import test
import unittest
import dll

class TestDLL(unittest.TestCase):

    def setUp(self):
        self.emptyLL = dll.DLL()

        node1 = dll.Node(4)
        node2 = dll.Node(6)
        node3 = dll.Node(8)
        node4 = dll.Node(10)
        node5 = dll.Node(12)
        node6 = dll.Node(14)
        node7 = dll.Node(16)
        node8 = dll.Node(18)
        node9 = dll.Node(20)

        self.doublyLL = dll.DLL()

        self.doublyLL.pushFirst(node1)
        self.doublyLL.pushLast(node2)
        self.doublyLL.pushLast(node3)
        self.doublyLL.pushLast(node4)
        self.doublyLL.pushLast(node5)
        self.doublyLL.pushLast(node6)
        self.doublyLL.pushLast(node7)
        self.doublyLL.pushLast(node8)
        self.doublyLL.pushLast(node9)

    def test_isEmptyIsCorrectForEmptyList(self):
        self.assertTrue(self.emptyLL.isEmpty())

    def test_isEmptyIsCorrectForNonEmptyList(self):
        self.assertFalse(self.doublyLL.isEmpty())
    
    def test_pushFirstOnEmptyListWorksCorrectly(self):
        testNode = dll.Node(2)
        self.emptyLL.pushFirst(testNode)
        self.assertTrue(self.emptyLL.Start == testNode and self.emptyLL.End == testNode)

    def test_pushLastOnEmptyListWorksCorrectly(self):
        testNode = dll.Node(2)
        self.emptyLL.pushLast(testNode)
        self.assertTrue(self.emptyLL.Start == testNode and self.emptyLL.End == testNode)

    def test_pushFirstWorksCorrectly(self):
        testNode = dll.Node(2)
        self.doublyLL.pushFirst(testNode)
        self.assertTrue(self.doublyLL.Start == testNode)
    
    def test_pushLastWorksCorrectly(self):
        testNode = dll.Node(2)
        self.doublyLL.pushLast(testNode)
        self.assertTrue(self.doublyLL.End == testNode)

    def test_deleteFirstThrowsExceptionForEmptyList(self):
        with self.assertRaises(Exception):
            self.emptyLL.deleteFirst()

    def test_deleteLastThrowsExceptionForEmptyList(self):
        with self.assertRaises(Exception):
            self.emptyLL.deleteLast()

    def test_deleteFirstWorksCorrectlyForListWithOneNode(self):
        testNode = dll.Node(2)
        self.emptyLL.pushFirst(testNode)
        self.emptyLL.deleteFirst()
        self.assertTrue(self.emptyLL.size() == 0)

    def test_deleteLastWorksCorrectlyForListWithOneNode(self):
        testNode = dll.Node(2)
        self.emptyLL.pushFirst(testNode)
        self.emptyLL.deleteLast()
        self.assertTrue(self.emptyLL.size() == 0)

    def test_deleteFirstWorksCorrectly(self):
        expectedNewFirst = self.doublyLL.Start.Next
        self.doublyLL.deleteFirst()
        self.assertTrue(self.doublyLL.Start.data == expectedNewFirst.data)
        self.assertTrue(self.doublyLL.Start.Previous == None)

    def test_deleteLastWorksCorrectly(self):
        expectedNewLast = self.doublyLL.End.Previous
        self.doublyLL.deleteLast()
        self.assertTrue(self.doublyLL.End.data == expectedNewLast.data)
        self.assertTrue(self.doublyLL.End.Next == None)

    def test_goForwardWorksCorrectly(self):
        oldCurrent = self.doublyLL.current
        self.doublyLL.goForward()
        self.assertTrue(self.doublyLL.current.data == oldCurrent.Next.data)

    def test_goBackwardWorksCorrectly(self):
        self.doublyLL.goForward()
        oldCurrent = self.doublyLL.current
        self.doublyLL.goBackward()
        self.assertTrue(self.doublyLL.current.data == oldCurrent.Previous.data)
    
    def test_sizeWorksCorrectlyForEmptyList(self):
        self.assertTrue(self.emptyLL.size() == 0)

    def test_sizeWorksCorrectlyForListWithOneNode(self):
        testNode = dll.Node(2)
        self.emptyLL.pushFirst(testNode)
        self.assertTrue(self.emptyLL.size() == 1)

    def test_sizeWorksCorrectlyForNonEmptyList(self):
        self.assertTrue(self.doublyLL.size() == 9) 

    def test_containsWorksCorrectlyForEmptyList(self):
        testNode = dll.Node(2)
        self.assertFalse(self.emptyLL.contains(testNode))

    def test_containsWorksCorrectlyForNonEmptyList(self):
        testNode = dll.Node(200)
        nodeThatExists = dll.Node(4)
        nodeThatExists2 = dll.Node(20)
        self.assertFalse(self.doublyLL.contains(testNode))
        self.assertTrue(self.doublyLL.contains(nodeThatExists))
        self.assertTrue(self.doublyLL.contains(nodeThatExists2))

    if __name__ == "__main__":
        unittest.main()