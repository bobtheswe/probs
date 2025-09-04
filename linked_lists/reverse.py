# Given the beginning of a singly linked list head, reverse the list, and return the new beginning of the list.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# first attempt
def fn(head):
    if head is None:
        return head
    stack = []

    #recursively build a stack of nodes
    def rescurse_into_stack(ll):
        if ll.next is None: # end of the list
            stack.append(ll)
            return
        rescurse_into_stack(ll.next)
        stack.append(ll)
    rescurse_into_stack(head)

    #iterate though stack and build a new list    
    new_ll = ListNode(stack[0].val)
    runner = new_ll

    for node in stack[1:]:
        runner.next = ListNode(node.val)
        runner = runner.next
    # return list
    return new_ll

# better solution   
def better_fn(head):
    curr, prev = head, None
    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    return prev