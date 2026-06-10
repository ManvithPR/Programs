nnode=Node(data) --> Create a new node
self.head=nnode --> Set the new node as the first node
cur.next= nnode --> link cur node to the new node
cur = self.head --> start from the head of the list
nnode.next = self.head --> Point new node to the head
cur = cur.next --> Move to next node
self.head = cur.next --> Update head to the node after cur
prev.next= cur.next ==> Skip cur node by linking previous to next node