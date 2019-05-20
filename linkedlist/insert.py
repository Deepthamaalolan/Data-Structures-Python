class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def display(self):
        temp=self.head
        while(temp):
            print(temp.data,end=" ")
            temp=temp.next
    def insertatbegin(self,newdata):
        newnode=Node(newdata)
        newnode.next=self.head
        self.head=newnode
    def insertatgiven(self,val,newdata):
        newnode=Node(newdata)
        if self.head!=None:
            temp=self.head
            while temp.data!=val:
                temp=temp.next
                if temp.next==None:
                    print("Value not in list")
                    return
        newnode.next=temp.next
        temp.next=newnode
                
    def insertatend(self,newdata):
        newnode=Node(newdata)
        if self.head==None:
            self.head=newnode
            return
        last=self.head
        while(last.next):
            last=last.next
        last.next=newnode
        
l=LinkedList()
l.head=Node(1)
second=Node(2)
third=Node(3)
l.head.next=second
second.next=third
print("The list contains")
l.display()
print("AFTER INSERTING 5 at the beginning")
l.insertatbegin(5)
l.display()
print("After inserting after a given value 1")
l.insertatgiven(1,8)
l.display()
print("After inserting at the end")
l.insertatend(9)
l.display()
    
