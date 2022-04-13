
# A class representing a node for use in an Undirected Graph or Doubly Linked List
class Node():
    def __init__(self, data):
        self.data = data
        self.Next = None
        self.Previous = None

class Edge():
    def __init__(self, node1:Node, node2:Node):
        self.node1 = node1
        self.node2 = node2

# A class representing a Doubly Linked List
class DLL():
    def __init__(self):
        self.Start : Node = None
        self.End : Node = None
        self.current : Node = None
        self.Size = 0

    # Inserts a node at a specific index, so that the new node
    # will be placed at the specified index.
    # Raises an exception if index is out of bounds.
    def insert(self, node:Node, index:int):
        if index < 0 or index > self.size():
            raise Exception("Index out of bounds.")
        if self.isEmpty():
            self.pushFirst(node)
        if index == self.size():
            self.pushLast(node)
        else:
            currentNodeAtIndex = self.get(index)
            nodeAtIndexMinusOne = currentNodeAtIndex.Previous
            if nodeAtIndexMinusOne != None:
                nodeAtIndexMinusOne.Next = node
            currentNodeAtIndex.Previous = node
            node.Next = currentNodeAtIndex
            node.Previous = nodeAtIndexMinusOne
    
    # Deletes the node at a given index.
    # Raises an exception if the list is empty
    # or if the index is out of bounds.
    def delete(self, index:int):
        if index < 0 or index >= self.size():
            raise Exception("Index out of bounds.")
        if self.isEmpty():
            raise Exception("List is empty.")
        else:
            nodeToDelete = self.get(index)
            previousNode = nodeToDelete.Previous
            nextNode = nodeToDelete.Next
            if previousNode != None:
                previousNode.Next = nextNode
            if nextNode != None:
                nextNode.Previous = previousNode
    
    # Pushes/inserts a node to the beginning of the list.
    def pushFirst(self, node:Node):
        newNode = node
        
        if self.isEmpty():
            self.Start, self.End = newNode, newNode
            newNode.Next = newNode
            self.current = self.Start
            self.Size += 1
        else:
            oldStart = self.Start
            self.Start = newNode
            newNode.Next = oldStart
            oldStart.Previous = newNode
            self.Size += 1

    # Pushes/inserts a node to the end of the list.
    def pushLast(self, node : Node):
        newNode = node

        if self.isEmpty():
            self.Start, self.End = newNode, newNode
            newNode.Next, newNode.Previous = newNode, newNode
            self.current = self.End
            self.Size += 1
        else:
            oldEnd = self.End
            self.End = newNode
            newNode.Previous = oldEnd
            oldEnd.Next = newNode
            self.Size += 1
    
    # Checks if the Linked List is empty or not.    
    # An empty Linked List is defined as one with no Start or End nodes.
    # Returns True if the List has no Start or End node
    # Returns False otherwise
    def isEmpty(self):
        return self.Start == None and self.End == None
    
    # Moves the "current" node forward by one
    # Raises an exception if the list is empty
    # or if you are already at the last node.
    def goForward(self):
        if self.isEmpty():
            raise Exception("List is empty.")
        if self.size() == 1 or self.current.Next == None:
            raise Exception("Already at the last node.")
        else:
            self.current = self.current.Next
    
    # Moves the "current" node backward by one.
    # Raises an exception if the list is empty
    # or if you are already at the first node.
    def goBackward(self):
        if self.isEmpty():
            raise Exception("List is empty.")
        if self.size() == 1 or self.current.Previous == None:
            raise Exception("Already at the first node.")
        else:
            self.current = self.current.Previous
    
    # Deletes the first node in the list.
    def deleteFirst(self):
        if self.isEmpty():
            raise Exception("List is empty.")
        elif self.Start.Next == self.Start:
            self.Start = None
            self.End = None
            self.Size -= 1
        else:
            oldStart = self.Start
            self.Start = oldStart.Next
            self.Start.Previous = None
            if self.Start.Next == None:
                self.Start.Next = self.Start
            self.Size -= 1
      
    # Deletes the last element in the list.  
    def deleteLast(self):
        if self.isEmpty():
            raise Exception("List is empty.")
        elif self.End.Next == self.End:
            self.Start = None
            self.End = None
            self.Size -= 1
        
        else:
            newEnd = self.End.Previous
            self.End = newEnd
            self.End.Next = None
            if self.End.Previous == None:
                self.End.Next = self.Start
            self.Size -= 1
    
    # Returns the size of the Linked List
    def size(self):
        return self.Size
    
    # A function to check if a node exists within the DLL and what its index is.
    # Returns True and the index of the node if the node is in the list.
    # Returns False and -1 if the node is not in the list.
    def contains(self, node:Node):
        if self.isEmpty():
            return False, -1
        else:
            index = 0
            currentNode = self.Start
            while currentNode != None:
                if currentNode.data == node.data:
                    return True, index
                currentNode = currentNode.Next
                index += 1
            return False, -1
    
    # Returns the node at a given index.
    # Raises an exception if the DLL is empty or if the index is out of bounds.
    def get(self, index:int):
        if self.isEmpty():
            raise Exception("List is empty.")
        if index >= self.size() or index < 0:
            raise Exception("Index out of bounds.")
        
        i = 0
        currentNode = self.Start
        while i < index:
            currentNode = currentNode.Next
            i += 1
        return currentNode


# A class representing an undirected unweighted graph. 
class Graph():
    def __init__(self):
        self.nodeList = list()
        self.adjacencyList : dict[Node, DLL] = dict()

    # Function to add a node to a list of all nodes in the graph
    # Duplicates are not allowed. If the node was not already in the list, return True.
    # If the node was already in the list, return False.
    def add_node(self, node:Node):
        if node not in self.nodeList:
            self.nodeList.append(node)
            return True
        else:
            return False

    # Function to add an edge.
    # Returns true if the edge was added.
    # Returns false if the edge already existed.
    def add_edge(self, node1:Node, node2:Node):
        value = self.adjacencyList[node1]
        if value == None:
            doublyLinkedList1 = DLL()
            doublyLinkedList1.pushLast(node2)
            doublyLinkedList2 = DLL()
            doublyLinkedList2.pushLast(node1)
            self.adjacencyList[node1] = doublyLinkedList1
            self.adjacencyList[node2] = doublyLinkedList2
            return True
        else:
            if not value.contains(node2):
                value.pushLast(node2)
                self.adjacencyList[node2].pushLast(node1)
                return True
            else:
                return False
                
            


    
