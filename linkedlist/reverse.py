class Node :
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def display(self):
        temp=self.head
        while(temp):
            print(temp.data,end= "")
            temp=temp.next
        print()
    def reverselist(self):
        prev=None
        curr=self.head
        while(curr is not None):
            next=curr.next
            curr.next=prev
            prev=curr
            curr=next
            self.head=prev
l=LinkedList()
l.head=Node(1)
second=Node(2)
third=Node(3)
l.head.next=second
second.next=third
l.display()
l.reverselist()
l.display()
