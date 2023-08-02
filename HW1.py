class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

class SLinkedList:
    def __init__(self):
        self.headval = None

# Print the linked list
    def listprint(self):
        printval = self.headval
        while printval is not None:
            print (printval.dataval)
            printval = printval.nextval
            
    def AtBegining(self,newdata):
        NewNode = Node(newdata)

# Update the new nodes next val to existing node
        NewNode.nextval = self.headval
        self.headval = NewNode
        
# Function to add newnode
    def AtEnd(self, newdata):
        NewNode = Node(newdata)
        if self.headval is None:
            self.headval = NewNode
            return
        laste = self.headval
        while(laste.nextval):
            laste = laste.nextval
        laste.nextval=NewNode

# Function to add node
    def Inbetween(self,middle_node,newdata):
        if middle_node is None:
            print("The mentioned node is absent")
            return

        NewNode = Node(newdata)
        NewNode.nextval = middle_node.nextval
        middle_node.nextval = NewNode
        
# Function to remove node
    def RemoveNode(self, Removekey):

        HeadVal = self.headval

        if (HeadVal is not None):
            if (HeadVal.dataval == Removekey):
                self.headval = HeadVal.nextval
                HeadVal = None
                return

        while (HeadVal is not None):
            if HeadVal.dataval == Removekey:
                break
            prev = HeadVal
            HeadVal = HeadVal.nextval

        if (HeadVal == None):
            return

        prev.nextval = HeadVal.nextval

        HeadVal = None

list1 = SLinkedList()
list1.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")

# Link first Node to second node
list1.headval.nextval = e2

# Link second Node to third node
e2.nextval = e3

print("遍歷:")
list1.listprint()

list2 = SLinkedList()
list2.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")

list2.headval.nextval = e2
e2.nextval = e3

list2.AtBegining("Sun")

print("在開頭插入Sun:")
list2.listprint()

list3 = SLinkedList()
list3.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")

list3.headval.nextval = e2
e2.nextval = e3

list3.AtEnd("Thu")

print("在末尾插入Thu:")
list3.listprint()

list4 = SLinkedList()
list4.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Thu")

list4.headval.nextval = e2
e2.nextval = e3

list4.Inbetween(list4.headval.nextval,"Fri")

print("在Tue和Thu之間插入Fri:")
list4.listprint()

llist = SLinkedList()
llist.AtBegining("Mon")
llist.AtBegining("Tue")
llist.AtBegining("Wed")
llist.AtBegining("Thu")
print("原始:")
llist.listprint()
llist.RemoveNode("Tue")
print("刪除Tue:")
llist.listprint()