def removeDuplicates(self,head):
        #Write your code here
        current =head
        while current is not None and current.next is not None:
                        while current.next is not None and current.data is current.next.data:
                              current.next=current.next.next
                        current=current.next
        return head
