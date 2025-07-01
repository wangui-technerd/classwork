class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def InsertAtTheBeginning(self,new_data):
        new_node = Node(new_data)
        new_node.next=self.head
        self.head =new_node

    def InsertAtTheEnd(self,new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head=new_node
            return
        last = self.head
        while last.next:
            last=last.next
        last.next=new_node

    def DeleteFromEnd(self):
        if self.head is None:
            return "Linked List is empty"

        if self.head.next is None:
            self.head = None
            return

        temp=self.head
        while temp.next.next:
            temp = temp.next
        temp.next=None


    def DeleteFromBeginning(self):
        if self.head is None:
            return "The Linked List Is Empty"

        self.head=self.head.next

    def PrintLinkedList(self):
        temp = self.head

        while temp:
            print(temp.data,end=" ")

            temp=temp.next

        print()

if __name__ == '__main__' :
    llist=LinkedList()
    llist.InsertAtTheBeginning("Fox")
    llist.InsertAtTheBeginning("Brown")
    llist.InsertAtTheBeginning("Quick")
    llist.InsertAtTheBeginning("The")

    llist.PrintLinkedList()

    llist.InsertAtTheEnd("Jumps")
    llist.PrintLinkedList()

    llist.DeleteFromEnd()
    llist.PrintLinkedList()

    llist.DeleteFromBeginning()
    llist.PrintLinkedList()

    llist.InsertAtTheBeginning("A")
    llist.PrintLinkedList()