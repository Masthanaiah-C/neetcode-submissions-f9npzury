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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode* fast = head;
        while (n) {
            fast = fast->next;
            n--;
        }
        ListNode* slow = head;
        if (slow == head && fast == nullptr) {
            return head-> next;
        }
        while((fast -> next!= nullptr) ) {
            fast = fast -> next;
            slow = slow->next;
        }
        
        cout<< fast->val <<slow->val;
        slow -> next = slow->next->next;
        return head;

    }
};