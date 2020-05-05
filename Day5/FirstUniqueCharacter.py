class node:
    def __init__(self,data):
        self.prev=None
        self.next=None
        self.val=data
        
class Solution:
    def firstUniqChar(self, s: str) -> int:
        dic={}
        head=None
        tail=None
        for index,char in enumerate(s):
            if char not in dic:
                temp=node(index)
                dic[char]=temp
                head,tail=self.insert(head,tail,temp)
            else:
                if dic[char]:
                    head,tail=self.delete(head,tail,dic[char])
                    dic[char]=None
        
        if tail:
            return tail.val
        else:
            return -1
        
    def insert(self,head,tail,temp):
        if not head:
            head=tail=temp
            return head,tail
        temp.next=head
        head.prev=temp
        head=temp
        return head,tail
    
    def delete(self,head,tail,node):
        if not node.prev and not node.next:
            head=tail=None
        elif not node.prev:
            head=head.next
            head.prev=None
        elif not node.next:
            tail=tail.prev
            tail.next=None
        else:
            node.prev.next=node.next
            node.next.prev=node.prev
        del node
        return head,tail
                
        