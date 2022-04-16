from cgi import test
import unittest
from unittest.result import failfast
import datastructures

class TestDLL(unittest.TestCase):

    def setUp(self):
        self.emptyLL = datastructures.DLL()

        node1 = datastructures.Node(4)
        node2 = datastructures.Node(6)
        node3 = datastructures.Node(8)
        node4 = datastructures.Node(10)
        node5 = datastructures.Node(12)
        node6 = datastructures.Node(14)
        node7 = datastructures.Node(16)
        node8 = datastructures.Node(18)
        node9 = datastructures.Node(20)

        self.doublyLL = datastructures.DLL()

        self.doublyLL.pushFirst(node1)
        self.doublyLL.pushLast(node2)
        self.doublyLL.pushLast(node3)
        self.doublyLL.pushLast(node4)
        self.doublyLL.pushLast(node5)
        self.doublyLL.pushLast(node6)
        self.doublyLL.pushLast(node7)
        self.doublyLL.pushLast(node8)
        self.doublyLL.pushLast(node9)

##########################################################

        self.node10 = datastructures.Node(4)
        self.node11 = datastructures.Node(6)
        self.node12 = datastructures.Node(8)
        self.node13 = datastructures.Node(10)
        self.node14 = datastructures.Node(12)
        self.node15 = datastructures.Node(14)
        self.node16 = datastructures.Node(16)
        self.node17 = datastructures.Node(18)
        self.node18 = datastructures.Node(20)
        
        self.udGraph = datastructures.Graph()                                            #                Graph representation:
        self.udGraph.addNode(self.node10)                                                # 
        self.udGraph.addNode(self.node11)                                                #                   4 - 20 - 12 - 10
        self.udGraph.addNode(self.node12)                                                #                  / \ /       \   |
        self.udGraph.addNode(self.node13)                                                #                 6   8         \  |
        self.udGraph.addNode(self.node14)                                                #                      \         \ |
        self.udGraph.addNode(self.node15)                                                #                       18   16 - 14 
        self.udGraph.addNode(self.node16)                                                #
        self.udGraph.addNode(self.node17)                                                #
        self.udGraph.addNode(self.node18)                                                #
        
        self.udGraph.addEdge(self.node10, self.node11)
        self.udGraph.addEdge(self.node10, self.node12)
        self.udGraph.addEdge(self.node10, self.node18)
        self.udGraph.addEdge(self.node12, self.node18)
        self.udGraph.addEdge(self.node12, self.node17)
        self.udGraph.addEdge(self.node18, self.node14)
        self.udGraph.addEdge(self.node14, self.node13)
        self.udGraph.addEdge(self.node13, self.node15)
        self.udGraph.addEdge(self.node15, self.node16)
        self.udGraph.addEdge(self.node15, self.node14)


    def test_isEmptyIsCorrectForEmptyList(self):
        self.assertTrue(self.emptyLL.isEmpty())

    def test_isEmptyIsCorrectForNonEmptyList(self):
        self.assertFalse(self.doublyLL.isEmpty())
    
    def test_pushFirstOnEmptyListWorksCorrectly(self):
        testNode = datastructures.Node(2)
        self.emptyLL.pushFirst(testNode)
        self.assertTrue(self.emptyLL.Start.data == testNode.data and self.emptyLL.End.data == testNode.data)

    def test_pushLastOnEmptyListWorksCorrectly(self):
        testNode = datastructures.Node(2)
        self.emptyLL.pushLast(testNode)
        self.assertTrue(self.emptyLL.Start.data == testNode.data and self.emptyLL.End.data == testNode.data)

    def test_pushFirstWorksCorrectly(self):
        testNode = datastructures.Node(2)
        self.doublyLL.pushFirst(testNode)
        self.assertTrue(self.doublyLL.Start.data == testNode.data)
    
    def test_pushLastWorksCorrectly(self):
        testNode = datastructures.Node(2)
        self.doublyLL.pushLast(testNode)
        self.assertTrue(self.doublyLL.End.data == testNode.data)

    def test_deleteFirstThrowsExceptionForEmptyList(self):
        with self.assertRaises(Exception):
            self.emptyLL.deleteFirst()

    def test_deleteLastThrowsExceptionForEmptyList(self):
        with self.assertRaises(Exception):
            self.emptyLL.deleteLast()

    def test_deleteFirstWorksCorrectlyForListWithOneNode(self):
        testNode = datastructures.Node(2)
        self.emptyLL.pushFirst(testNode)
        self.emptyLL.deleteFirst()
        self.assertTrue(self.emptyLL.size() == 0)

    def test_deleteLastWorksCorrectlyForListWithOneNode(self):
        testNode = datastructures.Node(2)
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
        
    def test_insertThrowsExceptionForIndexLessThanZeroAndGreaterThanSize(self):
        testNode = datastructures.Node(2)        
        with self.assertRaises(Exception):
            self.emptyLL.insert(testNode, -1)
            self.emptyLL.insert(testNode, 2)
            
    def test_insertWorksCorrectly(self):
        testNode = datastructures.Node(2)
        oldNodeAtIndex = self.doublyLL.get(5)
        nodeAtIndexMinusOne = oldNodeAtIndex.Previous
        self.doublyLL.insert(testNode, 5)
        nodeAtIndex = self.doublyLL.get(5)
        self.assertTrue(testNode.data == nodeAtIndex.data)
        self.assertTrue(nodeAtIndex.Previous == nodeAtIndexMinusOne)
        self.assertTrue(nodeAtIndex.Next == oldNodeAtIndex)
    
    def test_insertWorksCorrectlyWhenInsertingAtIndexEqualToSize(self):
        testNode = datastructures.Node(2)
        self.doublyLL.insert(testNode, 9)
        nodeAtIndex = self.doublyLL.get(9)
        self.assertTrue(testNode.data == nodeAtIndex.data)
        self.assertTrue(nodeAtIndex.Next == None)
        self.assertTrue(nodeAtIndex.Previous == self.doublyLL.get(8))
    
    def test_deleteThrowsExceptionForIndexLessThanZeroAndGreaterThanSizeAndEmptyList(self):     
        with self.assertRaises(Exception):
            self.doublyLL.delete(-1)
            self.doublyLL.delete(2)
            self.emptyLL.delete(2)
    
    def test_deleteWorksCorrectly(self):
        expectedNode = self.doublyLL.get(6)
        deletedNode = self.doublyLL.get(5)
        nodeBeforeDeletedNode = deletedNode.Previous
        self.doublyLL.delete(5)
        actualNode = self.doublyLL.get(5)
        self.assertTrue(expectedNode.data == actualNode.data)
        self.assertTrue(expectedNode.Previous == nodeBeforeDeletedNode)
        self.assertTrue(nodeBeforeDeletedNode.Next == expectedNode)

    def test_goForwardWorksCorrectly(self):
        oldCurrent = self.doublyLL.current
        self.doublyLL.goForward()
        self.assertTrue(self.doublyLL.current.data == oldCurrent.Next.data)

    def test_goBackwardWorksCorrectly(self):
        self.doublyLL.goForward()
        oldCurrent = self.doublyLL.current
        self.doublyLL.goBackward()
        self.assertTrue(self.doublyLL.current.data == oldCurrent.Previous.data)
    
    def test_goForwardRaisesExceptionWhenOnlyOneNodeInList(self):
        testNode = datastructures.Node(2)
        self.emptyLL.pushFirst(testNode)
        with self.assertRaises(Exception):
            self.emptyLL.goForward()
            
    def test_goBackwardRaisesExceptionWhenOnlyOneNodeInList(self):
        testNode = datastructures.Node(2)
        self.emptyLL.pushFirst(testNode)
        with self.assertRaises(Exception):
            self.emptyLL.goBackward()
            
    def test_goForwardRaisesExceptionForEmptyList(self):
        with self.assertRaises(Exception):
            self.emptyLL.goForward()
    
    def test_goBackwardRaisesExceptionForEmptyList(self):
        with self.assertRaises(Exception):
            self.emptyLL.goBackward()
    
    def test_goForwardRaisesExceptionWhenAlreadyAtLastNode(self):
        self.doublyLL.current = self.doublyLL.get(8)
        with self.assertRaises(Exception):
            self.emptyLL.goForward()
    
    def test_goBackwardRaisesExceptionWhenAlreadyAtFirstNode(self):
        self.doublyLL.current = self.doublyLL.get(0)
        with self.assertRaises(Exception):
            self.emptyLL.goBackward()
    
    def test_sizeWorksCorrectlyForEmptyList(self):
        self.assertTrue(self.emptyLL.size() == 0)

    def test_sizeWorksCorrectlyForListWithOneNode(self):
        testNode = datastructures.Node(2)
        self.emptyLL.pushFirst(testNode)
        self.assertTrue(self.emptyLL.size() == 1)

    def test_sizeWorksCorrectlyForNonEmptyList(self):
        self.assertTrue(self.doublyLL.size() == 9) 
    
    def test_sizeDecrementsByOneWhenDeletingNode(self):
        originalSize = self.doublyLL.size()
        self.doublyLL.deleteFirst()
        self.assertTrue(self.doublyLL.size() == originalSize - 1)
        
    def test_sizeIncrementsByOneWhenPushingNode(self):
        testNode = datastructures.Node(2)
        originalSize = self.doublyLL.size()
        self.doublyLL.pushFirst(testNode)
        self.assertTrue(self.doublyLL.size() == originalSize + 1)

    def test_containsWorksCorrectlyForEmptyList(self):
        testNode = datastructures.Node(2)
        self.assertTrue(self.emptyLL.contains(testNode) == (False, -1))

    def test_containsWorksCorrectlyForNonEmptyList(self):
        testNode = datastructures.Node(200)
        nodeThatExists = datastructures.Node(4)
        nodeThatExists2 = datastructures.Node(20)
        
        self.assertTrue(self.doublyLL.contains(testNode) == (False, -1))
        self.assertTrue(self.doublyLL.contains(nodeThatExists) == (True, 0))
        self.assertTrue(self.doublyLL.contains(nodeThatExists2) == (True, 8))
    
    def test_getRaisesExceptionForEmptyList(self):
        with self.assertRaises(Exception):
            self.emptyLL.get(0)
            
    def test_getRaisesExceptionForIndexOutOfBounds(self):
        with self.assertRaises(Exception):
            self.doublyLL.get(15)
            
    def test_getWorksCorrectlyForListWithOneNode(self):
        testNode = datastructures.Node(2)
        self.emptyLL.pushFirst(testNode)
        expectedNode = self.emptyLL.Start
        
        self.assertTrue(expectedNode.data == self.emptyLL.get(0).data)
    
    def test_getWorksCorrectlyForLastNode(self):
        expectedData = 20
        actualData = self.doublyLL.get(8).data
        
        self.assertTrue(expectedData == actualData)
    
    def test_getWorksCorrectly(self):
        expectedData = 12
        actualData = self.doublyLL.get(4).data
        
        self.assertTrue(expectedData == actualData)
        
