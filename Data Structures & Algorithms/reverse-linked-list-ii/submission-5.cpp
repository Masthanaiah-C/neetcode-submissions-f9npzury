/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* reverseBetween(ListNode* head, int left, int right) {
        // Base cases - if head == null or left and right are equal
        if (!head || left==right) {
            return head;
        }
        
        ListNode* prevleft = head;
ListNode* currleft = head;
ListNode* prevright = head;
ListNode* currright = head;

// Find left boundary
for (int c = 2; c < left; c++) {
    prevleft = prevleft->next;
}

if (left == 1)
    currleft = head;
else
    currleft = prevleft->next;


// Find right boundary
for (int c = 2; c < right; c++) {
    prevright = prevright->next;
}

if (right == 1)
    currright = head;
else
    currright = prevright->next;




ListNode* temp = currleft->next;
ListNode* stop = currright -> next;
while (temp != stop) {
    currleft->next = temp->next;
    
    if (left == 1) {
        temp->next = head;
        head = temp;
    }
    else {
        temp->next = prevleft->next;
        prevleft->next = temp;
    }

    
    temp = currleft->next;
}


  return head;
        
    }
};

/***

ListNode* reverseBetween(ListNode* head, int left, int right) {

    if (!head || left == right)
        return head;

    ListNode dummy(0, head);
    ListNode* prev = &dummy;

    // Move prev to node before 'left'
    for (int i = 1; i < left; i++) {
        prev = prev->next;
    }

    ListNode* curr = prev->next;

    // Move each next node to front of reversed section
    for (int i = 0; i < right - left; i++) {

        ListNode* temp = curr->next;

        curr->next = temp->next;
        temp->next = prev->next;
        prev->next = temp;
    }

    return dummy.next;
}

*///