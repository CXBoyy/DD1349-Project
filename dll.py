# Todo: Doubly Linked List

class Node():
    def __init__(self, data):
        self.data = data
        self.Next = None
        self.Previous = None

class Edge():
    def __init__(self, node1:Node, node2:Node):
        self.node1 = node1
        self.node2 = node2
   
class DLL():
    def __init__(self):
        self.Start : Node = None
        self.End : Node = None
        self.current : Node = None

    def pushFirst(self, node:Node):
        newNode = node
        
        if self.isEmpty():
            self.Start, self.End = newNode, newNode
            newNode.Next = newNode
            self.current = self.Start
        else:
            oldStart = self.Start
            self.Start = newNode
            newNode.Next = oldStart
            oldStart.Previous = newNode

    def pushLast(self, node : Node):
        newNode = node

        if self.isEmpty():
            self.Start, self.End = newNode, newNode
            newNode.Next, newNode.Previous = newNode, newNode
            self.current = self.End
        else:
            oldEnd = self.End
            self.End = newNode
            newNode.Previous = oldEnd
            oldEnd.Next = newNode

    def isEmpty(self):
        return self.Start == None and self.End == None
    
    def goForward(self):
        if self.isEmpty():
            raise Exception("List is empty.")
        if self.size() == 1:
            self.current = None
        else:
            self.current = self.current.Next
    
    def goBackward(self):
        self.current = self.current.Previous
    
    def deleteFirst(self):
        if self.isEmpty():
            raise Exception("List is empty.")
        elif self.Start.Next == self.Start:
            self.Start = None
            self.End = None
        else:
            oldStart = self.Start
            self.Start = oldStart.Next
            self.Start.Previous = None
            if self.Start.Next == None:
                self.Start.Next = self.Start
        
    def deleteLast(self):
        if self.isEmpty():
            raise Exception("List is empty.")
        elif self.size() == 1:
            print("\nSize is 1.")
            self.Start = None
            self.End = None
        else:
            newEnd = self.End.Previous
            self.End = newEnd
            self.End.Next = None
            if self.End.Previous == None:
                self.End.Next = self.Start
    
    def size(self):
        if self.isEmpty():
            return 0
        else:
            currentNode = self.Start
            counter = 1
            while(currentNode != None and currentNode.Next != None and currentNode.Next.data != currentNode.data):
                if self.Start == self.End:
                    break
                print(self.current.data)
                counter += 1
                currentNode = currentNode.Next
            return counter
    
    def contains(self, node:Node):
        if self.isEmpty():
            return False
        else:
            currentNode = self.Start
            while currentNode != None:
                if currentNode.data == node.data:
                    return True
                currentNode = currentNode.Next
            return False


# An undirected unweighted graph. 
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
                
            


    
