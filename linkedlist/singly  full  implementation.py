class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init(self):
        self.head=None
    def display(self):
        temp=self.head
        while(temp):
            print(temp.data,end=" ")
            temp=temp.next
        print()
    def insertatbegin(self,newdata):
        newnode=Node(newdata)
        newnode.next=self.head
        self.head=newnode
    def insertatany(self,val,newdata):
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
    def search(self,key):
        curr=self.head
        while curr!=None:
            if  curr.data==key:
                return True
            curr=curr.next
        return False
    def deletekey(self,key):
        temp=self.head
        if temp is not None:
            if(temp.data==key):
                self.next=temp.next
                temp=None
        while(temp is not None):
            if(temp.data==key):
                break
            prev=temp
            temp=temp.next
        if(temp==None):
            return
        prev.next=temp.next
        temp=None
    def deleteposition(self,pos):
        temp=self.head
        if temp==None:
            return
        if pos==0:
            self.head=temp.next
            temp=None
            return
        for i in range(pos-1):
            temp=temp.next
            if temp is None:
                break
        if temp is None:
            return
        if temp.next is None:
            return
        next=temp.next.next
        temp.next=None
        temp.next=next
l=LinkedList()
l.head=Node(1)
second=Node(2)
third=Node(3)
l.head.next=second
second.next=third
print("The list contains")
l.display()
print("Insert 5 at beginning")
l.insertatbegin(5)
l.display()
print("insert 7 at middle")
l.insertatany(2,7)
l.display()

print("insert 10 at end")
l.insertatend(10)
l.display()
print("Delete the data key=2")
l.deletekey(2)
l.display()
print("delete the node at position=4")
l.deleteposition(4)
l.display()
print("Search result of 1 is",l.search(1))
