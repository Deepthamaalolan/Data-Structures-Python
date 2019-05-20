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
    def deletelist(self):
        curr=self.head
        while curr:
            p=curr.next
            del curr.data
            curr=p
    def delete(self,key):
        temp=self.head
        if temp is not None:
            if (temp.data==key):
                self.next=temp.next
                temp=None
        while(temp is not None):
                if (temp.data==key):
                    break
                prev=temp
                temp=temp.next
                if (temp==None):
                    return
                prev.next=temp.next
                temp=None
    def deleteatany(self,pos):
        temp=self.head
        if (temp==None):
            return
        if (pos==0):
            self.head=temp.next
            temp=None
            return
        for i in range (pos-1):
            temp=temp.next
            if (temp is None):
                break
        if (temp is None):
            return
        if(temp.next is None):
            return
        next=temp.next.next
        temp.next=None
        temp.next=next
l=LinkedList()
l.head=Node(1)
second=Node(3)
third=Node(4)
four=Node(5)
l.head.next=second
second.next=third
third.next=four
l.display()
l.delete(3)
l.display()
l.deleteatany(2)
l.display()
l.deletelist()
