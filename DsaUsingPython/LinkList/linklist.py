class node:
    def __init__(self,data):
        self.data=data
        self.nxt=None
class linklist:
    def __init__(self):
        self.head=None
        self.size=0
        self.last=None


    def push_beg(self,data):
        temp=node(data)
        if(self.size==0):
            self.head=temp
            self.last=temp
            self.size+=1
        else:
            p=self.head
            self.head=temp
            self.head.nxt=p
            self.size+=1


    def r_push_beg(self,data,list):
        temp=node(data)
        temp.nxt=list
        list=temp
        return list


    def push_back(self,data):
        temp=node(data)
        self.last.nxt=temp
        self.last=temp
        self.size+=1


    def display(self):
        p=self.head
        t=self.size
        while p!=None:
            print(p.data,end=" -> ")
            p=p.nxt
            t-=1
        print("")


    def display1(self,list):
        p=list
        while p!=None:
            print(p.data,end=' -> ')
#            print(p.nxt)
            p=p.nxt
        print(" ")

    def rev_list(self,list):
        p=list.head
        n_revlist=node(list.head.data)
        p=p.nxt
        while(p!=None):
            n_revlist=self.r_push_beg(p.data,n_revlist)
            p=p.nxt
        return n_revlist



llist = linklist ()
llist.push_beg(5)
llist.push_beg(6)
llist.push_beg(7)
llist.push_beg(8)
llist.push_beg(9)
llist.display()
llist.push_back(99)
llist.push_back(97)
llist.push_back(96)
llist.push_back(95)
llist.display()
t=linklist()
z=t.rev_list(llist)
t.display1(z)
#print(z)
#print(llist.head)
