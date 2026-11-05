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


        std::cout<<prevleft->val<<currleft->val<<prevright->val<<currright->val<<endl;


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