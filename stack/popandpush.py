class stack:
    def __init__(self):
        self.items=[]
    def isempty(self):
        return self.items==[]
    def push(self,data):
        self.items.append(data)
    def pop(self):
        return self.items.pop()
    def display(self):
        print( self.items)
s=stack()
print("1.push\n2.pop\n3.display\nEnter your choice")
n=int(input())
if(n==1):
    x=input("Enter the item to be push")
    s.push(x)
    s.display()
elif(n==2):
    if s.isempty():
        print("The stack is empty")
    else:
        print("poped value",s.pop())
    s.display()
elif n==3:
    if s.isempty():
        print("The stack is empty")
    else:
        print("the stack contains",s.display())
else:
    print("Invalid option")