##########################################################################################################################################################################

    def test_addNodeWorksCorrectly(self):
        testNode = datastructures.Node(2)
        self.udGraph.addNode(testNode)
        self.assertTrue(testNode in self.udGraph.nodeList)
        
    def test_addEdgeWorksCorrectlyForNodesAlreadyInGraph(self):
        self.udGraph.addEdge(self.node16, self.node17)
        boolean = self.udGraph.hasEdge(self.node16, self.node17)
        self.assertTrue(boolean)

    def test_addEdgeWorksCorrectlyForNewNodes(self):
        testNode1 = datastructures.Node(30)
        testNode2 = datastructures.Node(40)
        self.udGraph.addEdge(testNode1, testNode2)
        self.assertTrue(testNode1 in self.udGraph.nodeList)
        self.assertTrue(testNode2 in self.udGraph.nodeList)
        self.assertTrue(self.udGraph.hasEdge(testNode1, testNode2))

    def test_hasEdgeWorksCorrectlyForNonExistantEdge(self):
        testTuple = self.udGraph.hasEdge(self.node16, self.node17)
        self.assertFalse(testTuple[0])
    
    def test_hasEdgeWorksCorrectlyForExistantEdge(self):
        testTuple = self.udGraph.hasEdge(self.node10, self.node11)
        self.assertTrue(testTuple[0])
    
    def test_removeEdgeWorksCorrectly(self):
        #TODO
        self.fail()
        
    def test_setCurrentNodeWorksCorrectly(self):
        #TODO
        self.fail()
    
    def test_traverseWorksCorrectly(self):
        #TODO
        self.fail()
        
    if __name__ == "__main__":
        unittest.main()