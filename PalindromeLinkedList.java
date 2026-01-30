class Solution {
    public boolean isPalindrome(ListNode head) {
      //middle
      ListNode slow=head;
      ListNode fast=head;
     while(fast!=null && fast.next!=null)
     {
        slow=slow.next;
        fast=fast.next.next;
     }

     //reverse
     ListNode prev=null;
     while(slow!=null)
     {
        ListNode next= slow.next;
        slow.next=prev;
        prev=slow;
        slow=next;
     }

ListNode first=head,second=prev;
while(second!=null)
{
    if(first.val!=second.val)
    {
        return false;
    }
    first=first.next;
    second=second.next;
}

return true;


    }
    
}